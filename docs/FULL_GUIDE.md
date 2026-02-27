# Complete Reference Guide for python-pt-br

This guide provides detailed documentation for every keyword and built-in function supported by python-pt-br.

## Table of Contents

1. [Keywords](#keywords)
2. [Built-in Functions](#built-in-functions)
3. [Examples by Feature](#examples-by-feature)
4. [Known Limitations](#known-limitations)

---

## Keywords

### Function Definition: `funcao` (def)

Define reusable blocks of code.

**Syntax:**
```python
funcao nome_da_funcao():
    # body

funcao nome_da_funcao(parametro1, parametro2):
    # body
```

**Example:**
```python
import pt_br

funcao saudar(nome):
    imprimir(f"Olá, {nome}!")

funcao somar(a, b):
    retorna a + b

saudar("Maria")
resultado = somar(10, 5)
imprimir(resultado)  # 15
```

**Notes:**
- Functions can take zero or more parameters
- Use `retorna` to return values
- Parameters can have default values

### Class Definition: `classe` (class)

Define custom data types and objects.

**Syntax:**
```python
classe NomeDaClasse:
    funcao __init__(self):
        # initialization

    funcao metodo(self):
        # method body
```

**Example:**
```python
import pt_br

classe Pessoa:
    funcao __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    funcao apresentar(self):
        imprimir(f"Meu nome é {self.nome}")
        imprimir(f"Tenho {self.idade} anos")

pessoa = Pessoa("João", 30)
pessoa.apresentar()
```

**Notes:**
- Classes are templates for creating objects
- `__init__` is the constructor (automatically called on creation)
- `self` refers to the instance itself

### For Loop: `para` (for)

Iterate over sequences.

**Syntax:**
```python
para variavel em sequencia:
    # body
```

**Example:**
```python
import pt_br

# Loop through range
para i em intervalo(5):
    imprimir(i)  # 0, 1, 2, 3, 4

# Loop through list
frutas = ["maçã", "banana", "laranja"]
para fruta em frutas:
    imprimir(fruta)

# Loop through string
para letra em "python":
    imprimir(letra)
```

**Notes:**
- Use with `em` (in)
- Works with any iterable: lists, strings, ranges, dictionaries (loops keys)
- Cannot modify list while looping directly (use `.pop()` instead)

### In Operator: `em` (in)

Used with `para` loops; checks if item is in sequence.

**Syntax:**
```python
para item em lista:
    # body

se item em lista:
    # item exists
```

**Example:**
```python
import pt_br

numeros = [1, 2, 3, 4, 5]

para numero em numeros:
    imprimir(numero)

se 3 em numeros:
    imprimir("3 está na lista")
```

### While Loop: `enquanto` (while)

Repeat while condition is true.

**Syntax:**
```python
enquanto condicao:
    # body
```

**Example:**
```python
import pt_br

contador = 0
enquanto contador < 5:
    imprimir(contador)
    contador = contador + 1

# With break
enquanto verdadeiro:
    entrada_usuario = entrada("Digite 'sair' para parar: ")
    se entrada_usuario == "sair":
        quebra
    imprimir(f"Você digitou: {entrada_usuario}")
```

**Notes:**
- Infinite loop if condition never becomes false
- Use `quebra` to exit early
- Use `continua` to skip to next iteration

### Conditional: `se` (if)

Execute code based on condition.

**Syntax:**
```python
se condicao:
    # body if true
```

**Example:**
```python
import pt_br

idade = 18

se idade >= 18:
    imprimir("Maior de idade")
    imprimir("Pode votar")
```

**Notes:**
- Condition must evaluate to `Verdadeiro` or `Falso`
- Can be combined with `senao_se` and `senao`
- Use logical operators: `e`, `ou`, `nao`

### Else If: `senao_se` (elif)

Additional condition if previous was false.

**Syntax:**
```python
se condicao1:
    # body if condicao1 is true
senao_se condicao2:
    # body if condicao2 is true
senao_se condicao3:
    # body if condicao3 is true
senao:
    # body if all conditions are false
```

**Example:**
```python
import pt_br

nota = 85

se nota >= 90:
    imprimir("A")
senao_se nota >= 80:
    imprimir("B")
senao_se nota >= 70:
    imprimir("C")
senao_se nota >= 60:
    imprimir("D")
senao:
    imprimir("F")
```

**Notes:**
- Can have multiple `senao_se` blocks
- `senao` is optional
- `senao_se` is checked left to right; first true block executes

### Else: `senao` (else)

Default case when all conditions are false.

**Syntax:**
```python
se condicao:
    # body if true
senao:
    # body if false
```

**Example:**
```python
import pt_br

idade = 15

se idade >= 18:
    imprimir("Maior de idade")
senao:
    imprimir("Menor de idade")
```

### Return: `retorna` (return)

Exit function and optionally return a value.

**Syntax:**
```python
retorna
retorna valor
```

**Example:**
```python
import pt_br

funcao dobro(x):
    retorna x * 2

funcao verificar_par(numero):
    se numero % 2 == 0:
        retorna verdadeiro
    retorna falso

resultado = dobro(5)
imprimir(resultado)  # 10

eh_par = verificar_par(4)
imprimir(eh_par)  # Verdadeiro
```

**Notes:**
- Function automatically returns `nulo` if no `retorna` is specified
- Can return any value: number, string, list, object, etc.
- Multiple `retorna` statements allowed (function stops at first)

### Break: `quebra` (break)

Exit loop immediately.

**Syntax:**
```python
quebra
```

**Example:**
```python
import pt_br

para i em intervalo(100):
    se i == 5:
        quebra  # Exit loop when i is 5
    imprimir(i)  # prints 0, 1, 2, 3, 4
```

**Notes:**
- Only breaks the innermost loop
- In nested loops, only exits one level

### Continue: `continua` (continue)

Skip to next iteration of loop.

**Syntax:**
```python
continua
```

**Example:**
```python
import pt_br

para i em intervalo(10):
    se i % 2 == 0:
        continua  # Skip even numbers
    imprimir(i)  # prints 1, 3, 5, 7, 9
```

**Notes:**
- Skips remaining body of current iteration
- Moves to next iteration

### Logical AND: `e` (and)

True only if both conditions are true.

**Syntax:**
```python
se condicao1 e condicao2:
    # body if both true
```

**Example:**
```python
import pt_br

idade = 25
carteira = verdadeiro

se idade >= 18 e carteira:
    imprimir("Pode dirigir")
```

**Notes:**
- Both sides must be true for result to be true
- Short-circuit: if left is false, right is not evaluated

### Logical OR: `ou` (or)

True if at least one condition is true.

**Syntax:**
```python
se condicao1 ou condicao2:
    # body if either is true
```

**Example:**
```python
import pt_br

dia = "domingo"

se dia == "sábado" ou dia == "domingo":
    imprimir("É fim de semana")
```

**Notes:**
- At least one side must be true
- Short-circuit: if left is true, right is not evaluated

### Logical NOT: `nao` (not)

Inverts boolean value.

**Syntax:**
```python
nao condicao
se nao condicao:
    # body
```

**Example:**
```python
import pt_br

ativo = falso

se nao ativo:
    imprimir("Conta inativa")

se nao (idade < 18):
    imprimir("É um adulto")
```

### Boolean True: `verdadeiro` (True)

Boolean true value.

**Example:**
```python
import pt_br

esta_ativo = verdadeiro

se esta_ativo:
    imprimir("Sistema ativo")
```

### Boolean False: `falso` (False)

Boolean false value.

**Example:**
```python
import pt_br

passou_teste = falso

se nao passou_teste:
    imprimir("Tente novamente")
```

### Null Value: `nulo` (None)

Represents absence of value.

**Example:**
```python
import pt_br

resultado = nulo

funcao talvez_retorna(condicao):
    se condicao:
        retorna "sucesso"
    retorna nulo

valor = talvez_retorna(falso)
se valor == nulo:
    imprimir("Nenhum valor retornado")
```

**Notes:**
- Used to represent "no value"
- Useful as default value
- Common in optional returns

---

## Built-in Functions

### Print: `imprimir()` (print)

Output text to console.

**Signature:**
```python
imprimir(valor1, valor2, ...)
```

**Example:**
```python
import pt_br

imprimir("Olá, Mundo!")
imprimir("Olá", "Mundo")  # separate with space
imprimir(123)
imprimir(1, 2, 3, 4, 5)
```

**Notes:**
- Can take multiple arguments
- Automatically adds newline at end
- Converts non-strings to strings

### Input: `entrada()` (input)

Read user input from console.

**Signature:**
```python
entrada(prompt="")
```

**Example:**
```python
import pt_br

nome = entrada("Qual é seu nome? ")
imprimir(f"Olá, {nome}!")

idade_texto = entrada("Idade: ")
idade = inteiro(idade_texto)
```

**Notes:**
- Returns string always
- Convert to number with `inteiro()` or `flutuante()`
- Prompt is optional

### Range: `intervalo()` (range)

Generate sequence of numbers.

**Signature:**
```python
intervalo(fim)
intervalo(inicio, fim)
intervalo(inicio, fim, passo)
```

**Example:**
```python
import pt_br

# 0 to 4
para i em intervalo(5):
    imprimir(i)  # 0, 1, 2, 3, 4

# 1 to 10
para i em intervalo(1, 11):
    imprimir(i)  # 1, 2, ..., 10

# 0, 2, 4, 6, 8
para i em intervalo(0, 10, 2):
    imprimir(i)
```

**Notes:**
- Start is inclusive, end is exclusive
- Default start is 0, default step is 1
- Can be negative: `intervalo(10, 0, -1)` goes backward

### Length: `comprimento()` (len)

Get length of sequence.

**Signature:**
```python
comprimento(sequencia)
```

**Example:**
```python
import pt_br

lista = [1, 2, 3, 4, 5]
imprimir(comprimento(lista))  # 5

texto = "Python"
imprimir(comprimento(texto))  # 6

dicionario = {"a": 1, "b": 2}
imprimir(comprimento(dicionario))  # 2
```

**Notes:**
- Works with lists, strings, tuples, dicts, sets
- Doesn't work with numbers or single values

### Integer Conversion: `inteiro()` (int)

Convert value to integer.

**Signature:**
```python
inteiro(valor)
inteiro(valor, base)
```

**Example:**
```python
import pt_br

imprimir(inteiro("42"))  # 42
imprimir(inteiro(3.14))  # 3
imprimir(inteiro("101", 2))  # 5 (binary to decimal)
```

**Notes:**
- Removes decimal part (truncates)
- Converts strings to integers
- Can specify base for string conversion

### Float Conversion: `flutuante()` (float)

Convert value to decimal number.

**Signature:**
```python
flutuante(valor)
```

**Example:**
```python
import pt_br

imprimir(flutuante("3.14"))  # 3.14
imprimir(flutuante(42))  # 42.0
imprimir(flutuante("3.14e-1"))  # 0.314
```

**Notes:**
- Creates floating-point number
- Converts strings and integers
- Accepts scientific notation

### String Conversion: `texto()` (str)

Convert value to string.

**Signature:**
```python
texto(valor)
```

**Example:**
```python
import pt_br

imprimir(texto(42))  # "42"
imprimir(texto(3.14))  # "3.14"
imprimir(texto([1, 2, 3]))  # "[1, 2, 3]"
```

**Notes:**
- Creates string representation of value
- Useful for displaying non-strings

### List Constructor: `lista()` (list)

Create a list or convert sequence to list.

**Signature:**
```python
lista()
lista(sequencia)
```

**Example:**
```python
import pt_br

lista_vazia = lista()
imprimir(lista_vazia)  # []

tupla = (1, 2, 3)
lista_convertida = lista(tupla)
imprimir(lista_convertida)  # [1, 2, 3]

lista_de_letras = lista("abc")
imprimir(lista_de_letras)  # ['a', 'b', 'c']
```

**Notes:**
- Lists are mutable (can be modified)
- Convert tuples, strings, sets to lists

### Tuple Constructor: `tupla()` (tuple)

Create a tuple or convert sequence to tuple.

**Signature:**
```python
tupla()
tupla(sequencia)
```

**Example:**
```python
import pt_br

tupla_vazia = tupla()
imprimir(tupla_vazia)  # ()

lista = [1, 2, 3]
tupla_convertida = tupla(lista)
imprimir(tupla_convertida)  # (1, 2, 3)
```

**Notes:**
- Tuples are immutable (cannot be changed)
- More efficient for read-only data

### Set Constructor: `conjunto()` (set)

Create a set or convert sequence to set.

**Signature:**
```python
conjunto()
conjunto(sequencia)
```

**Example:**
```python
import pt_br

conjunto_vazio = conjunto()
imprimir(conjunto_vazio)  # set()

lista = [1, 2, 2, 3, 3, 3]
conjunto_convertido = conjunto(lista)
imprimir(conjunto_convertido)  # {1, 2, 3}
```

**Notes:**
- Sets remove duplicates
- Unordered
- Use for membership checking

### Dictionary Constructor: `dicionario()` (dict)

Create an empty dictionary.

**Signature:**
```python
dicionario()
```

**Example:**
```python
import pt_br

dicionario_vazio = dicionario()
imprimir(dicionario_vazio)  # {}

# Usually created with literal syntax
pessoa = {"nome": "João", "idade": 30}
```

**Notes:**
- Dictionaries store key-value pairs
- Most often created using `{}` syntax

### Sum: `soma()` (sum)

Add up all values in sequence.

**Signature:**
```python
soma(sequencia)
soma(sequencia, inicio)
```

**Example:**
```python
import pt_br

numeros = [1, 2, 3, 4, 5]
imprimir(soma(numeros))  # 15

imprimir(soma(numeros, 10))  # 25 (starts from 10)
```

**Notes:**
- Works with lists, tuples, sets
- All elements should be numbers

### Minimum: `minimo()` (min)

Find smallest value.

**Signature:**
```python
minimo(sequencia)
minimo(valor1, valor2, ...)
```

**Example:**
```python
import pt_br

numeros = [5, 2, 8, 1, 9]
imprimir(minimo(numeros))  # 1

imprimir(minimo(5, 2, 8, 1, 9))  # 1
```

**Notes:**
- Can take sequence or multiple arguments
- Works with any comparable types

### Maximum: `maximo()` (max)

Find largest value.

**Signature:**
```python
maximo(sequencia)
maximo(valor1, valor2, ...)
```

**Example:**
```python
import pt_br

numeros = [5, 2, 8, 1, 9]
imprimir(maximo(numeros))  # 9

imprimir(maximo(5, 2, 8, 1, 9))  # 9
```

**Notes:**
- Can take sequence or multiple arguments
- Works with any comparable types

### Sorted: `classifica()` (sorted)

Sort items in a sequence.

**Signature:**
```python
classifica(sequencia)
```

**Example:**
```python
import pt_br

numeros = [5, 2, 8, 1, 9]
imprimir(classifica(numeros))  # [1, 2, 5, 8, 9]

nomes = ["Carlos", "Ana", "Bruno"]
imprimir(classifica(nomes))  # ['Ana', 'Bruno', 'Carlos']
```

**Notes:**
- Returns new sorted list
- Doesn't modify original
- Works with numbers and strings

---

## Examples by Feature

### Example 1: Simple Calculator

```python
import pt_br

funcao calcular(operacao, a, b):
    se operacao == "+":
        retorna a + b
    senao_se operacao == "-":
        retorna a - b
    senao_se operacao == "*":
        retorna a * b
    senao_se operacao == "/":
        retorna a / b
    senao:
        retorna nulo

imprimir("Calculadora Simples")
num1 = inteiro(entrada("Número 1: "))
op = entrada("Operação (+, -, *, /): ")
num2 = inteiro(entrada("Número 2: "))

resultado = calcular(op, num1, num2)
imprimir(f"Resultado: {resultado}")
```

### Example 2: Processing Data

```python
import pt_br

dados = [
    {"nome": "Ana", "nota": 85},
    {"nome": "Bruno", "nota": 92},
    {"nome": "Carlos", "nota": 78}
]

imprimir("=== Análise de Notas ===")
notas = [d["nota"] para d em dados]

imprimir(f"Maior nota: {maximo(notas)}")
imprimir(f"Menor nota: {minimo(notas)}")
imprimir(f"Média: {soma(notas) / comprimento(notas):.2f}")

para aluno em dados:
    imprimir(f"{aluno['nome']}: {aluno['nota']}")
```

### Example 3: File-like Pattern

```python
import pt_br

classe ListaCompras:
    funcao __init__(self):
        self.itens = []
    
    funcao adicionar(self, item):
        self.itens.acrescentar(item)
    
    funcao remover(self, item):
        se item em self.itens:
            self.itens.remover(item)
    
    funcao exibir(self):
        imprimir("Lista de Compras:")
        para i em intervalo(comprimento(self.itens)):
            imprimir(f"  {i+1}. {self.itens[i]}")

compras = ListaCompras()
compras.adicionar("Leite")
compras.adicionar("Pão")
compras.adicionar("Queijo")
compras.exibir()
```

---

## Known Limitations

1. **IDE Support**: IDEs don't recognize pt-BR keywords (syntax highlighting won't work perfectly)
2. **Error Messages**: Tracebacks show translated English code
3. **Module Names**: Only Python files can use pt-BR; C extensions are English-only
4. **Type Hints**: Type annotations must use English names
5. **Lambda Functions**: `lambda` keyword is not translated (not commonly used)
6. **Decorators**: Decorator syntax is not translated (advanced feature)
7. **Context Managers**: `with` statement is not translated
8. **Async/Await**: Async keywords are not translated
9. **Imports**: Module names and library names must be English

These are intentional design choices to keep the translator simple and focused on educational use.

---

## Quick Reference

**Keywords**: `funcao`, `classe`, `para`, `em`, `enquanto`, `se`, `senao_se`, `senao`, `retorna`, `quebra`, `continua`, `e`, `ou`, `nao`, `verdadeiro`, `falso`, `nulo`

**Functions**: `imprimir`, `entrada`, `intervalo`, `comprimento`, `inteiro`, `flutuante`, `texto`, `lista`, `tupla`, `conjunto`, `dicionario`, `soma`, `minimo`, `maximo`, `classifica`
