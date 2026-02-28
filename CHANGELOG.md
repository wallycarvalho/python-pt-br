# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-02-28

### Initial MVP Release

This is the first public release of python-pt-br, bringing Portuguese Brazilian language support to Python development.

### Added

#### Core Features
- **16 Portuguese Keywords** - Write control flow in pt-BR:
  - `funcao` (def), `classe` (class)
  - `para` (for), `em` (in), `enquanto` (while)
  - `se` (if), `senao_se` (elif), `senao` (else)
  - `retorna` (return), `quebra` (break), `continua` (continue)
  - `e` (and), `ou` (or), `nao` (not)
  - `verdadeiro` (True), `falso` (False), `nulo` (None)

- **20+ Built-in Functions** - Standard Python functions in Portuguese:
  - I/O: `imprimir()` (print), `entrada()` (input)
  - Collections: `lista()`, `tupla()`, `conjunto()`, `dicionario()`, `intervalo()` (range)
  - Type Conversion: `inteiro()`, `flutuante()`, `texto()`, `booleano()`
  - Aggregation: `soma()` (sum), `minimo()` (min), `maximo()` (max), `classifica()` (sorted)
  - Utilities: `comprimento()` (len), `enumerar()` (enumerate), `compacta()` (zip)
  - Introspection: `tipo()` (type), `eh_instancia()` (isinstance)
  - Functional: `mapa()` (map), `filtro()` (filter)

- **Import Hook System** - Seamless translation:
  - Zero friction - just add `import pt_br` at the top
  - Automatic translation on module import
  - Works with `python -m pt_br script.py` or direct execution

- **5 Example Scripts** - Learn by doing:
  - `hello_world.py` - Basic output and variables
  - `loops.py` - For and while loops with nested examples
  - `conditionals.py` - If/elif/else with logical operators
  - `functions.py` - Function definitions, parameters, and return values
  - `data_structures.py` - Lists, tuples, dicts, sets, and operations

#### Documentation
- **Getting Started Guide** (`docs/GETTING_STARTED.md`) - Beginner-friendly quick start
  - Installation and setup instructions
  - Your first program walkthrough
  - Common patterns with examples
  - Complete keywords and functions reference
  - Important notes and limitations

- **Complete Reference Guide** (`docs/FULL_GUIDE.md`) - Technical documentation
  - Detailed explanation of all 16 keywords
  - Complete documentation of all 20+ built-in functions
  - Usage examples for each keyword and function
  - Advanced patterns and use cases
  - Known limitations and design decisions

- **Troubleshooting Guide** (`docs/TROUBLESHOOTING.md`) - Problem solving
  - Solutions for common runtime errors
  - Function recognition and import issues
  - Logic errors and debugging strategies
  - String/output formatting issues
  - Type conversion gotchas
  - IDE and editor limitations

### Technical Details

- **Language:** Python 3.8+
- **License:** MIT
- **Dependencies:** None (zero external dependencies for runtime)
- **Code Coverage:** 181 tests with 69% coverage
  - 73 tests for translation engine
  - 46 tests for utility functions
  - 43 tests for keyword/function mappings
  - 19 integration tests with real-world scenarios

### Known Limitations

- **Object Methods** - Method names on built-in types remain in English:
  - Use `.append()` instead of `.acrescentar()` on lists
  - Future enhancement to support Portuguese method names planned
  
- **IDE Support** - Limited but acceptable for educational use:
  - Syntax highlighting may not recognize pt-BR keywords
  - Code completion won't suggest pt-BR names
  - This is expected and doesn't affect execution

- **Import Hook Scope** - Only applies to .py files:
  - C extensions and other modules use English names only
  - Type annotations must use English names

### How to Use

#### Installation
```bash
pip install python-pt-br
```

#### Your First Program
```python
import pt_br

imprimir("Olá, Mundo!")

para i em intervalo(5):
    imprimir(f"Número: {i}")
```

#### Running Your Code
```bash
# Method 1: Using the module runner (recommended)
python -m pt_br seu_script.py

# Method 2: Direct execution (requires 'import pt_br' at top)
python seu_script.py
```

### What's Next

For future releases, we're planning:
- CI/CD automation (GitHub Actions)
- Automated PyPI publishing on release tags
- Portuguese method names for built-in types
- IDE/VSCode plugin support
- Debugging tools and utilities
- Community contributions framework

### Contributors

- Wally Carvalho

### Acknowledgments

- The Python community for creating an extensible platform
- Portuguese-speaking learners who inspired this project

---

## [Unreleased]

Future enhancements and improvements being considered:
- Method translation support (`.acrescentar()` for `.append()`, etc.)
- GitHub Actions CI/CD pipeline
- VSCode extension for better IDE integration
- Additional language support (Spanish, French, etc.)
- Offline translation tools
- Educational IDE built on python-pt-br
