# Project Structure & Organization

## Directory Layout

```
python-pt-br/
├── README.md                      # Project overview, quick start
├── LICENSE                        # MIT or similar
├── setup.py                       # Package setup configuration
├── requirements.txt               # Dependencies (minimal)
├── .gitignore                     # Git ignore rules
│
├── pt_br/                         # Main package
│   ├── __init__.py               # Import hook registration + package init
│   ├── translator.py             # Core translation logic
│   ├── mappings.py               # pt-BR ↔ Python translation dictionary
│   └── utils.py                  # Helper utilities
│
├── tests/                         # Test suite
│   ├── __init__.py
│   ├── test_translator.py        # Unit tests for translator
│   ├── test_keywords.py          # Test keyword translations
│   ├── test_builtins.py          # Test built-in function translations
│   └── test_integration.py       # End-to-end integration tests
│
├── examples/                      # Example scripts in pt-BR
│   ├── hello_world.py            # Basic print example
│   ├── loops.py                  # for/while loop examples
│   ├── conditionals.py           # if/else examples
│   ├── functions.py              # Function definition examples
│   └── data_structures.py        # List/dict/tuple examples
│
├── docs/                          # Documentation
│   ├── GETTING_STARTED.md        # Installation & basic usage
│   ├── FULL_GUIDE.md             # Comprehensive guide
│   └── TROUBLESHOOTING.md        # Common issues & fixes
│
└── planning/                      # Planning documents (this phase)
    ├── 01-ARCHITECTURE.md        # Architecture & design
    ├── 02-KEYWORD_MAPPING.md     # Keyword translations
    ├── 03-PROJECT_STRUCTURE.md   # This file
    ├── 04-MVP_SCOPE.md           # MVP definition & requirements
    └── 05-IMPLEMENTATION_PLAN.md # Step-by-step implementation roadmap
```

---

## File Descriptions & Responsibilities

### Core Package Files

#### `pt_br/__init__.py`
**Purpose**: Package initialization and import hook registration

**Contents**:
```
- Version string: __version__ = "0.1.0"
- Import hook registration (register with sys.meta_path)
- Expose public API (what users can import)
- Docstring explaining how to use the package
```

**Key Responsibility**: Make `import pt_br` work and activate the translator

---

#### `pt_br/translator.py`
**Purpose**: Core translation engine

**Key Functions**:
- `translate_source(source_code: str) -> str`
  - Takes pt-BR source code as string
  - Returns Python-compatible source code
  - Handles keyword and function name replacements

- `should_translate_token(token: str, context: str) -> bool`
  - Determines if a token should be translated based on context
  - Avoids translating inside strings/comments

- `create_translator_finder()` → Custom finder class
  - Returns a class implementing `meta_path` finder/loader protocol
  - Intercepts module imports

**Key Responsibility**: Implement the translation algorithm

---

#### `pt_br/mappings.py`
**Purpose**: Centralized translation dictionary

**Contents**:
```
PT_BR_TO_PYTHON = {
    # Keywords
    'para': 'for',
    'em': 'in',
    'se': 'if',
    'senao': 'else',
    ...
    
    # Built-in functions
    'imprimir': 'print',
    'intervalo': 'range',
    ...
}

# Optional: reverse mapping for debugging
PYTHON_TO_PT_BR = {v: k for k, v in PT_BR_TO_PYTHON.items()}
```

**Key Responsibility**: Single source of truth for all translations

---

#### `pt_br/utils.py`
**Purpose**: Helper functions and utilities

**Key Functions**:
- `is_inside_string(source: str, position: int) -> bool`
  - Check if a position is inside a string literal

- `is_inside_comment(source: str, position: int) -> bool`
  - Check if a position is inside a comment

