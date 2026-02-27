# Implementation Plan & Roadmap

## Overview

This document outlines the step-by-step implementation plan to build the MVP of python-pt-br. It breaks down the work into manageable phases with clear milestones, dependencies, and checkpoints.

---

## Phase 0: Project Setup (0.5 hours)

### Objectives
- Initialize Git repository
- Create basic project structure
- Set up `setup.py` and package metadata
- Create `.gitignore`

### Tasks

#### Task 0.1: Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial project setup"
```

#### Task 0.2: Create `setup.py`
**File**: `setup.py`

**Contents**:
```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-pt-br",
    version="0.1.0",
    author="[Your Name]",
    author_email="[your.email@example.com]",
    description="Write Python code in Portuguese Brazilian",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/python-pt-br",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Topic :: Education",
    ],
    python_requires=">=3.8",
    install_requires=[],  # No external dependencies
    extras_require={
        "dev": ["pytest>=7.0", "pytest-cov>=4.0"],
    },
)
```

#### Task 0.3: Create `.gitignore`
**File**: `.gitignore`

```
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.pytest_cache/
.coverage
htmlcov/
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
.DS_Store
*.swp
*.swo
*~
.idea/
.vscode/
*.code-workspace
```

#### Task 0.4: Create `requirements.txt` (Development)
**File**: `requirements.txt`

```
pytest>=7.0
pytest-cov>=4.0
```

#### Task 0.5: Create README Skeleton
**File**: `README.md`

```markdown
# python-pt-br

Write Python code in Portuguese Brazilian!

## Quick Start

```python
import pt_br

imprimir("Olá, Mundo!")
```

## Installation

```bash
pip install python-pt-br
```

## Supported Keywords & Functions

See [documentation](docs/GETTING_STARTED.md) for full list.

## License

MIT
```

### Deliverable
- ✅ Git repository initialized
- ✅ Project structure created
- ✅ Setup files in place

### Checkpoint
```bash
# Verify structure
ls -la
# Should see: setup.py, .gitignore, README.md, pt_br/, tests/, etc.
```

---

## Phase 1: Core Translator Implementation (2-3 hours)

### Objectives
- Implement translation engine
- Define keyword/function mappings
- Create import hook system
- Basic error handling

### Deliverables
- `pt_br/mappings.py`: Translation dictionary
- `pt_br/translator.py`: Translation engine
- `pt_br/utils.py`: Helper utilities
- `pt_br/__init__.py`: Import hook registration

---

### Task 1.1: Create `pt_br/mappings.py`

**Purpose**: Single source of truth for all translations

**Implementation**:
```python
# Define mapping dictionaries
PT_BR_TO_PYTHON_KEYWORDS = {...}
PT_BR_TO_PYTHON_BUILTINS = {...}
COMBINED_MAPPINGS = {...}
```

**Scope**: Include all MVP keywords and functions from `02-KEYWORD_MAPPING.md`

**Checkpoint**:
- ✅ Mapping file created
- ✅ All 16 keywords defined
- ✅ All 10 core functions defined
- ✅ No syntax errors

---

### Task 1.2: Create `pt_br/utils.py`

**Purpose**: Helper functions for translation and context detection

**Key Functions to Implement**:

1. `is_inside_string(source: str, position: int) -> bool`
   - Detect if position is inside a string literal
   - Handle both single and double quotes
   - Handle escaped quotes

2. `is_inside_comment(source: str, position: int) -> bool`
   - Detect if position is inside a comment
   - Handle `#` comments

3. `safe_replace_word(source: str, old: str, new: str) -> str`
   - Replace word boundaries only
   - Use regex with `\b` word boundary markers

4. `is_word_boundary(source: str, position: int) -> bool`
   - Check if position is at a word boundary

**Checkpoint**:
- ✅ All helper functions implemented
- ✅ Functions are testable (unit tested)
- ✅ Handle edge cases

---

### Task 1.3: Create `pt_br/translator.py`

**Purpose**: Core translation engine

**Key Class/Functions**:

