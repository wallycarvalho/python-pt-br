"""Test: Functions"""
import pt_br

def dobro(x):
    retorna x * 2

def saudacao(nome):
    imprimir(f"Olá, {nome}!")

# Test function with return
resultado = dobro(5)
imprimir(f"Dobro de 5 é {resultado}")

# Test function with no return
saudacao("Maria")

# Test with built-in functions
numeros = [1, 2, 3, 4, 5]
imprimir(f"Soma: {soma(numeros)}")
imprimir(f"Mínimo: {minimo(numeros)}")
imprimir(f"Máximo: {maximo(numeros)}")
imprimir(f"Comprimento: {comprimento(numeros)}")
