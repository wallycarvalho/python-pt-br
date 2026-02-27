#!/usr/bin/env python3
"""Wrapper script to run pt-BR Python files.

Usage:
    python -m pt_br your_script.py [args...]

This script:
1. Reads the target script
2. Translates pt-BR → Python
3. Executes the translated code

This allows direct execution of pt-BR scripts.
"""

import sys
import os
from pathlib import Path

# Add the pt_br module to the path
import pt_br
from pt_br.translator import translate_source


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python -m pt_br script.py [arguments...]")
        print("\nRun a Python script that uses pt-BR keywords.")
        sys.exit(1)

    script_path = sys.argv[1]
    script_args = sys.argv[2:]

    # Check if the script exists
    if not os.path.exists(script_path):
        print(f"Error: File '{script_path}' not found")
        sys.exit(1)

    # Read the script
    try:
        with open(script_path, "r", encoding="utf-8") as f:
            source = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Translate pt-BR → Python
    try:
        translated = translate_source(source)
    except Exception as e:
        print(f"Error translating script: {e}")
        sys.exit(1)

    # Update sys.argv so the script sees its arguments correctly
    sys.argv = [script_path] + script_args

    # Create a module to execute in
    import types

    module = types.ModuleType("__main__")
    module.__file__ = script_path
    module.__spec__ = None

    # Execute the translated code
    try:
        code = compile(translated, script_path, "exec")
        exec(code, module.__dict__)
    except SystemExit as e:
        # Allow the script to call sys.exit()
        sys.exit(e.code)
    except Exception as e:
        print(f"Error executing script: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
