# Conditionals Example - Demonstrating if, elif, and else
# This example shows conditional logic using Portuguese keywords

import pt_br

# Simple if statement
imprimir("=== Simple IF statements ===")
idade = 18

se idade >= 18:
    imprimir("Você é maior de idade!")

# If-else statement
imprimir("\n=== IF-ELSE statements ===")
temperatura = 25

se temperatura >= 30:
    imprimir("Está muito quente!")
senao:
    imprimir("A temperatura está agradável.")

# If-elif-else statement
imprimir("\n=== IF-ELIF-ELSE statements ===")
nota = 85

se nota >= 90:
    imprimir("Conceito: A - Excelente!")
senao_se nota >= 80:
    imprimir("Conceito: B - Bom!")
senao_se nota >= 70:
    imprimir("Conceito: C - Satisfatório")
senao_se nota >= 60:
    imprimir("Conceito: D - Passável")
senao:
    imprimir("Conceito: F - Reprovado")

# Nested conditionals
imprimir("\n=== NESTED conditionals ===")
idade = 25
carteira_habilitacao = verdadeiro

se idade >= 18:
    se carteira_habilitacao:
        imprimir("Você pode dirigir!")
    senao:
        imprimir("Você é maior de idade, mas precisa tirar carteira de habilitação.")
senao:
    imprimir("Você é menor de idade e não pode dirigir.")

# Logical operators
imprimir("\n=== Logical operators (e, ou, nao) ===")
idade = 25
renda = 3000

se idade >= 18 e renda >= 2000:
    imprimir("Você pode solicitar um crédito!")

se idade < 18 ou renda < 2000:
    imprimir("Você não atende aos critérios de crédito.")

ativo = verdadeiro
se nao ativo:
    imprimir("Conta inativa")
senao:
    imprimir("Conta ativa")

# Multiple conditions
imprimir("\n=== Complex conditions ===")
hora = 14
dia_semana = "segunda"

se hora >= 9 e hora < 17 e dia_semana != "sábado" e dia_semana != "domingo":
    imprimir("Estabelecimento aberto!")
senao:
    imprimir("Estabelecimento fechado!")