1. `TranslatorFinder` class
   - Implements `meta_path` protocol
   - `find_module(fullname, path=None)` or `find_spec(fullname, path, target=None)`
   - Returns custom loader

2. `TranslatorLoader` class
   - Loads and translates module source
   - `exec_module(module)` to execute translated code

3. `translate_source(source_code: str) -> str`
   - Main translation function
   - Input: pt-BR source code
   - Output: Python-compatible source code
   - Algorithm:
     ```
     1. Read source code as string
     2. For each mapping (keyword/function):
        a. Use regex to find all occurrences
        b. Check context (not in string/comment)
        c. Replace with Python equivalent
     3. Return translated code
     ```

**Implementation Notes**:
- Use `re` module for pattern matching
- Iterate through mappings in a safe order (avoid conflicts)
- Preserve formatting/indentation
- Handle both `.py` and `.ptbr` files (if desired)

**Checkpoint**:
- ✅ Finder/loader classes implemented
- ✅ `translate_source()` works for basic cases
- ✅ Handles context detection (strings/comments)

---

### Task 1.4: Create `pt_br/__init__.py`

**Purpose**: Package initialization and import hook registration

**Implementation**:
```python
__version__ = "0.1.0"

# Import and register the translator
from . import translator

# Install import hook
import sys
sys.meta_path.insert(0, translator.TranslatorFinder())

# Optional: expose public API
from .translator import translate_source
from .mappings import PT_BR_TO_PYTHON_KEYWORDS, PT_BR_TO_PYTHON_BUILTINS

__all__ = [
    "translate_source",
    "PT_BR_TO_PYTHON_KEYWORDS",
    "PT_BR_TO_PYTHON_BUILTINS",
]
```

**Checkpoint**:
- ✅ Import hook registers without errors
- ✅ `import pt_br` works
- ✅ Hook doesn't break other imports

---

### Phase 1 Validation

#### Test 1.1: Direct Translation
```python
# In a test file
from pt_br.translator import translate_source

source = "para i em intervalo(5):\n    imprimir(i)"
translated = translate_source(source)
assert "for i in range(5):" in translated
assert "print(i)" in translated
```

#### Test 1.2: Import Hook
```python
# Create temp file: test_hook.py
import pt_br
imprimir("Hello")

# Run: python test_hook.py
# Should print: Hello
```

---

## Phase 2: Testing Suite (2-3 hours)

### Objectives
- Write comprehensive unit tests
- Write integration tests
- Achieve 90%+ code coverage
- Test all keywords and functions

### Deliverables
- `tests/test_translator.py`: Unit tests for translator
- `tests/test_keywords.py`: Test each keyword
- `tests/test_builtins.py`: Test each built-in function
- `tests/test_integration.py`: End-to-end tests

---

### Task 2.1: Create `tests/test_translator.py`

**Test Cases**:
1. Basic keyword translation
2. Multiple keywords in one line
3. Nested structures (if inside for)
4. Context detection (strings, comments)
5. Function name translation
6. Edge cases (variable names with pt-BR words)

**Example**:
```python
import pytest
from pt_br.translator import translate_source

def test_translate_simple_keyword():
    source = "para i em intervalo(5):\n    pass"
    result = translate_source(source)
    assert "for i in range(5):" in result

def test_translate_with_strings():
    source = 'imprimir("para sempre")'
    result = translate_source(source)
    assert 'print("para sempre")' in result
    # "para" inside string should NOT be translated to "for"
```

---

### Task 2.2: Create `tests/test_keywords.py`

**Structure**: One test per keyword

```python
def test_keyword_para(): ...
def test_keyword_em(): ...
def test_keyword_se(): ...
def test_keyword_senao(): ...
def test_keyword_enquanto(): ...
def test_keyword_e(): ...
def test_keyword_ou(): ...
def test_keyword_nao(): ...
# ... and so on
```

**Each test**:
- Translates a simple code snippet with the keyword
- Verifies the translation is correct
- Executes the translated code if possible (integration)

