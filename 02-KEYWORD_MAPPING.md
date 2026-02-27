# Keyword Mapping & Translation Dictionary

## Overview

This document defines all pt-BR keywords and built-in functions that will be translated to Python equivalents in the MVP phase.

## Philosophy

- **Conservative Start**: Include only the most common, unambiguous keywords
- **Extensible Design**: Easy to add more translations later
- **Bidirectional Reference**: Show pt-BR ↔ Python pairs clearly
- **Context Notes**: Explain any special handling needed

---

## Part 1: Language Keywords

These are Python reserved keywords that control program flow. They **must** be translated exactly.

### Control Flow

| pt-BR | Python | Context | Notes |
|-------|--------|---------|-------|
| `para` | `for` | Loop declaration | `para item em lista:` |
| `em` | `in` | Membership/loop containment | Used with `para` |
| `enquanto` | `while` | Conditional loop | `enquanto condicao:` |
| `se` | `if` | Conditional | `se condicao:` |
| `senao` | `else` | Alternative condition | `else:` blocks |
| `senao_se` / `sen_se` | `elif` | Chained condition | Multiple conditions |
| `quebra` | `break` | Exit loop | Inside `para` or `enquanto` |
| `continua` | `continue` | Skip to next iteration | Inside loops |

### Boolean & Logic

| pt-BR | Python | Context | Notes |
|-------|--------|---------|-------|
| `e` | `and` | Logical AND | Condition combining |
| `ou` | `or` | Logical OR | Condition combining |
| `nao` | `not` | Logical NOT | Negation |
| `verdadeiro` | `True` | Boolean true | Literal value |
| `falso` | `False` | Boolean false | Literal value |
| `nulo` | `None` | Null value | Absence of value |

### Function & Class Definition

| pt-BR | Python | Context | Notes |
|-------|--------|---------|-------|
| `funcao` | `def` | Define function | Keep as-is (or use `funcao`?) |
| `classe` | `class` | Define class | Class definition |
| `retorna` | `return` | Return from function | Function exit |
| `rendimento` | `yield` | Generator yield | Advanced, maybe MVP+ |

### Exception Handling

| pt-BR | Python | Context | Notes |
|-------|--------|---------|-------|
| `tenta` | `try` | Try block | Exception handling |
| `exceto` | `except` | Catch exception | Handle specific errors |
| `finalmente` | `finally` | Finally block | Cleanup code |
| `levanta` | `raise` | Raise exception | Throw error |

### Imports & Modules

| pt-BR | Python | Context | Notes |
|-------|--------|---------|-------|
| `importa` | `import` | Import module | Module loading |
| `de` | `from` | Import from module | `de modulo importa funcao` |
| `como` | `as` | Alias import | `importa numpy como np` |

### Advanced (MVP+, consider for later)

| pt-BR | Python | Context | Notes |
|-------|--------|---------|-------|
| `com` | `with` | Context manager | File handling, advanced |
| `assincrone` | `async` | Async function | Advanced, skip for MVP |
| `aguarda` | `await` | Await async | Advanced, skip for MVP |
| `lambda` | `lambda` | Anonymous function | Maybe keep as-is? |
| `global` | `global` | Global scope | Variable scope |
| `nao_local` | `nonlocal` | Nonlocal scope | Variable scope |

---

## Part 2: Built-in Functions

These are Python built-in functions (not keywords). Users will call them as `funcao()`.

### I/O & Console

| pt-BR | Python | Example | Notes |
|-------|--------|---------|-------|
| `imprimir()` | `print()` | `imprimir("Olá")` | Most common, high priority |
| `entrada()` | `input()` | `entrada("Digite algo:")` | User input |

### Collections & Iteration

| pt-BR | Python | Example | Notes |
|-------|--------|---------|-------|
| `intervalo()` | `range()` | `intervalo(10)` | Generate number sequence |
| `lista()` | `list()` | `lista([1, 2, 3])` | Create list |
| `tupla()` | `tuple()` | `tupla([1, 2])` | Create tuple |
| `conjunto()` | `set()` | `conjunto([1, 1, 2])` | Create set |
| `dicionario()` | `dict()` | `dicionario(a=1)` | Create dict |
| `enumerar()` | `enumerate()` | `enumerar(lista)` | Index + item |
| `compacta()` | `zip()` | `compacta(lista1, lista2)` | Combine iterables |
| `comprimento()` | `len()` | `comprimento(lista)` | Get length |

### Type Conversion

| pt-BR | Python | Example | Notes |
|-------|--------|---------|-------|
| `inteiro()` | `int()` | `inteiro("42")` | Convert to integer |
| `flutuante()` | `float()` | `flutuante("3.14")` | Convert to float |
| `texto()` | `str()` | `texto(42)` | Convert to string |
| `booleano()` | `bool()` | `booleano(1)` | Convert to boolean |

### Aggregation & Sorting

| pt-BR | Python | Example | Notes |
|-------|--------|---------|-------|
| `soma()` | `sum()` | `soma([1, 2, 3])` | Sum numbers |
| `minimo()` | `min()` | `minimo([3, 1, 2])` | Minimum value |
| `maximo()` | `max()` | `maximo([3, 1, 2])` | Maximum value |
| `classifica()` | `sorted()` | `classifica(lista)` | Sort iterable |

### Utilities

