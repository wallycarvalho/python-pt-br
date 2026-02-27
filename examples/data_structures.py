# Data Structures Example - Working with lists, tuples, dicts, and sets
# This example demonstrates common data structure operations

import pt_br

# LISTS - Ordered, mutable collections
imprimir("=== LISTS (Listas) ===")
frutas = ["maçã", "banana", "laranja", "morango"]
imprimir(f"Lista original: {frutas}")

# Accessing elements
imprimir(f"Primeira fruta: {frutas[0]}")
imprimir(f"Última fruta: {frutas[-1]}")

# Adding elements
frutas.append("uva")
imprimir(f"Após acrescentar 'uva': {frutas}")

# Removing elements
frutas.remove("banana")
imprimir(f"Após remover 'banana': {frutas}")

# List length
imprimir(f"Total de frutas: {comprimento(frutas)}")

# Iterating through list
imprimir("Frutas disponíveis:")
para fruta em frutas:
    imprimir(f"  - {fruta}")

# TUPLES - Ordered, immutable collections
imprimir("\n=== TUPLES (Tuplas) ===")
coordenadas = (10, 20, 30)
imprimir(f"Tupla: {coordenadas}")
imprimir(f"Primeiro elemento: {coordenadas[0]}")
imprimir(f"Comprimento da tupla: {comprimento(coordenadas)}")

# DICTIONARIES - Key-value pairs
imprimir("\n=== DICTIONARIES (Dicionários) ===")
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo",
    "profissao": "Engenheiro"
}
imprimir(f"Dicionário: {pessoa}")

# Accessing values by key
imprimir(f"Nome: {pessoa['nome']}")
imprimir(f"Idade: {pessoa['idade']}")

# Adding new key-value pairs
pessoa["email"] = "joao@email.com"
imprimir(f"Após adicionar email: {pessoa}")

# Getting keys and values
imprimir("Chaves do dicionário:")
para chave em pessoa:
    imprimir(f"  {chave}: {pessoa[chave]}")

# SETS - Unordered, unique elements
imprimir("\n=== SETS (Conjuntos) ===")
numeros = {1, 2, 3, 4, 5, 5, 5}
imprimir(f"Conjunto: {numeros}")
imprimir(f"Total de elementos: {comprimento(numeros)}")

# SET OPERATIONS
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

imprimir(f"\nConjunto 1: {conjunto1}")
imprimir(f"Conjunto 2: {conjunto2}")

# Union (união) - using | operator
uniao = conjunto1 | conjunto2
imprimir(f"União: {uniao}")

# Intersection (interseção) - using & operator
interseccao = conjunto1 & conjunto2
imprimir(f"Interseção: {interseccao}")

# Difference (diferença) - using - operator
diferenca = conjunto1 - conjunto2
imprimir(f"Diferença: {diferenca}")

# LIST COMPREHENSION
imprimir("\n=== List Comprehension ===")
numeros = [1, 2, 3, 4, 5]
quadrados = [x * x para x em numeros]
imprimir(f"Números: {numeros}")
imprimir(f"Quadrados: {quadrados}")

# Filtering with list comprehension
pares = [x para x em numeros se x % 2 == 0]
imprimir(f"Números pares: {pares}")

# WORKING WITH MIXED STRUCTURES
imprimir("\n=== Mixed structures ===")
alunos = [
    {"nome": "Ana", "notas": [8.5, 9.0, 8.0]},
    {"nome": "Bruno", "notas": [7.0, 7.5, 8.0]},
    {"nome": "Carlos", "notas": [9.0, 9.5, 9.0]}
]

imprimir("Dados dos alunos:")
para aluno em alunos:
    nome = aluno["nome"]
    notas = aluno["notas"]
    media = soma(notas) / comprimento(notas)
    imprimir(f"  {nome} - Média: {media:.2f}")

# SLICING
imprimir("\n=== Slicing ===")
letras = ["a", "b", "c", "d", "e"]
imprimir(f"Lista original: {letras}")
imprimir(f"Primeiros 3 elementos [0:3]: {letras[0:3]}")
imprimir(f"Últimos 2 elementos [-2:]: {letras[-2:]}")
imprimir(f"Do índice 1 ao 4 [1:4]: {letras[1:4]}")

# SORTING
imprimir("\n=== Sorting ===")
numeros_aleatorios = [5, 2, 8, 1, 9, 3]
imprimir(f"Lista original: {numeros_aleatorios}")
numeros_classificas = classifica(numeros_aleatorios)
imprimir(f"Ordenado: {numeros_classificas}")

nomes = ["Carlos", "Ana", "Bruno", "Diana"]
nomes_classificas = classifica(nomes)
imprimir(f"Nomes classificas: {nomes_classificas}")