- `is_word_boundary(source: str, position: int) -> bool`
  - Check if position is at word boundary (don't translate if not)

- `debug_show_translation(pt_br_code: str, python_code: str) -> None`
  - Print side-by-side comparison (useful for debugging)

**Key Responsibility**: Utility functions to support translator and testing

---

### Test Files

#### `tests/test_translator.py`
**Purpose**: Unit tests for translation engine

**Test Categories**:
- Basic translation (single keyword)
- Multiple keywords in one line
- Nested keywords (if inside for loop)
- Edge cases (word boundaries, false matches)

---

#### `tests/test_keywords.py`
**Purpose**: Test each keyword translation individually

**Structure**:
```
test_keyword_para()     # for loop
test_keyword_se()       # if statement
test_keyword_senao()    # else statement
... (one test per keyword)
```

---

#### `tests/test_builtins.py`
**Purpose**: Test built-in function translations

**Structure**:
```
test_builtin_imprimir()  # print function
test_builtin_intervalo() # range function
... (one test per function)
```

---

#### `tests/test_integration.py`
**Purpose**: End-to-end tests with real pt-BR scripts

**Examples**:
- Run complete script in pt-BR, verify output
- Test example scripts from `examples/` directory
- Test combinations of multiple features

---

### Example Scripts

#### `examples/hello_world.py`
```python
import pt_br

imprimir("Olá, Mundo!")
```

#### `examples/loops.py`
```python
import pt_br

# for loop example
para i em intervalo(5):
    imprimir(i)

# while loop example
x = 0
enquanto x < 3:
    imprimir(x)
    x = x + 1
```

#### `examples/conditionals.py`
```python
import pt_br

idade = 18

se idade >= 18:
    imprimir("Você é um adulto")
senao:
    imprimir("Você é menor de idade")
```

#### `examples/functions.py`
```python
import pt_br

def saudacao(nome):
    imprimir(f"Olá, {nome}!")

saudacao("Maria")
```

#### `examples/data_structures.py`
```python
import pt_br

numeros = [1, 2, 3, 4, 5]
imprimir(comprimento(numeros))
imprimir(soma(numeros))
imprimir(minimo(numeros))
imprimir(maximo(numeros))
```

---

### Documentation Files

#### `docs/GETTING_STARTED.md`
**Contents**:
- Installation instructions: `pip install python-pt-br`
- Basic usage: "import pt_br at the top"
- First example: hello world
- Common patterns: loops, conditionals, functions

#### `docs/FULL_GUIDE.md`
**Contents**:
- Complete reference of all keywords/functions
- How import hooks work (explanation)
- Advanced usage
- Debugging tips

#### `docs/TROUBLESHOOTING.md`
**Contents**:
- FAQ
- Common errors and solutions
- Known limitations
- How to report issues

---

### Planning Documents (This Phase)

These files live in `planning/` to keep them separate from code:

1. `01-ARCHITECTURE.md` ✅ (created)
   - Design decisions, component overview, execution flow

2. `02-KEYWORD_MAPPING.md` ✅ (created)
   - Full translation dictionary, phased rollout

3. `03-PROJECT_STRUCTURE.md` (this file)
   - Directory layout, file descriptions, responsibilities

4. `04-MVP_SCOPE.md` (next)
   - MVP requirements, success criteria, assumptions

5. `05-IMPLEMENTATION_PLAN.md` (next)
   - Step-by-step implementation roadmap, milestones

---

## Package Dependencies

### `setup.py` Configuration

**Runtime Dependencies**: None (pure Python)
- Leverage Python's built-in `importlib` and `sys` modules
- No external packages needed for MVP

**Development Dependencies**:
- `pytest`: Testing framework
- `pytest-cov`: Code coverage reporting

**Metadata**:
- Package name: `python-pt-br`
- Version: `0.1.0`
- Python version: `>=3.8` (import hooks stable)
- License: MIT
- Description: "Write Python code in Portuguese Brazilian"

---

## File Ownership & Responsibilities

| File/Directory | Responsibility | Phase |
|---|---|---|
| `pt_br/__init__.py` | Register import hook | MVP Phase 1 |
| `pt_br/translator.py` | Implement translation engine | MVP Phase 1 |
| `pt_br/mappings.py` | Define keyword/function mappings | MVP Phase 1 |
| `pt_br/utils.py` | Provide helper functions | MVP Phase 1 |
| `tests/` | Comprehensive test coverage | MVP Phase 1 |
| `examples/` | Demonstrate features | MVP Phase 2 |
| `docs/` | User documentation | MVP Phase 2 |
| `planning/` | Planning documents | Planning Phase |

---

## Naming Conventions

### Python Files
- Use `lowercase_with_underscores` for file names
- Use `lowercase_with_underscores` for function names
- Use `CamelCase` for class names
- Use `UPPERCASE_WITH_UNDERSCORES` for constants

### Package Structure
- Main package: `pt_br` (lowercase, abbreviated, clear)
- Modules inside: descriptive names (`translator`, `mappings`, `utils`)

### Test Files
- Pattern: `test_*.py` (pytest convention)
- Test functions: `test_<feature>_<scenario>()`

---

## Version Control

### `.gitignore` Essentials
```
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.pytest_cache/
.coverage
htmlcov/
.env
.DS_Store
```

### Commit Strategy
- Semantic commits: `feat:`, `fix:`, `test:`, `docs:`, `refactor:`
- Example: `feat: implement translator for keywords`

---

## Summary

This structure provides:
- ✅ **Clear separation of concerns**: Core logic, translation, utilities, tests
- ✅ **Easy to find things**: Logical grouping, descriptive names
- ✅ **Scalable**: Easy to add new modules, extend mappings
- ✅ **Testable**: Dedicated test directory with clear organization
- ✅ **Documented**: Examples and docs for users
- ✅ **Maintainable**: Single source of truth (mappings.py), helper utilities

---

**Next Steps**: See `04-MVP_SCOPE.md` for MVP requirements and success criteria
