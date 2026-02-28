"""python-pt-br: Write Python code in Portuguese Brazilian.

This package enables developers to write Python code using pt-BR keywords
and built-in function names, making Python more accessible for Portuguese-
speaking learners.

Quick start:
    import pt_br
    imprimir("Olá, Mundo!")

How it works:
    1. Add 'import pt_br' at the top of your script
    2. Write Python code using pt-BR keywords
    3. Run the script normally: python script.py
    4. The pt-BR code is automatically translated to Python

No build steps, no CLI tools—just pure Python!
"""

__version__ = "0.1.0"
__author__ = "Wally Carvalho"
__author_email__ = "qzn2cpm83@mozmail.com"
__license__ = "MIT"

# Register the import hook when this module is imported
from .translator import register_translator

register_translator()

# Public API
from .translator import translate_source
from .mappings import (
    PT_BR_TO_PYTHON,
    PT_BR_KEYWORDS,
    PT_BR_BUILTINS,
    PYTHON_TO_PT_BR,
)
from .utils import debug_show_translation

__all__ = [
    "translate_source",
    "PT_BR_TO_PYTHON",
    "PT_BR_KEYWORDS",
    "PT_BR_BUILTINS",
    "PYTHON_TO_PT_BR",
    "debug_show_translation",
]
