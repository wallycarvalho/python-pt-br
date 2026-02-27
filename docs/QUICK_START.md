# Quick Start Guide

## Installation

```bash
pip install python-pt-br
```

## Running pt-BR Python Scripts

There are multiple ways to run Python scripts written in Portuguese Brazilian:

### Option 1: Using `python -m pt_br` (Recommended)

This is the simplest and most portable method:

```bash
python -m pt_br seu_script.py
```

**Advantages:**
- Works on any system with Python installed
- No additional setup needed
- Works with Python 3.8+

**Example:**
```bash
python -m pt_br hello.py
# or with Python 3.13:
python3.13 -m pt_br hello.py
```

### Option 2: Using the `pt-br` wrapper script

For convenience, you can use the included wrapper script:

```bash
./pt-br seu_script.py
# or
python pt-br seu_script.py
```

**Advantages:**
- More natural syntax
- No need to type `-m pt_br`

**Setup:**
```bash
chmod +x pt-br  # Make it executable
```

### Option 3: Importing modules with pt-BR code

You can import modules written in pt-BR directly:

```python
import pt_br
import meu_modulo  # meu_modulo.py written in pt-BR
```

## Example Script

Create a file named `hello.py`:

```python
import pt_br

imprimir("Olá, Mundo!")

numeros = [1, 2, 3, 4, 5]

para i em numeros:
    imprimir(f"Número: {i}")

se soma(numeros) > 10:
    imprimir("A soma é maior que 10!")
```

Run it:

```bash
# Method 1
python -m pt_br hello.py

# Method 2
python pt-br hello.py

# Method 3
python hello.py  # (after 'import pt_br' at the top)
```

## Supported Keywords

| Portuguese | English | Example |
|------------|---------|---------|
| `para` | for | `para i em intervalo(5):` |
| `em` | in | `para item em lista:` |
| `se` | if | `se x > 0:` |
| `senao` | else | `senao:` |
| `senao_se` | elif | `senao_se x == 0:` |
| `enquanto` | while | `enquanto condicao:` |
| `e` | and | `se x e y:` |
| `ou` | or | `se x ou y:` |
| `nao` | not | `se nao x:` |
| `verdadeiro` | True | `x = verdadeiro` |
| `falso` | False | `x = falso` |
| `nulo` | None | `x = nulo` |
| `quebra` | break | `quebra` |
| `continua` | continue | `continua` |
| `retorna` | return | `retorna x` |
| `funcao` | def | `def minha_funcao():` |
| `classe` | class | `classe MinhaClasse:` |

## Supported Built-in Functions

| Portuguese | English | Example |
|------------|---------|---------|
| `imprimir()` | print() | `imprimir("Olá")` |
| `entrada()` | input() | `nome = entrada("Nome:")` |
| `intervalo()` | range() | `para i em intervalo(10):` |
| `comprimento()` | len() | `comprimento(lista)` |
| `lista()` | list() | `lista([1, 2, 3])` |
| `tupla()` | tuple() | `tupla([1, 2])` |
| `conjunto()` | set() | `conjunto([1, 1, 2])` |
| `dicionario()` | dict() | `dicionario()` |
| `inteiro()` | int() | `inteiro("42")` |
| `flutuante()` | float() | `flutuante("3.14")` |
| `texto()` | str() | `texto(42)` |
| `soma()` | sum() | `soma([1, 2, 3])` |
| `minimo()` | min() | `minimo([3, 1, 2])` |
| `maximo()` | max() | `maximo([3, 1, 2])` |
| `classifica()` | sorted() | `classifica(lista)` |

## Important Notes

1. **Import must be first**: Add `import pt_br` at the very top of your script if using direct Python execution
2. **String protection**: Words inside strings won't be translated (e.g., `"para sempre"` stays as is)
3. **IDE support**: IDEs won't recognize pt-BR keywords (this is a known limitation)
4. **Error messages**: Tracebacks show the translated (Python) code

## Troubleshooting

**Error: `SyntaxError: invalid syntax` when running with `python script.py`**

Solution: Use `python -m pt_br script.py` instead

**Error: `ModuleNotFoundError: No module named 'pt_br'`**

Solution: Make sure you've installed python-pt-br:
```bash
pip install python-pt-br
```

**Functions like `soma`, `minimo` not found**

Solution: These translate to Python built-ins (`sum`, `min`). Make sure your import statement is at the top:
```python
import pt_br
```

## More Examples

See the `examples/` directory for more complete examples:
- `hello_world.py` - Basic output
- `loops.py` - Loops and iteration
- `conditionals.py` - If/else statements
- `functions.py` - Function definitions
- `data_structures.py` - Lists, dicts, tuples
