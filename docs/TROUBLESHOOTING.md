# Troubleshooting Guide for python-pt-br

This guide helps you resolve common issues when using python-pt-br.

## Running Your Programs

### Issue: `SyntaxError: invalid syntax` when running with `python script.py`

**Cause:** Python doesn't know how to translate pt-BR syntax without the import hook.

**Solution:** Use one of these methods:

```bash
# Method 1: Use the runner (RECOMMENDED)
python -m pt_br seu_script.py

# Method 2: Add import at the top of your script
# Add this as the FIRST line:
import pt_br

# Then run normally:
python seu_script.py
```

**Example:**
```python
import pt_br  # ← MUST be first!

funcao ola():
    imprimir("Olá!")

ola()
```

### Issue: `ModuleNotFoundError: No module named 'pt_br'`

**Cause:** The python-pt-br package is not installed.

**Solution:** Install it using pip:

```bash
pip install python-pt-br
```

**Verify installation:**
```bash
python -c "import pt_br; print('Installation successful!')"
```

### Issue: The `pt-br` wrapper script doesn't work

**Cause:** The script doesn't exist or isn't executable.

**Solution:**

1. Check if file exists:
```bash
ls -la pt-br
```

2. Make it executable:
```bash
chmod +x pt-br
```

3. Try running it:
```bash
./pt-br seu_script.py
```

**On Windows:** The wrapper script doesn't work. Use `python -m pt_br` instead.

---

## Functions Not Recognized

### Issue: `NameError: name 'soma' is not defined`

**Cause:** The pt-BR function mappings aren't loaded.

**Solution:** Add `import pt_br` at the top of your script:

```python
import pt_br  # ← Add this first!

resultado = soma([1, 2, 3])
imprimir(resultado)
```

**Wrong:**
```python
resultado = soma([1, 2, 3])  # ← This fails, pt_br not imported
import pt_br
```

**Right:**
```python
import pt_br  # ← Must be first!

resultado = soma([1, 2, 3])  # ← Now this works
```

### Issue: Built-in functions like `len()` or `print()` don't work

**Cause:** These are English names; use Portuguese equivalents.

**Solution:** Use the Portuguese names instead:

```python
import pt_br

# Wrong:
print("Olá")  # This works but is English
len([1, 2, 3])  # This works but is English

# Right:
imprimir("Olá")  # Use Portuguese name
comprimento([1, 2, 3])  # Use Portuguese name
```

**All translations:**
- `print()` → `imprimir()`
- `len()` → `comprimento()`
- `range()` → `intervalo()`
- `input()` → `entrada()`
- `int()` → `inteiro()`
- `float()` → `flutuante()`
- `str()` → `texto()`
- `sum()` → `soma()`
- `min()` → `minimo()`
- `max()` → `maximo()`
- `sorted()` → `ordenado()`

---

## Keywords Not Working

### Issue: `NameError` when using keywords like `para`, `se`, etc.

**Cause:** The pt-BR keywords aren't being translated because `import pt_br` is missing.

**Solution:** Add `import pt_br` at the very beginning:

```python
import pt_br  # ← MUST be first line!

para i em intervalo(5):
    imprimir(i)
```

### Issue: Unexpected indentation or syntax errors in conditionals

**Cause:** Missing colon (`:`) at end of `se`, `senao`, `para`, etc.

**Solution:** Add `:` after all block statements:

```python
import pt_br

# Wrong:
se x > 0
    imprimir("Positivo")

# Right:
se x > 0:
    imprimir("Positivo")
```

### Issue: `SyntaxError` with nested blocks

**Cause:** Incorrect indentation in nested structures.

**Solution:** Use consistent indentation (usually 4 spaces):

```python
import pt_br

# Wrong:
funcao verificar(x):
se x > 0:
imprimir("Positivo")

# Right:
funcao verificar(x):
    se x > 0:
        imprimir("Positivo")
```

---

## Common Logic Errors

### Issue: Loop doesn't execute

**Cause:** Loop condition is false from the start.

**Solution:** Check your condition:

```python
import pt_br

# Wrong - loop never runs
para i em intervalo(0):
    imprimir(i)

# Right - loop runs 5 times
para i em intervalo(5):
    imprimir(i)

# Wrong - while is false
enquanto falso:
    imprimir("Never prints")

# Right
enquanto verdadeiro:
    imprimir("Runs forever!")
    quebra  # Add break to exit
```