---

### Task 2.3: Create `tests/test_builtins.py`

**Structure**: One test per function

```python
def test_builtin_imprimir(): ...
def test_builtin_intervalo(): ...
def test_builtin_entrada(): ...
def test_builtin_comprimento(): ...
# ... and so on
```

**Each test**:
- Translates code using the function
- Verifies translation is correct
- Tests that the function works after translation

---

### Task 2.4: Create `tests/test_integration.py`

**Test Cases**:
1. Run example scripts (hello_world, loops, etc.)
2. Verify output matches expected
3. Test error handling
4. Test import hook doesn't break other modules

**Example**:
```python
import subprocess
import sys

def test_hello_world_example():
    result = subprocess.run(
        [sys.executable, "examples/hello_world.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Olá, Mundo!" in result.stdout
```

---

### Task 2.5: Setup & Configuration

**File**: `tests/__init__.py`
- Empty or minimal (pytest requires this)

**File**: `pytest.ini` or `pyproject.toml`
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

**Run Tests**:
```bash
pytest tests/
pytest tests/ --cov=pt_br --cov-report=html
```

### Phase 2 Validation

#### Coverage Check
```bash
pytest tests/ --cov=pt_br --cov-report=term-missing
# Target: 90%+ coverage
```

#### All Tests Pass
```bash
pytest tests/ -v
# All tests should pass
```

---

## Phase 3: Examples & Documentation (1-2 hours)

### Objectives
- Create working example scripts
- Write comprehensive documentation
- Make it easy for users to get started

### Deliverables
- `examples/hello_world.py`
- `examples/loops.py`
- `examples/conditionals.py`
- `examples/functions.py`
- `examples/data_structures.py`
- `docs/GETTING_STARTED.md`
- `docs/FULL_GUIDE.md`
- `docs/TROUBLESHOOTING.md`

---

### Task 3.1: Create Example Scripts

**Each example should**:
- Be simple and educational
- Demonstrate a specific feature
- Include comments explaining the code
- Be runnable: `python examples/hello_world.py`

**Example**: `examples/hello_world.py`
```python
import pt_br

# Imprimir é a tradução para print()
imprimir("Olá, Mundo!")
```

---

### Task 3.2: Write Getting Started Guide

**File**: `docs/GETTING_STARTED.md`

**Contents**:
- Installation: `pip install python-pt-br`
- First program: hello_world.py
- How it works: explanation of import hook
- Common patterns: loops, conditionals, functions
- Supported keywords/functions table
- Troubleshooting

---

### Task 3.3: Write Full Guide

**File**: `docs/FULL_GUIDE.md`

**Contents**:
- Complete reference of all keywords
- Complete reference of all functions
- Examples for each keyword/function
- Advanced usage (if applicable)
- Known limitations

---

### Task 3.4: Write Troubleshooting

**File**: `docs/TROUBLESHOOTING.md`

**Contents**:
- FAQ
- Common errors and solutions
- Known limitations
- How to debug translation

---

### Phase 3 Validation

#### Examples Run Without Errors
```bash
python examples/hello_world.py
python examples/loops.py
python examples/conditionals.py
python examples/functions.py
python examples/data_structures.py
```

#### Documentation is Complete
- ✅ README is clear
- ✅ Getting Started guide covers basics
- ✅ Full Guide has all keywords/functions
- ✅ Troubleshooting answers common questions

---

## Phase 4: Package Release (0.5-1 hour)

### Objectives
- Prepare package for distribution
- Verify installation works
- Release to PyPI (optional for MVP)

### Tasks

#### Task 4.1: Final Code Review
- Check code quality
- Ensure no hardcoded values
- Review for security issues
- Add docstrings where needed

#### Task 4.2: Build Distributions
```bash
python setup.py sdist  # Source distribution
python setup.py bdist_wheel  # Wheel distribution
```

**Verify**:
- ✅ `dist/python-pt-br-0.1.0.tar.gz` exists
- ✅ `dist/python_pt_br-0.1.0-py3-none-any.whl` exists

