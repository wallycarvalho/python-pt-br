# MVP Scope & Requirements

## What is the MVP?

The Minimum Viable Product is the smallest, most focused version that demonstrates the core concept and delivers real value. For python-pt-br, it's a functional package that allows users to write simple Python scripts using pt-BR keywords.

---

## MVP Goals

1. **Prove the concept works**: Users can import pt_br and write pt-BR Python code
2. **Enable basic programs**: Support common programming patterns (loops, conditionals, functions)
3. **Minimize friction**: One import line, then write normal `.py` files
4. **Build foundation**: Create clean architecture for future expansion
5. **Educational focus**: Target learners, make it easy to understand and use

---

## MVP Success Criteria

### Functional Requirements

#### Core Feature 1: Keyword Translation
- ✅ Translate all control flow keywords (`para`, `em`, `se`, `senao`, `enquanto`)
- ✅ Translate all logical operators (`e`, `ou`, `nao`)
- ✅ Translate boolean/null values (`verdadeiro`, `falso`, `nulo`)
- ✅ Translate flow control (`quebra`, `continua`, `retorna`)
- ✅ Translate function definition (`def` or `funcao`)
- ✅ Translate class definition (`classe`)

**Test**: Write a script using all these keywords, execute it, verify output

---

#### Core Feature 2: Built-in Function Translation
- ✅ `imprimir()` → `print()`
- ✅ `intervalo()` → `range()`
- ✅ `entrada()` → `input()`
- ✅ `comprimento()` → `len()`
- ✅ `lista()` → `list()`
- ✅ `inteiro()` → `int()`
- ✅ `texto()` → `str()`
- ✅ `soma()` → `sum()`
- ✅ `minimo()` → `min()`
- ✅ `maximo()` → `max()`

**Test**: Write functions using all these built-ins, execute them, verify behavior

---

