# Phase 4.3: Build & Local Testing Guide

This guide walks you through building the wheel locally and testing it before uploading to PyPI.

## Prerequisites

Make sure you have the following installed:
```bash
pip install build twine pytest pytest-cov
```

Or install from requirements.txt:
```bash
pip install -r requirements.txt
```

## Step 1: Clean Previous Builds (Optional but Recommended)

Remove any previous build artifacts:
```bash
rm -rf build dist *.egg-info
```

## Step 2: Build the Wheel

Create the wheel distribution:
```bash
python -m build
```

This should create:
- `dist/python_pt_br-0.1.0-py3-none-any.whl` (wheel - optimized)
- `dist/python_pt_br-0.1.0.tar.gz` (source distribution)

**Expected output:**
```
Successfully built python-pt-br
```

## Step 3: Verify Build Artifacts

Check that the files were created:
```bash
ls -lh dist/
```

You should see:
- `python_pt_br-0.1.0-py3-none-any.whl` (~50-100 KB)
- `python_pt_br-0.1.0.tar.gz` (~50-100 KB)

## Step 4: Test Wheel Installation Locally

Install the wheel in a fresh environment:

### Option A: Install in current environment (simple)
```bash
pip install dist/python_pt_br-0.1.0-py3-none-any.whl
```

### Option B: Use a virtual environment (recommended for clean test)
```bash
# Create a test venv
python -m venv test_env

# Activate it
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install the wheel
pip install dist/python_pt_br-0.1.0-py3-none-any.whl

# Verify installation
python -c "import pt_br; print(f'Version: {pt_br.__version__}')"
# Should output: Version: 0.1.0

# Deactivate when done
deactivate
```

## Step 5: Run Test Suite Against Installed Package

With the wheel installed, run the test suite:

```bash
pytest tests/ -v --cov=pt_br
```

**Expected output:**
- All 181 tests pass
- Coverage report shows 69% coverage
- No import errors

### What each test suite checks:

1. **test_translator.py** (73 tests)
   - Translation accuracy for all keywords
   - Translation accuracy for all functions
   - Edge cases and special handling

2. **test_utils.py** (46 tests)
   - String/comment detection
   - Safe replacement logic
   - Edge cases in utility functions

3. **test_coverage.py** (43 tests)
   - Validates all mappings are working
   - Verifies no translations are missing

4. **test_integration.py** (19 tests)
   - Real-world usage scenarios
   - Module imports
   - Complex code patterns

## Step 6: Test Example Scripts

Test that example scripts work with the installed package:

```bash
# From repository root, run examples
python -m pt_br examples/hello_world.py
python -m pt_br examples/loops.py
python -m pt_br examples/conditionals.py
python -m pt_br examples/functions.py
python -m pt_br examples/data_structures.py
```

**Expected behavior:**
- Each script runs without errors
- Output displays correctly
- No import errors

### Example output expectations:

**hello_world.py:**
```
Olá, Mundo!
Bem-vindo ao python-pt-br!
Este é um programa em Python com palavras-chave em português!
2 + 2 = 4
Linguagem: Python
```

**loops.py:**
```
=== FOR LOOPS (para e intervalo) ===
Contando de 0 a 4:
Número: 0
Número: 1
...
```

## Step 7: Verify Package Metadata

Check that package information is correct:

```bash
pip show python-pt-br
```

**Expected output includes:**
- Name: python-pt-br
- Version: 0.1.0
- Author: Wally Carvalho
- Summary: Write Python code in Brazilian Portuguese (pt-BR)

## Step 8: Test Import and Access Public API

Verify the public API is accessible:

```python
python -c "
from pt_br import (
    translate_source,
    PT_BR_TO_PYTHON,
    PT_BR_KEYWORDS,
    PT_BR_BUILTINS,
    PYTHON_TO_PT_BR,
    debug_show_translation,
    __version__,
    __author__,
)
print(f'python-pt-br v{__version__}')
print(f'Author: {__author__}')
print(f'Keywords: {len(PT_BR_KEYWORDS)}')
print(f'Functions: {len(PT_BR_BUILTINS)}')
print('✅ All public APIs accessible')
"
```

**Expected output:**
```
python-pt-br v0.1.0
Author: Wally Carvalho
Keywords: 16
Functions: 17
✅ All public APIs accessible
```

## Step 9: Verify Wheel Contents (Optional)

Inspect what's inside the wheel:

```bash
unzip -l dist/python_pt_br-0.1.0-py3-none-any.whl
```

You should see:
- `pt_br/` directory with all modules
- `dist-info/` metadata directory
- `METADATA` file with correct version and author

## Step 10: Test Uninstallation and Reinstallation

Ensure clean uninstall and reinstall works:

```bash
# Uninstall
pip uninstall python-pt-br -y

# Verify it's gone
pip show python-pt-br  # Should say not found

# Reinstall from wheel
pip install dist/python_pt_br-0.1.0-py3-none-any.whl

# Verify again
pip show python-pt-br  # Should show v0.1.0
```

## Troubleshooting

### Build fails with "No module named setuptools"
```bash
pip install --upgrade setuptools wheel
python -m build
```

### Tests fail after installation
```bash
# Make sure pytest is installed
pip install pytest pytest-cov

# Run from repo root where tests/ directory is
cd /path/to/python-pt-br
pytest tests/ -v
```

### Wheel installation fails
```bash
# Check if there's a conflicting version installed
pip uninstall python-pt-br -y

# Try installing wheel again
pip install dist/python_pt_br-0.1.0-py3-none-any.whl
```

### Example scripts fail with "No module named pt_br"
```bash
# Make sure package is installed
pip install -e .  # or from the wheel

# Then try again
python -m pt_br examples/hello_world.py
```

## Validation Checklist

Before proceeding to Phase 4.4 (PyPI Upload), verify:

- ✅ Wheel builds successfully with no errors
- ✅ Wheel file exists and has reasonable size (>30KB)
- ✅ Installation from wheel succeeds
- ✅ `import pt_br` works after installation
- ✅ All 181 tests pass
- ✅ Test coverage shows 69%
- ✅ All 5 example scripts run successfully
- ✅ Package metadata is correct (`pip show python-pt-br`)
- ✅ Public API is accessible
- ✅ Clean uninstall/reinstall works

## Next Steps

Once all checks pass, you're ready for Phase 4.4 (PyPI Upload):

1. Upload to test.pypi.org first (practice run)
2. Verify installation from test PyPI works
3. Then upload to production PyPI
4. Announce the release on social media

## Commands Reference

```bash
# Build
python -m build

# Test installation
pip install dist/python_pt_br-0.1.0-py3-none-any.whl

# Run all tests
pytest tests/ -v --cov=pt_br

# Test examples
python -m pt_br examples/hello_world.py

# Verify metadata
pip show python-pt-br

# Uninstall
pip uninstall python-pt-br -y

# Upload to test PyPI (Phase 4.4)
twine upload --repository testpypi dist/*

# Upload to production PyPI (Phase 4.4)
twine upload dist/*
```
