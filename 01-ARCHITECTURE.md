# Architecture & Design

## Project Overview

**python-pt-br** is a Python package that enables Portuguese Brazilian (pt-BR) speakers to write Python code using pt-BR keywords and built-in function names, while maintaining full compatibility with standard Python.

## Core Approach: Import Hook (Wrapper)

### How It Works

1. **User writes a `.py` file** in pt-BR:
   ```python
   # exemplo.py
   import pt_br
   
   para i em intervalo(5):
       imprimir(i)
   ```

2. **Import Hook intercepts** the file loading process
   - Before Python parses the code, the hook translates pt-BR keywords → Python keywords
   - Translation happens transparently at import time

3. **Python executes** the translated code:
   ```python
   # What Python actually sees:
   for i in range(5):
       print(i)
   ```

### Key Design Principles

| Principle | Description |
|-----------|-------------|
| **Zero Friction** | Users write `.py` files and execute them normally—no build steps, no CLI tools |
| **Transparency** | Translation is invisible; users can inspect translated code if needed (debug mode) |
| **Pythonic** | Leverages Python's import system (PEP 302 import hooks), uses standard Python conventions |
| **Educational** | Simple, readable codebase; easy for learners to understand how it works |
| **Extensible** | Architecture supports adding more languages/keywords without major refactoring |

## Technical Architecture

### Component Overview

```
┌─────────────────────────────────────────┐
│   User writes code in pt-BR (.py)       │
├─────────────────────────────────────────┤
│                                         │
│  python-pt-br Package                   │
│  ├── pt_br/__init__.py                  │
│  │   └── Registers import hook          │
│  │                                      │
│  ├── pt_br/translator.py                │
│  │   └── Handles keyword translation    │
│  │                                      │
│  ├── pt_br/mappings.py                  │
│  │   └── pt-BR → Python keyword map     │
│  │                                      │
│  └── pt_br/utils.py                     │
│      └── Helper functions               │
│                                         │
├─────────────────────────────────────────┤
│  Python's Import System                 │
│  (meta_path, importlib)                 │
├─────────────────────────────────────────┤
│  Translated Python Code                 │
│  (ready for execution)                  │
└─────────────────────────────────────────┘
```

### Main Components

#### 1. **Import Hook** (`pt_br/__init__.py`)
- Registers a custom finder/loader with `sys.meta_path`
- Intercepts module imports and delegates to translator
- Minimal—just sets up the hook

#### 2. **Translator** (`pt_br/translator.py`)
- Core logic: takes pt-BR source code, returns Python source code
- Uses regex/string replacement for keyword translation
- Handles edge cases (strings, comments, etc.)
- Responsible for source code transformation

#### 3. **Keyword Mappings** (`pt_br/mappings.py`)
- Centralized dictionary of pt-BR ↔ Python translations
- Easy to maintain, easy to extend for other languages later
- Includes: keywords, built-ins, operators

#### 4. **Utilities** (`pt_br/utils.py`)
- Helper functions for translation (e.g., `should_translate_in_context()`)
- Debug utilities (e.g., `show_translation()` to inspect translated code)
- Validation helpers

## Translation Strategy

### Two-Phase Approach

#### Phase 1: Simple Token Replacement
- Replace pt-BR keywords with Python equivalents using regex patterns
- Handle common cases: `para` → `for`, `em` → `in`, `ou` → `or`, etc.
- Avoid translating inside strings/comments

#### Phase 2: Function/Method Translation
- Replace built-in function names: `imprimir()` → `print()`, `intervalo()` → `range()`
- Handle method chains and attribute access
- Preserve all arguments as-is

### Translation Safeguards

To avoid translating inside strings/comments:
- Use simple regex lookahead/lookbehind to detect context
- For MVP: Conservative approach (only translate in "safe" contexts)
- Future: Full AST parsing for 100% accuracy

## Execution Flow

```
1. User: python exemplo.py
   ↓
2. Python loads exemplo.py
   ↓
3. Import hook intercepts (before parsing)
   ↓
4. Translator reads source code
   ↓
5. Translator applies pt-BR → Python mappings
   ↓
6. Python receives translated code
   ↓
7. Python parses & executes normally
   ↓
8. Program runs with expected output
```

## Why This Approach?

| Aspect | Why Import Hook? |
|--------|------------------|
| **Performance** | No build step, no CLI tool, no pre-processing—translation happens once at import |
| **Simplicity** | No external dependencies, uses Python's built-in import system |
| **Pythonic** | Follows Python conventions (import hooks are standard) |
| **Educational** | Easy to understand: "import pt_br does magic import stuff" |
| **Friction** | Minimal—one import line, then write code normally |
| **Debugging** | Users can see translated code, inspect what happened |

## Limitations & Considerations

1. **Order of import matters**: `import pt_br` must come before any pt-BR code
2. **Only .py files**: Direct execution via `python script.py` works; REPL/interactive mode is trickier
3. **String/comment handling**: Simple approach may miss edge cases (future improvement)
4. **IDE/linting support**: IDEs won't recognize pt-BR keywords (educational focus, acceptable tradeoff)
5. **Error messages**: Stack traces show translated Python code, not original pt-BR

## Future Evolution

Once MVP is solid, we could:
- Support other languages by adding new mappings
- Add AST-based translation for 100% accuracy
- Create IDE extensions for pt-BR keyword recognition
- Build a REPL for interactive pt-BR coding
- Generate `.ptbr` files that compile to `.py`

---

**Next Steps**: See `02-KEYWORD_MAPPING.md` for initial pt-BR ↔ Python translations