#### Core Feature 3: Import Hook Integration
- ✅ `import pt_br` registers translation hook
- ✅ Files can be executed with `python script.py`
- ✅ Translation happens transparently (user doesn't see it)
- ✅ Translation errors are reported clearly

**Test**: Write example scripts, execute them normally, verify they work

---

#### Core Feature 4: Error Handling
- ✅ Syntax errors in pt-BR code: Report useful error messages
- ✅ Runtime errors: Standard Python traceback (acceptable to show Python code)
- ✅ Import errors: Clear message if translation fails

**Test**: Intentionally break scripts in various ways, verify error messages

---

### Non-Functional Requirements

#### Code Quality
- ✅ Clean, readable code (educational value)
- ✅ Well-commented, especially translation logic
- ✅ No external dependencies (pure Python)
- ✅ Python 3.8+ compatible

#### Testing
- ✅ 90%+ code coverage
- ✅ Unit tests for each keyword/function
- ✅ Integration tests with example scripts
- ✅ Edge case tests (strings, comments, etc.)

#### Documentation
- ✅ README with quick start
- ✅ Installation instructions
- ✅ Example scripts for each feature
- ✅ Getting started guide
- ✅ Full API reference

#### Package Distribution
- ✅ Publishable to PyPI
- ✅ `setup.py` configured correctly
- ✅ Version numbering: `0.1.0`
- ✅ LICENSE file (MIT)

---

## In-Scope vs Out-of-Scope

### In-Scope (MVP)

| Feature | Why Included |
|---------|------------|
| **Core keywords** | Essential for any program |
| **Basic built-ins** | Enable common operations (print, loops, input) |
| **Simple translation** | Regex-based, good enough for MVP |
| **`.py` file execution** | Main use case (zero friction) |
| **Error messages** | Help users debug |
| **Test coverage** | Ensure reliability |
| **Documentation** | Help users get started |

### Out-of-Scope (MVP+)

| Feature | Why Deferred |
|---------|------------|
| **Module/package translations** | Complex, can defer |
| **`async`/`await`** | Advanced feature, educational gap |
| **Context managers (`com`)** | Advanced, less common |
| **Decorators (`@`)** | Advanced, can defer |
| **IDE/linter support** | External tool integration, future |
| **REPL support** | Interactive mode is complex |
| **Other languages** | pt-BR first, then expand |
| **100% AST parsing** | Regex sufficient for MVP, AST can improve accuracy later |
| **Pre-compiled `.pyc` files** | Not necessary for MVP |
| **Performance optimization** | Translation is fast enough |

---

## Translation Coverage Goals

### Completeness Metrics

| Category | Target | MVP Goal |
|----------|--------|----------|
| **Keywords** | 16 total | All 16 (100%) |
| **Built-in functions** | 30+ total | 10 core (33%) |
| **Edge cases** | Perfect handling | 90% accuracy |

**Rationale**: 16 keywords + 10 core functions cover ~95% of educational Python programs

---

## Example Programs That Should Work

### Example 1: Basic Loop
```python
import pt_br

para i em intervalo(5):
    imprimir(i)
```

**Expected Output**: 0, 1, 2, 3, 4

---

### Example 2: Conditional
```python
import pt_br

idade = 18

se idade >= 18:
    imprimir("Adulto")
senao:
    imprimir("Menor")
```

**Expected Output**: "Adulto"

---

### Example 3: Function Definition
```python
import pt_br

def dobro(x):
    retorna x * 2

resultado = dobro(5)
imprimir(resultado)
```

**Expected Output**: 10

---

### Example 4: Data Structures
```python
import pt_br

numeros = [1, 2, 3, 4, 5]
imprimir(soma(numeros))
imprimir(minimo(numeros))
imprimir(maximo(numeros))
```

**Expected Output**: 15, 1, 5

---

### Example 5: User Input
```python
import pt_br

nome = entrada("Qual é o seu nome? ")
imprimir(f"Olá, {nome}!")
```

**Expected Output**: Prompts for input, then greets user

---

## Assumptions

### Technical Assumptions
1. **Python version**: Users have Python 3.8+
2. **File encoding**: Files are UTF-8 encoded (handles pt-BR characters)
3. **Standard library**: All examples use only built-in functions/modules (no external packages)
4. **Import order**: `import pt_br` must come before pt-BR code (documented limitation)

### User Assumptions
1. **Target audience**: Beginners/students learning Python
2. **Use case**: Educational projects, not production code
3. **Environment**: Local development (not cloud, embedded systems, etc.)
4. **Comfort level**: Users know basic Python syntax concepts

### Project Assumptions
1. **Scope**: pt-BR only for MVP (no other languages yet)
2. **Error handling**: Translation failures are acceptable (show Python traceback)
3. **Performance**: Translation speed is acceptable (sub-second for typical files)
4. **Testing**: Can be tested on macOS, Linux, Windows (standard CI)

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **Translation misses keywords in strings** | Incorrect behavior | Simple regex + comment detection, accept 90% accuracy for MVP |
| **Import hook conflicts** | Breaking other packages | Document import order, add warning, test with common packages |
| **Python version compatibility** | Doesn't work for users | Test on 3.8, 3.9, 3.10, 3.11, 3.12; document minimum version |
| **Users expect full Python compat** | Disappointment | Clear documentation of what's supported, manage expectations |
| **IDE/linter doesn't recognize pt-BR** | Bad DX | Document limitation, acknowledge in README |
| **Performance too slow** | Unusable for large files | Test with large files, optimize if needed (regex is fast) |

---

## Validation Plan

### How We'll Verify MVP Success

#### Phase 1: Unit Tests
- Run test suite: `pytest tests/`
- Target: 90%+ code coverage
- All keywords and functions have tests

#### Phase 2: Integration Tests
- Run all example scripts: `python examples/*.py`
- Verify correct output
- Test with different Python versions (3.8+)

#### Phase 3: Manual Validation
- Write a complete program in pt-BR (e.g., number guessing game)
- Execute it: `python game.py`
- Verify it works as expected

#### Phase 4: Package Distribution
- Create source distribution: `python setup.py sdist`
- Create wheel: `python setup.py bdist_wheel`
- Test installation: `pip install <generated package>`
- Verify it works after installation

---

## Success Metrics

### Quantitative
- ✅ 16/16 keywords working
- ✅ 10/10 core functions working
- ✅ 100% of example scripts run correctly
- ✅ 90%+ code coverage
- ✅ <10ms translation time per file

### Qualitative
- ✅ Users can write simple pt-BR programs without frustration
- ✅ Documentation is clear and accessible
- ✅ Error messages are helpful
- ✅ Code is clean and understandable

---

## Definition of Done

MVP is complete when:

1. ✅ All 16 keywords translate correctly
2. ✅ All 10 core functions translate correctly
3. ✅ At least 5 example scripts run without errors
4. ✅ 90%+ code coverage
5. ✅ Full documentation (README, Getting Started, API Reference)
6. ✅ Package is installable via pip
7. ✅ All unit and integration tests pass
8. ✅ Code is reviewed and clean

---

## Timeline Estimate

This is for planning purposes; actual speed may vary.

| Phase | Duration | Deliverable |
|-------|----------|------------|
| **Setup** | 0.5 hours | Project structure, setup.py, git init |
| **Core translator** | 2-3 hours | translator.py, mappings.py, basic import hook |
| **Testing** | 2-3 hours | test suite, 90%+ coverage |
| **Documentation** | 1-2 hours | README, examples, Getting Started |
| **Polish & release** | 0.5-1 hour | Final cleanup, version bump, PyPI prep |
| **Total** | **6-10 hours** | **Functional MVP** |

---

## Summary

The MVP is a **focused, working implementation** that:
- Translates 16 keywords + 10 core functions
- Allows users to write simple pt-BR Python scripts
- Has solid documentation and examples
- Is publishable to PyPI
- Provides foundation for future expansion

**Key principle**: Better to do one thing (keyword/function translation) well than many things poorly.

---

**Next Steps**: See `05-IMPLEMENTATION_PLAN.md` for the step-by-step implementation roadmap
