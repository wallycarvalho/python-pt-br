"""Translation mappings for pt-BR to Python.

This module contains the central mapping dictionary that defines all
pt-BR to Python translations. It serves as the single source of truth
for the translator.

Structure:
    - PT_BR_TO_PYTHON: Main mapping dictionary
    - Organized by category for clarity
"""

# ============================================================================
# KEYWORDS & LOGICAL OPERATORS
# ============================================================================

PT_BR_KEYWORDS = {
    # Control Flow - Loops
    "para": "for",
    "em": "in",
    "enquanto": "while",
    # Control Flow - Conditionals
    "se": "if",
    "senao": "else",
    "senao_se": "elif",
    # Logical Operators
    "e": "and",
    "ou": "or",
    "nao": "not",
    # Boolean & Null Values
    "verdadeiro": "True",
    "falso": "False",
    "nulo": "None",
    # Loop Control
    "quebra": "break",
    "continua": "continue",
    # Function & Return
    "retorna": "return",
    # Function Definition (keep 'def' as-is, but add 'funcao' as alternative)
    "funcao": "def",
    # Class Definition
    "classe": "class",
}

# ============================================================================
# BUILT-IN FUNCTIONS
# ============================================================================

PT_BR_BUILTINS = {
    # I/O & Console
    "imprimir": "print",
    "entrada": "input",
    # Collections & Iteration
    "intervalo": "range",
    "lista": "list",
    "tupla": "tuple",
    "conjunto": "set",
    "dicionario": "dict",
    "enumerar": "enumerate",
    "compacta": "zip",
    "comprimento": "len",
    # Type Conversion
    "inteiro": "int",
    "flutuante": "float",
    "texto": "str",
    "booleano": "bool",
    # Aggregation & Sorting
    "soma": "sum",
    "minimo": "min",
    "maximo": "max",
    "classifica": "sorted",
    # Type & Introspection
    "tipo": "type",
    "eh_instancia": "isinstance",
    # Functional Programming
    "mapa": "map",
    "filtro": "filter",
}

# ============================================================================
# COMBINED MAPPING
# ============================================================================

PT_BR_TO_PYTHON = {**PT_BR_KEYWORDS, **PT_BR_BUILTINS}

# ============================================================================
# REVERSE MAPPING (For debugging/introspection)
# ============================================================================

PYTHON_TO_PT_BR = {v: k for k, v in PT_BR_TO_PYTHON.items()}

# ============================================================================
# CATEGORIES FOR REFERENCE
# ============================================================================

# All keywords (16 for MVP)
ALL_KEYWORDS = set(PT_BR_KEYWORDS.keys())

# All built-in functions (20+ for MVP)
ALL_BUILTINS = set(PT_BR_BUILTINS.keys())

# All translations
ALL_TRANSLATIONS = set(PT_BR_TO_PYTHON.keys())

# ============================================================================
# HELPER CONSTANTS
# ============================================================================

# Regular expression patterns for word boundary detection
# These are used by the translator to avoid replacing inside compound words
WORD_PATTERN = r"\b{}\b"

# Pattern for function call detection
FUNCTION_CALL_PATTERN = r"\b{}(?=\()"

# Debug: Print mapping statistics
if __name__ == "__main__":
    print("=" * 70)
    print("PT-BR TO PYTHON TRANSLATION MAPPINGS")
    print("=" * 70)
    print(f"\nKeywords: {len(PT_BR_KEYWORDS)}")
    for pt_br, python in sorted(PT_BR_KEYWORDS.items()):
        print(f"  {pt_br:20} → {python}")

    print(f"\nBuilt-in Functions: {len(PT_BR_BUILTINS)}")
    for pt_br, python in sorted(PT_BR_BUILTINS.items()):
        print(f"  {pt_br:20} → {python}")

    print(f"\nTotal Translations: {len(PT_BR_TO_PYTHON)}")
    print("=" * 70)