#### Task 4.3: Test Installation
```bash
pip install dist/python_pt_br-0.1.0-py3-none-any.whl

# Test in a new environment
python -c "import pt_br; print('Success!')"
```

#### Task 4.4: Update Version & Tag
```bash
# Update version if needed
git tag -a v0.1.0 -m "Initial release"
git push origin v0.1.0
```

#### Task 4.5: Optional: Publish to PyPI

**Note**: Only do this if you want public release. For MVP, local testing is sufficient.

```bash
pip install twine
twine upload dist/*
```

---

### Phase 4 Validation

#### Package Installs Correctly
```bash
pip install python-pt-br
# Should install without errors
```

#### Package Works After Installation
```bash
python -c "import pt_br; print(pt_br.__version__)"
# Should print: 0.1.0
```

---

## Overall Timeline

| Phase | Duration | Focus |
|-------|----------|-------|
| **Phase 0** | 0.5 hours | Setup & infrastructure |
| **Phase 1** | 2-3 hours | Core translator |
| **Phase 2** | 2-3 hours | Testing |
| **Phase 3** | 1-2 hours | Examples & docs |
| **Phase 4** | 0.5-1 hour | Release prep |
| **Total** | **6-10 hours** | MVP complete |

---

## Milestones & Checkpoints

### Milestone 1: Translator Works (End of Phase 1)
- ✅ Translator can translate pt-BR → Python
- ✅ Import hook registers and works
- ✅ Basic test script runs

**Exit Criteria**:
```bash
python examples/hello_world.py  # Prints "Olá, Mundo!"
```

---

### Milestone 2: Comprehensive Testing (End of Phase 2)
- ✅ 90%+ code coverage
- ✅ All keywords tested
- ✅ All functions tested
- ✅ Integration tests pass

**Exit Criteria**:
```bash
pytest tests/ -v  # All pass
pytest tests/ --cov=pt_br  # 90%+ coverage
```

---

### Milestone 3: Documented & Exemplified (End of Phase 3)
- ✅ README is clear and helpful
- ✅ All example scripts work
- ✅ Getting Started guide is complete
- ✅ Full reference exists

**Exit Criteria**:
```bash
# All examples run without errors
for file in examples/*.py; do python "$file" || exit 1; done
```

---

### Milestone 4: Package Release Ready (End of Phase 4)
- ✅ Code is clean and reviewed
- ✅ Package builds without errors
- ✅ Installation works correctly
- ✅ Can be distributed

**Exit Criteria**:
```bash
pip install python-pt-br  # Works
python -c "import pt_br"  # Works
```

---

## Dependency Map

```
Phase 0: Setup
    ↓
Phase 1: Translator (depends on Phase 0)
    ↓
Phase 2: Testing (depends on Phase 1)
    ↓
Phase 3: Examples & Docs (depends on Phase 1, 2)
    ↓
Phase 4: Release (depends on all phases)
```

**Key**: Phases can overlap slightly (e.g., start Phase 2 while finishing Phase 1), but Phase 1 must be complete before Phase 4.

---

## Rollback Plan

If issues arise at any phase:

### Phase 1 Issues
- Revert translator changes
- Go back to mappings and fix issues
- Re-test before proceeding

### Phase 2 Issues
- Fix translator based on test failures
- Add more comprehensive tests
- Don't proceed to Phase 3 until tests pass

### Phase 3 Issues
- Update documentation
- Fix example scripts
- Don't release until docs/examples are correct

### Phase 4 Issues
- Don't publish to PyPI
- Fix issues and rebuild distributions
- Re-test installation

---

## Success Criteria Summary

By end of MVP implementation:

1. ✅ 16/16 keywords working
2. ✅ 10/10 core functions working
3. ✅ 90%+ code coverage
4. ✅ 5+ working example scripts
5. ✅ Complete documentation
6. ✅ Package installable and working
7. ✅ All tests passing

---

**Next**: Begin Phase 0 setup, then proceed to Phase 1 implementation!
