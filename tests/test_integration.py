"""Integration tests for the pt-BR translator.

Tests end-to-end scenarios:
- Running actual pt-BR example scripts
- Verifying output matches expectations
- Testing import hook functionality
"""

import subprocess
import sys
import os
import pytest
from pt_br.translator import translate_source


class TestTranslateAndExecute:
    """Test translating and executing code directly."""

    def test_translate_and_execute_simple_loop(self):
        """Test translating and executing a simple loop."""
        pt_br_code = """
resultado = []
para i em intervalo(3):
    resultado.append(i)
"""
        translated = translate_source(pt_br_code)
        # Execute translated code
        namespace = {}
        exec(translated, namespace)
        assert namespace["resultado"] == [0, 1, 2]

    def test_translate_and_execute_conditional(self):
        """Test translating and executing conditionals."""
        pt_br_code = """
se verdadeiro:
    resultado = "ok"
senao:
    resultado = "not ok"
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert namespace["resultado"] == "ok"

    def test_translate_and_execute_function_definition(self):
        """Test translating and executing function definitions."""
        pt_br_code = """
funcao dobro(x):
    retorna x * 2

resultado = dobro(5)
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert namespace["resultado"] == 10

    def test_translate_and_execute_with_builtins(self):
        """Test translating code using pt-BR builtins."""
        pt_br_code = """
numeros = [1, 2, 3, 4, 5]
resultado_soma = soma(numeros)
resultado_min = minimo(numeros)
resultado_max = maximo(numeros)
resultado_len = comprimento(numeros)
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert namespace["resultado_soma"] == 15
        assert namespace["resultado_min"] == 1
        assert namespace["resultado_max"] == 5
        assert namespace["resultado_len"] == 5

    def test_translate_and_execute_list_operations(self):
        """Test translating list operations."""
        pt_br_code = """
numeros = lista([1, 2, 3])
numeros_tupla = tupla([1, 2, 3])
resultado = comprimento(numeros)
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert namespace["resultado"] == 3
        assert isinstance(namespace["numeros"], list)
        assert isinstance(namespace["numeros_tupla"], tuple)

    def test_translate_and_execute_type_conversion(self):
        """Test type conversion functions."""
        pt_br_code = """
x = inteiro("42")
y = flutuante("3.14")
z = texto(100)
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert namespace["x"] == 42
        assert namespace["y"] == 3.14
        assert namespace["z"] == "100"

    def test_translate_and_execute_boolean_logic(self):
        """Test boolean logic operations."""
        pt_br_code = """
resultado1 = verdadeiro e falso
resultado2 = verdadeiro ou falso
resultado3 = nao falso
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert namespace["resultado1"] is False
        assert namespace["resultado2"] is True
        assert namespace["resultado3"] is True

    def test_translate_and_execute_while_loop(self):
        """Test while loop translation and execution."""
        pt_br_code = """
resultado = 0
contador = 0
enquanto contador < 5:
    resultado = resultado + contador
    contador = contador + 1
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert namespace["resultado"] == 10  # 0 + 1 + 2 + 3 + 4

    def test_translate_and_execute_break_continue(self):
        """Test break and continue statements."""
        pt_br_code = """
resultado = []
para i em intervalo(10):
    se i == 5:
        quebra
    se i % 2 == 0:
        continua
    resultado.append(i)
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert namespace["resultado"] == [1, 3]

    def test_translate_and_execute_nested_loops(self):
        """Test nested loops."""
        pt_br_code = """
resultado = []
para i em intervalo(3):
    para j em intervalo(2):
        resultado.append((i, j))
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert len(namespace["resultado"]) == 6

    def test_translate_and_execute_class_definition(self):
        """Test class definition."""
        pt_br_code = """
classe Pessoa:
    funcao __init__(self, nome):
        self.nome = nome
    
    funcao saudar(self):
        retorna f"Olá, {self.nome}!"

pessoa = Pessoa("João")
resultado = pessoa.saudar()
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert "João" in namespace["resultado"]


class TestErrorHandling:
    """Test error handling in translation and execution."""

    def test_syntax_error_in_translated_code(self):
        """Test that syntax errors are reported properly."""
        # This should raise a SyntaxError during compilation
        pt_br_code = "se verdadeiro"  # Missing colon - should be invalid
        with pytest.raises(SyntaxError):
            translate_source(pt_br_code)
            # Try to compile it
            compile(translate_source(pt_br_code), "<string>", "exec")

    def test_runtime_error_in_translated_code(self):
        """Test that runtime errors are reported properly."""
        pt_br_code = """
x = 1 / 0  # Division by zero
"""
        translated = translate_source(pt_br_code)
        with pytest.raises(ZeroDivisionError):
            exec(translated)

    def test_name_error_in_translated_code(self):
        """Test that name errors are reported properly."""
        pt_br_code = """
resultado = variavel_inexistente
"""
        translated = translate_source(pt_br_code)
        with pytest.raises(NameError):
            exec(translated)


class TestComplexScenarios:
    """Test complex real-world scenarios."""

    def test_fibonacci_function(self):
        """Test a Fibonacci function in pt-BR."""
        pt_br_code = """
funcao fibonacci(n):
    se n <= 1:
        retorna n
    senao:
        retorna fibonacci(n - 1) + fibonacci(n - 2)

resultado = [fibonacci(i) para i em intervalo(6)]
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert namespace["resultado"] == [0, 1, 1, 2, 3, 5]

    def test_list_filtering(self):
        """Test list filtering with pt-BR."""
        pt_br_code = """
numeros = intervalo(10)
pares = [n para n em numeros se n % 2 == 0]
resultado = soma(pares)
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert namespace["resultado"] == 20  # 0 + 2 + 4 + 6 + 8

    def test_dictionary_operations(self):
        """Test dictionary operations."""
        pt_br_code = """
dados = dicionario(nome="João", idade=30)
resultado = dados
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert namespace["resultado"]["nome"] == "João"
        assert namespace["resultado"]["idade"] == 30

    def test_enumerate_and_zip(self):
        """Test enumerate and zip functions."""
        pt_br_code = """
nomes = ["Alice", "Bob", "Charlie"]
idades = [25, 30, 35]
resultado = []
para i, nome em enumerar(nomes):
    resultado.append((i, nome, idades[i]))
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert len(namespace["resultado"]) == 3
        assert namespace["resultado"][0] == (0, "Alice", 25)

    def test_map_and_filter(self):
        """Test map and filter functions."""
        pt_br_code = """
numeros = [1, 2, 3, 4, 5]
dobrados = lista(mapa(lambda x: x * 2, numeros))
resultado = dobrados
"""
        translated = translate_source(pt_br_code)
        namespace = {}
        exec(translated, namespace)
        assert namespace["resultado"] == [2, 4, 6, 8, 10]