| pt-BR | Python | Example | Notes |
|-------|--------|---------|-------|
| `tipo()` | `type()` | `tipo(42)` | Get object type |
| `eh_instancia()` | `isinstance()` | `eh_instancia(x, int)` | Type checking |
| `mapa()` | `map()` | `mapa(funcao, lista)` | Apply function to items |
| `filtro()` | `filter()` | `filtro(funcao, lista)` | Filter items |

### Advanced (MVP+, consider for later)

| pt-BR | Python | Example | Notes |
|-------|--------|---------|-------|
| `intervalo_aberto()` | `range()` with step | For MVP, use single `intervalo()` | |
| `reduz()` | `reduce()` | From `functools` | Import needed, complex |
| `todos()` | `all()` | `todos(condicoes)` | All true? |
| `qualquer()` | `any()` | `qualquer(condicoes)` | Any true? |
| `indice()` | `.index()` | Method, not function | Handle separately |

---

## Part 3: Operators (Considered for Translation)

Python operators are symbols, not keywords. We might keep them as-is for clarity.

| Operator | pt-BR (optional) | Keep as-is? | Reason |
|----------|------------------|------------|--------|
| `+` | `mais` | **Yes** | Keep operators as symbols—clearer mathematically |
| `-` | `menos` | **Yes** | Universal mathematical notation |
| `*` | `vezes` | **Yes** | Symbols are language-agnostic |
| `/` | `dividido` | **Yes** | Symbols are language-agnostic |
| `==` | `igual_a` | **Yes** | Symbols are clearer |
| `!=` | `diferente_de` | **Yes** | Symbols are clearer |
| `<` | `menor_que` | **Yes** | Symbols are clearer |
| `>` | `maior_que` | **Yes** | Symbols are clearer |

**Decision**: Keep operators as symbols. They're mathematical and universal.

---

## Part 4: Translation Implementation Strategy

### Regex Patterns (Simple Approach for MVP)

The translator will use regex patterns to identify and replace keywords. Challenge: don't replace inside strings or comments.

#### Example Patterns (pseudo-code)

```
# Simple keyword replacement (avoid strings)
Pattern: \b(para|em|enquanto|se|senao|e|ou|nao)\b(?!["\'])
Replace: [corresponding Python keyword]

# Built-in function replacement
Pattern: \b(imprimir|intervalo|entrada)\(
Replace: [corresponding Python function](
```

### Context Sensitivity (MVP)

For MVP, we'll handle these contexts:
1. ✅ Standalone keywords: `para`, `enquanto`, `se`, etc.
2. ✅ Function calls: `imprimir()`, `intervalo()`, etc.
3. ⚠️ Inside strings/comments: Skip (simple detection)
4. ❌ Complex cases: AST parsing (post-MVP)

### Edge Cases to Watch

| Case | Example | Handling |
|------|---------|----------|
| Inside strings | `texto = "imprimir olá"` | Don't translate (string detection) |
| Inside comments | `# imprimir deve fazer algo` | Don't translate (comment detection) |
| Variable names | `meu_para = 5` | Don't translate (word boundary check) |
| Combined keywords | `se x > 0 e y < 10:` | Translate all keywords |

---

## Part 5: Phased Rollout

### MVP Phase 1: Core Keywords + Common Functions

**High Priority** (must-have):
- Keywords: `para`, `em`, `se`, `senao`, `enquanto`, `e`, `ou`, `nao`
- Functions: `imprimir()`, `intervalo()`, `entrada()`, `comprimento()`
- Booleans: `verdadeiro`, `falso`, `nulo`

**Medium Priority** (should-have):
- Keywords: `quebra`, `continua`, `retorna`, `funcao`, `classe`
- Functions: `lista()`, `inteiro()`, `texto()`, `soma()`, `minimo()`, `maximo()`

### MVP Phase 2: Extended Coverage

- All remaining keywords except `async`/`await`/`with`
- All basic type conversions
- Common iteration utilities

### MVP+: Advanced Features

- `async`/`await` for advanced users
- Context managers (`com`)
- Generator expressions

---

## Part 6: Testing the Translations

Once implemented, we'll test each translation:

```python
# Test example for imprimir()
# Input:
imprimir("Olá, Mundo!")

# Should translate to:
print("Olá, Mundo!")

# And execute correctly, printing: Olá, Mundo!
```

For each keyword/function, we need at least one test case.

---

## Summary: MVP Translation List

### Keywords to Translate (MVP):
- `para` → `for`
- `em` → `in`
- `se` → `if`
- `senao` → `else`
- `enquanto` → `while`
- `e` → `and`
- `ou` → `or`
- `nao` → `not`
- `verdadeiro` → `True`
- `falso` → `False`
- `nulo` → `None`
- `quebra` → `break`
- `continua` → `continue`
- `retorna` → `return`
- `funcao` → `def`
- `classe` → `class`

### Functions to Translate (MVP):
- `imprimir()` → `print()`
- `intervalo()` → `range()`
- `entrada()` → `input()`
- `comprimento()` → `len()`
- `lista()` → `list()`
- `inteiro()` → `int()`
- `texto()` → `str()`
- `soma()` → `sum()`
- `minimo()` → `min()`
- `maximo()` → `max()`

**Total MVP**: ~25 translations (16 keywords + ~10 functions)

---

**Next Steps**: See `03-PROJECT_STRUCTURE.md` for how to organize the code