### Issue: Infinite loop

**Cause:** Loop condition never becomes false.

**Solution:** Make sure to update the loop variable:

```python
import pt_br

# Wrong - infinite loop!
contador = 0
enquanto contador < 10:
    imprimir(contador)
    # ← contador never changes!

# Right
contador = 0
enquanto contador < 10:
    imprimir(contador)
    contador = contador + 1  # ← Now it increments
```

### Issue: Function returns `None` / `nulo`

**Cause:** Missing `retorna` statement.

**Solution:** Add explicit return:

```python
import pt_br

# Wrong - returns nulo implicitly
funcao somar(a, b):
    resultado = a + b  # ← Missing return

# Right
funcao somar(a, b):
    resultado = a + b
    retorna resultado  # ← Explicit return

# Or shorter
funcao somar(a, b):
    retorna a + b
```

---

## String and Output Issues

### Issue: Portuguese characters not displaying correctly

**Cause:** Encoding issue (rare on modern systems).

**Solution:** Add encoding declaration at the top:

```python
# -*- coding: utf-8 -*-
import pt_br

imprimir("São Paulo")
imprimir("Programação")
```

### Issue: Extra spaces in output

**Cause:** `imprimir()` adds space between multiple arguments.

**Solution:** Use string concatenation or formatting:

```python
import pt_br

# Adds spaces between arguments
imprimir("Olá", "Mundo")  # Output: "Olá Mundo"

# No spaces - use concatenation
imprimir("Olá" + "Mundo")  # Output: "OláMundo"

# Formatted (recommended)
nome = "Maria"
imprimir(f"Olá, {nome}!")  # Output: "Olá, Maria!"
```

### Issue: newlines in strings

**Cause:** Need to add newlines explicitly.

**Solution:** Use `\n` or call `imprimir()` multiple times:

```python
import pt_br

# With newlines
imprimir("Linha 1\nLinha 2")

# Multiple calls
imprimir("Linha 1")
imprimir("Linha 2")

# Both produce the same output:
# Linha 1
# Linha 2
```

---

## Type Conversion Issues

### Issue: `ValueError: invalid literal for int()`

**Cause:** Trying to convert non-numeric string to integer.

**Solution:** Validate input before conversion:

```python
import pt_br

# Wrong - crashes if user enters "abc"
entrada_texto = entrada("Digite um número: ")
numero = inteiro(entrada_texto)

# Right - validate first
entrada_texto = entrada("Digite um número: ")
se entrada_texto.eh_digito():
    numero = inteiro(entrada_texto)
senao:
    imprimir("Por favor, digite um número válido")
    numero = 0
```

### Issue: List indexing with float

**Cause:** Can't use floats as list indices.

**Solution:** Convert to integer:

```python
import pt_br

lista = [10, 20, 30]

# Wrong
indice = flutuante("1.5")
valor = lista[indice]  # TypeError!

# Right
indice = inteiro(flutuante("1.5"))  # Converts to 1
valor = lista[indice]  # Works: 20
```

---

## List and Dictionary Issues

### Issue: `IndexError: list index out of range`

**Cause:** Accessing list index that doesn't exist.

**Solution:** Check list length first:

```python
import pt_br

lista = [1, 2, 3]

# Wrong - index 5 doesn't exist
valor = lista[5]  # IndexError!

# Right - check bounds
se 5 < comprimento(lista):
    valor = lista[5]
senao:
    imprimir("Índice fora dos limites")

# Or use safe access
se 0 <= indice < comprimento(lista):
    valor = lista[indice]
```

### Issue: `KeyError` with dictionaries

**Cause:** Accessing dictionary key that doesn't exist.

**Solution:** Check if key exists first:

```python
import pt_br

dicionario = {"nome": "João", "idade": 30}

# Wrong
email = dicionario["email"]  # KeyError!

# Right - check if key exists
se "email" em dicionario:
    email = dicionario["email"]
senao:
    email = "Não fornecido"
```

### Issue: Modifying list while looping

**Cause:** List size changes during iteration.

**Solution:** Loop over a copy or create new list:

```python
import pt_br

numeros = [1, 2, 3, 4, 5]

# Wrong - removes items while looping
para numero em numeros:
    se numero % 2 == 0:
        numeros.remover(numero)  # ← Dangerous!

# Right - loop over copy
para numero em lista(numeros):  # ← Creates copy
    se numero % 2 == 0:
        numeros.remover(numero)

# Or create new list
numeros_pares = [n para n em numeros se n % 2 == 0]
```

