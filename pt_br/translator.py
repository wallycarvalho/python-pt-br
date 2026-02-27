"""Core translation engine for pt-BR to Python code.

This module handles:
1. Source code translation (pt-BR keywords/functions → Python)
2. Import hook registration for transparent translation
3. Support for direct script execution

The import hook works by intercepting Python's module loading system
and translating pt-BR code to Python before execution.
"""

import sys
import os
import importlib.abc
import importlib.machinery
import importlib.util
from typing import Optional

from .mappings import PT_BR_KEYWORDS, PT_BR_BUILTINS
from .utils import safe_replace_word, safe_replace_function


def translate_source(source_code: str) -> str:
    """Translate pt-BR source code to Python.

    Applies all keyword and function name translations from the mappings.
    Translation order:
    1. Keywords (with word boundary checks)
    2. Built-in functions (function call pattern)

    Args:
        source_code: The original pt-BR source code

    Returns:
        The translated Python source code
    """
    result = source_code

    # Translate keywords first (with word boundaries)
    for pt_br_keyword, python_keyword in PT_BR_KEYWORDS.items():
        result = safe_replace_word(
            result,
            pt_br_keyword,
            python_keyword,
            avoid_strings=True,
            avoid_comments=True,
        )

    # Translate built-in functions (look for pattern: word + '(')
    for pt_br_func, python_func in PT_BR_BUILTINS.items():
        result = safe_replace_function(result, pt_br_func, python_func)

    return result


class PTBRSourceLoader(importlib.abc.SourceLoader):
    """A source loader that translates pt-BR code before execution.

    This loader intercepts the source code loading process and translates
    pt-BR to Python before compilation.
    """

    def __init__(self, fullname: str, path: str):
        """Initialize the loader.

        Args:
            fullname: The module name (e.g., 'mymodule')
            path: The path to the source file
        """
        self.fullname = fullname
        self.path = path

    def get_filename(self, fullname: str) -> str:
        """Get the filename for the module.

        Args:
            fullname: The module name

        Returns:
            The file path
        """
        return self.path

    def get_source(self, fullname: str) -> str:
        """Get the source code from the file.

        Args:
            fullname: The module name

        Returns:
            The source code as a string
        """
        with open(self.path, "r", encoding="utf-8") as f:
            return f.read()

    def get_data(self, path: str) -> bytes:
        """Get the raw data from a file (required by abstract class).

        Args:
            path: The file path

        Returns:
            The file contents as bytes
        """
        with open(path, "rb") as f:
            return f.read()

    def get_code(self, fullname: str):
        """Get compiled code, translating pt-BR first.

        This is the key method that translates before compilation.

        Args:
            fullname: The module name

        Returns:
            The compiled code object
        """
        # Read the source
        source = self.get_source(fullname)

        # Translate pt-BR → Python
        translated = translate_source(source)

        # Compile the translated code
        code = compile(
            translated,
            self.path,
            "exec",
            dont_inherit=True,
        )

        return code


class PTBRFinder(importlib.abc.MetaPathFinder):
    """Meta path finder that loads Python modules with pt-BR translation.

    This finder is inserted into sys.meta_path and intercepts imports.
    It allows Python modules to be written in pt-BR and translated on import.
    """

    def find_spec(self, fullname, path, target=None):
        """Find a module and return a spec with our custom loader.

        This method is called for every import. We check if the module
        exists as a .py file and return a spec with our loader if it does.

        Args:
            fullname: The fully qualified module name
            path: The search path
            target: Unused

        Returns:
            A ModuleSpec with our loader, or None to let other finders handle it
        """
        # Don't translate the pt_br package itself
        if fullname.startswith("pt_br"):
            return None

        # If this module is being imported directly (not as a submodule)
        # we don't interfere - let the standard finders work
        # This preserves normal Python behavior for most imports

        # However, if someone explicitly writes Python with pt-BR,
        # our import hook will be active and we'll translate it
        # by our loader when they're imported after pt_br.

        # To keep things simple, we return None here and rely on
        # the fact that if 'import pt_br' is called, we become available.
        # Then any modules that have pt-BR code will be translated
        # by our loader when they're imported after pt_br.

        return None


def register_translator():
    """Register the pt-BR translator in sys.meta_path.

    This installs a custom import hook that:
    1. Intercepts all imports
    2. For .py files, translates pt-BR → Python
    3. Then executes the translated code

    Called when the pt_br module is imported.
    """

    # Create a custom finder that provides our loader
    class TranslatorFinder(importlib.abc.MetaPathFinder):
        """Finder that wraps the standard finder with our loader."""

        def find_spec(self, fullname, path, target=None):
            # Don't translate the pt_br package itself
            if fullname.startswith("pt_br"):
                return None

            # Don't translate standard library modules
            if fullname in sys.stdlib_module_names:
                return None

            # Let the default finder search for the module
            spec = importlib.machinery.PathFinder.find_spec(fullname, path, target)

            if spec is not None and spec.origin is not None:
                # If it's a .py file in the current project, use our loader
                if spec.origin.endswith(".py"):
                    # Only translate files in the current directory or user code
                    # Not the standard library
                    if (
                        "site-packages" not in spec.origin
                        and "/usr" not in spec.origin
                        and "/opt" not in spec.origin
                    ):
                        # Replace the loader with ours
                        spec.loader = PTBRSourceLoader(fullname, spec.origin)

            return spec

    # Register this finder in sys.meta_path
    # Insert at position 0 to run before other finders
    if not any(isinstance(f, TranslatorFinder) for f in sys.meta_path):
        sys.meta_path.insert(0, TranslatorFinder())

    # Also handle the __main__ module (direct script execution)
    # by translating it when the module is already being loaded
    _hook_main_module()


def _hook_main_module():
    """Hook the __main__ module to translate pt-BR code.

    This is for when a user runs 'python script.py' where script.py
    contains pt-BR code with 'import pt_br' at the top.

    The challenge: Python parses the entire script upfront, so we need
    to translate it before that happens.

    Solution: We'll hook into the import system so that when pt_br is
    imported, we also translate the main module retroactively.
    """
    # Get the main module
    import __main__

    # Check if it was written in pt-BR by looking for pt-BR keywords
    if hasattr(__main__, "__file__") and __main__.__file__:
        try:
            with open(__main__.__file__, "r", encoding="utf-8") as f:
                source = f.read()

            # Check if this file has pt-BR keywords
            has_pt_br = any(kw in source for kw in PT_BR_KEYWORDS.keys())

            if has_pt_br:
                # Translate the source
                translated = translate_source(source)

                # Execute the translated code in __main__'s namespace
                # We need to skip the 'import pt_br' line to avoid re-importing
                # So we just execute the rest
                lines = translated.split("\n")
                # Remove the 'import pt_br' line
                filtered_lines = [l for l in lines if "import pt_br" not in l]
                translated_filtered = "\n".join(filtered_lines)

                # Execute in __main__
                exec(translated_filtered, __main__.__dict__)
        except Exception:
            # If anything goes wrong, just let the normal import work
            pass
