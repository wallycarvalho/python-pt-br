# python-pt-br

Write Python code in Brazilian Portuguese (pt-BR)!

A Python package that enables developers to write Python code using pt-BR keywords and built-in function names, making Python more accessible for Portuguese-speaking learners.

## Quick Start

Create a file `hello.py`:

```python
import pt_br

imprimir("Olá, Mundo!")

para i em intervalo(5):
    imprimir(i)
```

Run it:

```bash
python -m pt_br hello.py
```

Or with a specific Python version:

```bash
python3.13 -m pt_br hello.py
```

## Installation

```bash
pip install python-pt-br
```

## Features

- ✅ Write `.py` files in Portuguese Brazilian—execute them normally
- ✅ Translate pt-BR keywords: `para` → `for`, `se` → `if`, `enquanto` → `while`
- ✅ Translate pt-BR built-in functions: `imprimir()` → `print()`, `intervalo()` → `range()`
- ✅ Zero friction: just add `import pt_br` at the top of your script
- ✅ Near-native performance (translates to Python, then executes)
- ✅ Educational focus—designed for learners

## Example

### Write in Portuguese Brazilian:

```python
import pt_br

para i em intervalo(5):
    se i % 2 == 0:
        imprimir(f"Número par: {i}")
    senao:
        imprimir(f"Número ímpar: {i}")
```

### Runs as Standard Python:

```bash
$ python -m pt_br seu_script.py
Número par: 0
Número ímpar: 1
Número par: 2
Número ímpar: 3
Número par: 4
```

## Supported Keywords & Functions

See [documentation](docs/GETTING_STARTED.md) for full list of supported keywords and functions.

### Keywords (16)

`para`, `em`, `se`, `senao`, `enquanto`, `e`, `ou`, `nao`, `verdadeiro`, `falso`, `nulo`, `quebra`, `continua`, `retorna`, `funcao`, `classe`

### Functions (20+)

`imprimir()`, `entrada()`, `intervalo()`, `comprimento()`, `lista()`, `tupla()`, `conjunto()`, `dicionario()`, `inteiro()`, `flutuante()`, `texto()`, `soma()`, `minimo()`, `maximo()`, `classifica()`, and more

## How It Works

1. You write Python code using pt-BR keywords
2. You add `import pt_br` at the top
3. Import hook intercepts your module
4. Translator converts pt-BR → Python
5. Python executes normally

No build steps, no CLI tools—just pure Python!

## Documentation

- [Getting Started Guide](docs/GETTING_STARTED.md)
- [Full API Reference](docs/FULL_GUIDE.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)

## Examples

Check the `examples/` directory for working example scripts:

- `hello_world.py` — Basic output
- `loops.py` — For and while loops
- `conditionals.py` — If/else statements
- `functions.py` — Function definitions
- `data_structures.py` — Lists, dicts, tuples

## Project Status

- ✅ Planning phase complete
- 🚀 MVP development in progress
- 📦 Initial release: v0.1.0

## Contributing

We welcome contributions! Please see CONTRIBUTING.md (coming soon).

## License

MIT License - See LICENSE file for details.

## Changelog

### v0.1.0 (In Development)
- Initial MVP release
- 16 keywords support
- 10 core built-in functions
- Comprehensive test suite

## FAQ

**Q: Will my code run on other people's machines?**  
A: Yes! Once they install `python-pt-br`, they can run your code normally.

**Q: Does this work with IDEs?**  
A: Yes, but IDEs won't recognize pt-BR keywords (limitation of current approach). This is acceptable for educational use.

**Q: Can I use other Python libraries?**  
A: Yes! You can import and use any Python library normally.

**Q: Will this support other languages?**  
A: Yes! After the MVP, we plan to add support for other languages.

## Support

- 📖 Read the [documentation](docs/GETTING_STARTED.md)
- 🐛 Report issues on GitHub
- 💬 Ask questions in discussions

---

**Made with ❤️ for Portuguese-speaking Python learners**