---

## IDE and Editor Issues

### Issue: IDE shows "undefined name" errors for pt-BR keywords

**Expected behavior** - This is normal and expected.

**Why:** IDEs don't know about the pt-BR translation at design time.

**Solution:** This doesn't prevent your code from running. You can:

1. Ignore the error warnings
2. Use a simpler editor (VS Code, Sublime, Vim)
3. Configure your IDE to run your code with `python -m pt_br`

### Issue: Syntax highlighting is wrong

**Expected behavior** - Keywords won't be highlighted in special colors.

**Why:** Your editor only knows English Python syntax.

**Solution:** This is a known limitation. The code still runs correctly.

### Issue: IDE can't find imported modules

**Cause:** IDE analysis happens before translation.

**Solution:** This is expected. Run your code to verify it works:

```bash
python -m pt_br seu_script.py
```

---

## Performance Issues

### Issue: Program runs slowly

**Cause:** Translation overhead is minimal; likely a logic issue.

**Solution:** Profile your code:

1. Check for inefficient loops
2. Avoid unnecessary list copies
3. Use built-in functions (they're optimized)

```python
import pt_br

# Slow - creates many lists
resultado = []
para i em intervalo(1000000):
    resultado.acrescentar(i)

# Fast - uses list comprehension
resultado = [i para i em intervalo(1000000)]
```

### Issue: Memory usage is high

**Cause:** Likely algorithm issue, not the translator.

**Solution:** Avoid creating large intermediate data structures:

```python
import pt_br

# Memory intensive
todas_as_linhas = []
arquivo = entrada("Nome do arquivo: ")
# Read all lines into memory

# Better - process one at a time
# (Requires file I/O, not covered in basic docs)
```

---

## Advanced Troubleshooting

### Issue: Tracebacks show English code

**Expected behavior** - Error messages show the translated Python code.

**Why:** Tracebacks are generated after translation.

**Solution:** Map back to your original pt-BR code manually, or use the error line numbers as hints.

### Issue: Mixing English and Portuguese code

**Cause:** Some code uses Python keywords, some uses pt-BR.

**Solution:** Be consistent - choose Portuguese or English and stick with it:

```python
import pt_br

# Mixed (confusing!)
para i in range(5):  # ← English!
    imprimir(i)

se condition:  # ← English!
    imprimir("okay")

# Consistent Portuguese
para i em intervalo(5):
    imprimir(i)

se condicao:
    imprimir("okay")
```

### Issue: Module-level code doesn't execute

**Cause:** Import hook isn't active yet.

**Solution:** Put all code inside functions or `if __name__ == "__main__"`:

```python
import pt_br

# This might not work:
imprimir("Executa?")

# This works:
funcao main():
    imprimir("Executa!")

main()

# Or this:
se __name__ == "__main__":
    imprimir("Executa!")
```

---

## Getting More Help

1. **Check the examples:** Look at `/examples/` for working code
2. **Read FULL_GUIDE.md:** Detailed reference of all keywords and functions
3. **Read GETTING_STARTED.md:** Basic concepts and patterns
4. **Run simple test:** Create minimal example to isolate problem
5. **Check syntax:** Verify colons, indentation, and brackets match
6. **Check import:** Verify `import pt_br` is the first line

## Common Mistakes Summary

| Mistake | Fix |
|---------|-----|
| `import pt_br` not first line | Move to top of file |
| Using English keywords | Use Portuguese equivalents |
| Missing colon after `se`, `para`, etc | Add `:` at end of line |
| Wrong indentation | Use 4 spaces consistently |
| Infinite loop | Make sure loop variable updates |
| Accessing invalid index | Check list length first |
| KeyError in dict | Check if key exists first |
| IDE warnings about undefined names | Normal; run to verify it works |
| SyntaxError with `python script.py` | Use `python -m pt_br script.py` |

Still having issues? Check that:
- ✅ You're using correct syntax (colons, indentation)
- ✅ `import pt_br` is the first line (if not using `python -m pt_br`)
- ✅ You're using Portuguese names not English equivalents
- ✅ Package is installed: `pip install python-pt-br`
- ✅ Python version is 3.8 or higher: `python --version`
