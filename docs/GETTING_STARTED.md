# Getting Started with python-pt-br

Welcome! This guide will help you start writing Python code using Portuguese Brazilian (pt-BR) keywords and function names.

## Installation

The simplest way to get started is to install python-pt-br from PyPI:

```bash
pip install python-pt-br
```

## Your First Program

### Create `hello.py`:

```python
import pt_br

imprimir("Olá, Mundo!")
imprimir("Bem-vindo ao python-pt-br!")
```

### Run it:

```bash
python -m pt_br hello.py
```

**Output:**
```
Olá, Mundo!
Bem-vindo ao python-pt-br!
```

That's it! You've just run your first program in Portuguese!

## How It Works

When you `import pt_br`, Python installs an import hook that:
1. Intercepts Python file imports
2. Translates Portuguese keywords and functions to English equivalents
3. Executes the translated code normally

This means **everything still runs as standard Python** - we just use Portuguese syntax!

## Common Patterns

### Printing Output

```python
import pt_br

nome = "Maria"
imprimir(f"Olá, {nome}!")  # imprimir = print
```

### Variables and Simple Math

```python
import pt_br

x = 10
y = 20
resultado = x + y
imprimir(resultado)
```

### Loops

```python
import pt_br

# For loop using 'para' and 'intervalo'
para i em intervalo(5):
    imprimir(f"Iteração {i}")

# While loop
contador = 0
enquanto contador < 3:
    imprimir(contador)
    contador = contador + 1
```

### Conditionals

```python
import pt_br

idade = 18

se idade >= 18:
    imprimir("Você é maior de idade")
senao:
    imprimir("Você é menor de idade")
```

### Functions

```python
import pt_br

funcao saudar(nome):
    imprimir(f"Olá, {nome}!")

funcao somar(a, b):
    retorna a + b

saudar("João")
resultado = somar(5, 3)
imprimir(resultado)  # outputs: 8
```

### Working with Lists

```python
import pt_br

frutas = ["maçã", "banana", "laranja"]

# Add item
frutas.acrescentar("morango")

# Loop through
para fruta em frutas:
    imprimir(fruta)

# Check length
imprimir(comprimento(frutas))  # comprimento = len
```

### Working with Dictionaries

```python
import pt_br

pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}

imprimir(pessoa["nome"])

# Loop through keys
para chave em pessoa:
    imprimir(f"{chave}: {pessoa[chave]}")
```

## All Supported Keywords

| Portuguese | English | Usage |
|------------|---------|-------|
| `funcao` | def | Define a function |
| `classe` | class | Define a class |
| `para` | for | Loop over items |
| `em` | in | Check membership / loop |
| `enquanto` | while | Conditional loop |
| `se` | if | Conditional branch |
| `senao_se` | elif | Additional condition |
| `senao` | else | Default branch |
| `retorna` | return | Return from function |
| `quebra` | break | Exit loop |
| `continua` | continue | Skip to next iteration |
| `e` | and | Logical AND |
| `ou` | or | Logical OR |
| `nao` | not | Logical NOT |
| `verdadeiro` | True | Boolean true |
| `falso` | False | Boolean false |
| `nulo` | None | Null value |

## All Supported Built-in Functions

| Portuguese | English | Purpose |
|------------|---------|---------|
| `imprimir()` | print() | Print to output |
| `entrada()` | input() | Read user input |
| `intervalo()` | range() | Generate sequence |
| `comprimento()` | len() | Get length |
| `inteiro()` | int() | Convert to integer |
| `flutuante()` | float() | Convert to float |
| `texto()` | str() | Convert to string |
| `lista()` | list() | Create a list |
| `tupla()` | tuple() | Create a tuple |
| `conjunto()` | set() | Create a set |
| `dicionario()` | dict() | Create a dictionary |
| `soma()` | sum() | Sum values |
| `minimo()` | min() | Find minimum |
| `maximo()` | max() | Find maximum |
| `ordenado()` | sorted() | Sort items |

## Running Your Programs

### Method 1: Using `python -m pt_br` (Recommended)

```bash
python -m pt_br seu_script.py
```

This method:
- ✅ Works on any system
- ✅ No setup needed
- ✅ Most reliable

### Method 2: Direct Python (requires `import pt_br` at top)

```python
import pt_br

# Your code here...
```

Then run normally:
```bash
python seu_script.py
```

This method:
- ✅ More natural
- ✅ No command line tricks
- ⚠️ Must have `import pt_br` at the very top

### Method 3: Using the wrapper script

```bash
./pt-br seu_script.py
```

This method:
- ✅ Cleanest syntax
- ⚠️ Need to set up executable (see QUICK_START.md)

## Example Programs

We've included several examples in the `examples/` directory:

- **hello_world.py** - Basic output and variables
- **loops.py** - For and while loops
- **conditionals.py** - If/elif/else statements  
- **functions.py** - Function definitions and calls
- **data_structures.py** - Lists, dicts, tuples, sets

Try running them:

```bash
python -m pt_br examples/hello_world.py
python -m pt_br examples/loops.py
python -m pt_br examples/conditionals.py
```

## Important Notes

### 1. Import must be first

If using `python seu_script.py` directly, `import pt_br` **must be the first line**:

```python
import pt_br  # ← Must be first!

funcao main():
    imprimir("Olá")
```

### 2. Strings and comments are protected

Words inside strings won't be translated:

```python
import pt_br

# This comment stays in Portuguese
mensagem = "para sempre"  # The word 'para' inside the string stays as is
imprimir(mensagem)
```

### 3. IDE limitations

Your IDE (VS Code, PyCharm, etc.) won't recognize pt-BR keywords. This is expected and doesn't affect execution.

You can still:
- ✅ Use auto-formatting
- ✅ Use syntax highlighting (though colors may be off)
- ✅ Use extensions for Python syntax
- ✅ Run the code without issues

### 4. Debugging

If you encounter errors, the traceback will show translated (English) Python code. This is because the translator converts your pt-BR code to Python before execution.

## Next Steps

1. **Run the examples**: Try each example program to see what's possible
2. **Read FULL_GUIDE.md**: Get complete details on every keyword and function
3. **Read TROUBLESHOOTING.md**: Find solutions for common issues
4. **Write your own programs**: Start small and build up!

## Getting Help

- Check **TROUBLESHOOTING.md** for common issues
- Read **FULL_GUIDE.md** for detailed documentation
- Review the **examples/** directory for working code
- Open an issue on GitHub if you find bugs

## Ready to Explore?

You now have all the basics to start writing Python in Portuguese! Start with simple programs and gradually try more complex features.

Happy coding! 🎉
