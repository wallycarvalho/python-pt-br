"""Test: Conditionals"""
import pt_br

idade = 18

se idade >= 18:
    imprimir("Você é um adulto")
senao:
    imprimir("Você é menor de idade")

# Test with multiple conditions
x = 5

se x < 0:
    imprimir("Negativo")
senao_se x == 0:
    imprimir("Zero")
senao:
    imprimir("Positivo")
