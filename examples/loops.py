# Loops Example - Demonstrating para and enquanto
# This example shows for loops and while loops in Portuguese

import pt_br

# For loop using 'para' and 'intervalo'
imprimir("=== FOR LOOPS (para e intervalo) ===")
imprimir("Contando de 0 a 4:")

para i em intervalo(5):
    imprimir(f"Número: {i}")

imprimir("\nContando de 1 a 10, de 2 em 2:")
para i em intervalo(1, 11, 2):
    imprimir(i)

# For loop with list iteration
imprimir("\n=== Iterating over a list ===")
frutas = ["maçã", "banana", "laranja", "morango"]
imprimir("Frutas disponíveis:")

para fruta em frutas:
    imprimir(f"  - {fruta}")

# While loop using 'enquanto'
imprimir("\n=== WHILE LOOPS (enquanto) ===")
contador = 0
imprimir("Contagem regressiva de 5 até 1:")

enquanto contador < 5:
    contador = contador + 1
    imprimir(f"Contagem: {6 - contador}")

# While loop with condition
imprimir("\nAcumulando números:")
soma = 0
numero = 1

enquanto numero <= 5:
    soma = soma + numero
    imprimir(f"Somando {numero}, total agora: {soma}")
    numero = numero + 1

imprimir(f"Soma final: {soma}")

# Nested loops
imprimir("\n=== NESTED LOOPS (laços aninhados) ===")
imprimir("Tabuada 2x3:")

para i em intervalo(1, 3):
    para j em intervalo(1, 4):
        imprimir(f"{i} x {j} = {i * j}")
    imprimir("")  # blank line for readability
