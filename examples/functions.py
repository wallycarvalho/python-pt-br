# Functions Example - Demonstrating function definition and calls
# This example shows how to define and use functions in Portuguese

import pt_br

# Simple function without parameters
imprimir("=== Simple functions ===")

funcao saudacao():
    imprimir("Olá! Bem-vindo ao python-pt-br!")

saudacao()

# Function with parameters
imprimir("\n=== Functions with parameters ===")

funcao soma(a, b):
    resultado = a + b
    retorna resultado

valor1 = 5
valor2 = 3
resultado_soma = soma(valor1, valor2)
imprimir(f"A soma de {valor1} e {valor2} é: {resultado_soma}")

# Function with multiple return values
imprimir("\n=== Function with return value ===")

funcao dobro(x):
    retorna x * 2

numero = 7
resultado_dobro = dobro(numero)
imprimir(f"O dobro de {numero} é: {resultado_dobro}")

# Function with conditional logic
imprimir("\n=== Function with conditionals ===")

funcao classificar_idade(idade):
    se idade < 13:
        retorna "Criança"
    senao_se idade < 18:
        retorna "Adolescente"
    senao_se idade < 60:
        retorna "Adulto"
    senao:
        retorna "Idoso"

para idade em [10, 15, 25, 65]:
    classificacao = classificar_idade(idade)
    imprimir(f"Idade {idade}: {classificacao}")

# Function with loop
imprimir("\n=== Function with loop ===")

funcao tabuada(numero):
    imprimir(f"Tabuada do {numero}:")
    para i em intervalo(1, 11):
        resultado = numero * i
        imprimir(f"  {numero} x {i} = {resultado}")

tabuada(7)

# Function with default parameters
imprimir("\n=== Function with default parameters ===")

funcao cumprimento(nome, tratamento="Sr."):
    imprimir(f"Olá, {tratamento} {nome}!")

cumprimento("João")
cumprimento("Maria", "Dra.")

# Function that processes a list
imprimir("\n=== Function processing list ===")

funcao processar_lista(lista):
    soma = 0
    para elemento em lista:
        soma = soma + elemento
    retorna soma

numeros = [1, 2, 3, 4, 5]
total = processar_lista(numeros)
imprimir(f"Soma da lista {numeros}: {total}")

# Calling functions within functions
imprimir("\n=== Nested function calls ===")

funcao quadrado(x):
    retorna x * x

funcao cubo(x):
    resultado_quadrado = quadrado(x)
    retorna resultado_quadrado * x

numero = 3
imprimir(f"Quadrado de {numero}: {quadrado(numero)}")
imprimir(f"Cubo de {numero}: {cubo(numero)}")
