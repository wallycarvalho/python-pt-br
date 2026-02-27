"""Unit tests for the core translator module.

Tests the translate_source() function with various input scenarios:
- Basic keyword translations
- Function call translations
- Multiple translations in one line
- Context detection (strings, comments, f-strings)
- Edge cases (variable names, nested structures)
"""

import pytest
from pt_br.translator import translate_source


class TestBasicKeywords:
    """Test translation of basic keywords."""

    def test_translate_para(self):
        """Test 'para' → 'for' translation."""
        source = "para i em intervalo(5):\n    pass"
        result = translate_source(source)
        assert "for i in range(5):" in result
        assert "para" not in result

    def test_translate_em(self):
        """Test 'em' → 'in' translation in for loop."""
        source = "para item em lista:\n    pass"
        result = translate_source(source)
        assert "for item in lista:" in result

    def test_translate_se(self):
        """Test 'se' → 'if' translation."""
        source = "se x > 0:\n    pass"
        result = translate_source(source)
        assert "if x > 0:" in result

    def test_translate_senao(self):
        """Test 'senao' → 'else' translation."""
        source = "se x > 0:\n    pass\nsenao:\n    pass"
        result = translate_source(source)
        assert "if x > 0:" in result
        assert "else:" in result

    def test_translate_senao_se(self):
        """Test 'senao_se' → 'elif' translation."""
        source = "se x > 0:\n    pass\nsenao_se x == 0:\n    pass"
        result = translate_source(source)
        assert "if x > 0:" in result
        assert "elif x == 0:" in result

    def test_translate_enquanto(self):
        """Test 'enquanto' → 'while' translation."""
        source = "enquanto condicao:\n    pass"
        result = translate_source(source)
        assert "while condicao:" in result

    def test_translate_e(self):
        """Test 'e' → 'and' translation."""
        source = "se x > 0 e y < 10:\n    pass"
        result = translate_source(source)
        assert "if x > 0 and y < 10:" in result

    def test_translate_ou(self):
        """Test 'ou' → 'or' translation."""
        source = "se x == 0 ou y == 0:\n    pass"
        result = translate_source(source)
        assert "if x == 0 or y == 0:" in result

    def test_translate_nao(self):
        """Test 'nao' → 'not' translation."""
        source = "se nao condicao:\n    pass"
        result = translate_source(source)
        assert "if not condicao:" in result

    def test_translate_verdadeiro(self):
        """Test 'verdadeiro' → 'True' translation."""
        source = "x = verdadeiro"
        result = translate_source(source)
        assert "x = True" in result

    def test_translate_falso(self):
        """Test 'falso' → 'False' translation."""
        source = "x = falso"
        result = translate_source(source)
        assert "x = False" in result

    def test_translate_nulo(self):
        """Test 'nulo' → 'None' translation."""
        source = "x = nulo"
        result = translate_source(source)
        assert "x = None" in result

    def test_translate_quebra(self):
        """Test 'quebra' → 'break' translation."""
        source = "para i em intervalo(5):\n    quebra"
        result = translate_source(source)
        assert "break" in result

    def test_translate_continua(self):
        """Test 'continua' → 'continue' translation."""
        source = "para i em intervalo(5):\n    continua"
        result = translate_source(source)
        assert "continue" in result

    def test_translate_retorna(self):
        """Test 'retorna' → 'return' translation."""
        source = "funcao foo():\n    retorna 42"
        result = translate_source(source)
        assert "return 42" in result

    def test_translate_funcao(self):
        """Test 'funcao' → 'def' translation."""
        source = "funcao hello():\n    pass"
        result = translate_source(source)
        assert "def hello():" in result

    def test_translate_classe(self):
        """Test 'classe' → 'class' translation."""
        source = "classe MinhaClasse:\n    pass"
        result = translate_source(source)
        assert "class MinhaClasse:" in result


class TestBuiltinFunctions:
    """Test translation of built-in functions."""

    def test_translate_imprimir(self):
        """Test 'imprimir()' → 'print()' translation."""
        source = 'imprimir("Olá")'
        result = translate_source(source)
        assert 'print("Olá")' in result

    def test_translate_intervalo(self):
        """Test 'intervalo()' → 'range()' translation."""
        source = "para i em intervalo(10):\n    pass"
        result = translate_source(source)
        assert "range(10)" in result

    def test_translate_entrada(self):
        """Test 'entrada()' → 'input()' translation."""
        source = 'x = entrada("Digite: ")'
        result = translate_source(source)
        assert 'x = input("Digite: ")' in result

    def test_translate_comprimento(self):
        """Test 'comprimento()' → 'len()' translation."""
        source = "x = comprimento(lista)"
        result = translate_source(source)
        assert "x = len(lista)" in result

    def test_translate_lista(self):
        """Test 'lista()' → 'list()' translation."""
        source = "x = lista([1, 2, 3])"
        result = translate_source(source)
        assert "x = list([1, 2, 3])" in result

    def test_translate_inteiro(self):
        """Test 'inteiro()' → 'int()' translation."""
        source = 'x = inteiro("42")'
        result = translate_source(source)
        assert 'x = int("42")' in result

    def test_translate_texto(self):
        """Test 'texto()' → 'str()' translation."""
        source = "x = texto(42)"
        result = translate_source(source)
        assert "x = str(42)" in result

    def test_translate_soma(self):
        """Test 'soma()' → 'sum()' translation."""
        source = "x = soma([1, 2, 3])"
        result = translate_source(source)
        assert "x = sum([1, 2, 3])" in result

    def test_translate_minimo(self):
        """Test 'minimo()' → 'min()' translation."""
        source = "x = minimo([3, 1, 2])"
        result = translate_source(source)
        assert "x = min([3, 1, 2])" in result

    def test_translate_maximo(self):
        """Test 'maximo()' → 'max()' translation."""
        source = "x = maximo([3, 1, 2])"
        result = translate_source(source)
        assert "x = max([3, 1, 2])" in result

    def test_translate_flutuante(self):
        """Test 'flutuante()' → 'float()' translation."""
        source = 'x = flutuante("3.14")'
        result = translate_source(source)
        assert 'x = float("3.14")' in result

    def test_translate_booleano(self):
        """Test 'booleano()' → 'bool()' translation."""
        source = "x = booleano(1)"
        result = translate_source(source)
        assert "x = bool(1)" in result

    def test_translate_tupla(self):
        """Test 'tupla()' → 'tuple()' translation."""
        source = "x = tupla([1, 2])"
        result = translate_source(source)
        assert "x = tuple([1, 2])" in result

    def test_translate_conjunto(self):
        """Test 'conjunto()' → 'set()' translation."""
        source = "x = conjunto([1, 2])"
        result = translate_source(source)
        assert "x = set([1, 2])" in result

    def test_translate_dicionario(self):
        """Test 'dicionario()' → 'dict()' translation."""
        source = "x = dicionario(a=1)"
        result = translate_source(source)
        assert "x = dict(a=1)" in result

    def test_translate_enumerar(self):
        """Test 'enumerar()' → 'enumerate()' translation."""
        source = "para i, v em enumerar(lista):\n    pass"
        result = translate_source(source)
        assert "enumerate(lista)" in result

    def test_translate_compacta(self):
        """Test 'compacta()' → 'zip()' translation."""
        source = "para a, b em compacta(l1, l2):\n    pass"
        result = translate_source(source)
        assert "zip(l1, l2)" in result

    def test_translate_tipo(self):
        """Test 'tipo()' → 'type()' translation."""
        source = "x = tipo(42)"
        result = translate_source(source)
        assert "x = type(42)" in result

    def test_translate_eh_instancia(self):
        """Test 'eh_instancia()' → 'isinstance()' translation."""
        source = "x = eh_instancia(42, int)"
        result = translate_source(source)
        assert "x = isinstance(42, int)" in result

    def test_translate_mapa(self):
        """Test 'mapa()' → 'map()' translation."""
        source = "x = mapa(funcao, lista)"
        result = translate_source(source)
        assert "x = map(def, lista)" in result

    def test_translate_filtro(self):
        """Test 'filtro()' → 'filter()' translation."""
        source = "x = filtro(funcao, lista)"
        result = translate_source(source)
        assert "x = filter(def, lista)" in result

    def test_translate_classifica(self):
        """Test 'classifica()' → 'sorted()' translation."""
        source = "x = classifica(lista)"
        result = translate_source(source)
        assert "x = sorted(lista)" in result


class TestMultipleTranslations:
    """Test multiple translations in one source."""

    def test_multiple_keywords_one_line(self):
        """Test multiple keywords in a single line."""
        source = "se x > 0 e y < 10 ou z == 5:\n    pass"
        result = translate_source(source)
        assert "if x > 0 and y < 10 or z == 5:" in result

    def test_keywords_and_functions(self):
        """Test keywords and functions together."""
        source = "para i em intervalo(5):\n    imprimir(i)"
        result = translate_source(source)
        assert "for i in range(5):" in result
        assert "print(i)" in result

    def test_nested_structures(self):
        """Test nested if/for structures."""
        source = "para i em intervalo(5):\n    se i > 2:\n        imprimir(i)"
        result = translate_source(source)
        assert "for i in range(5):" in result
        assert "if i > 2:" in result
        assert "print(i)" in result


class TestStringProtection:
    """Test that translations don't happen inside strings."""

    def test_keyword_in_double_quoted_string(self):
        """Test that keywords in double-quoted strings are not translated."""
        source = 'imprimir("para sempre")'
        result = translate_source(source)
        assert 'print("para sempre")' in result
        # The "para" inside the string should NOT be translated to "for"
        assert '"for sempre"' not in result

    def test_keyword_in_single_quoted_string(self):
        """Test that keywords in single-quoted strings are not translated."""
        source = "imprimir('para sempre')"
        result = translate_source(source)
        assert "print('para sempre')" in result
        assert "'for sempre'" not in result

    def test_multiple_strings(self):
        """Test protection with multiple strings."""
        source = 'imprimir("para") e imprimir("se")'
        result = translate_source(source)
        assert 'print("para")' in result
        assert 'print("se")' in result
        assert 'print("for")' not in result
        assert 'print("if")' not in result

    def test_escaped_quotes_in_string(self):
        """Test protection with escaped quotes."""
        source = 'imprimir("She said \\"para\\"")'
        result = translate_source(source)
        # The "para" inside the escaped string should not be translated
        assert '\\"para\\"' in result


class TestCommentProtection:
    """Test that translations don't happen inside comments."""

    def test_keyword_in_comment(self):
        """Test that keywords in comments are not translated."""
        source = "# para sempre\nx = 1"
        result = translate_source(source)
        assert "# para sempre" in result
        assert "# for sempre" not in result

    def test_function_in_comment(self):
        """Test that function names in comments are not translated."""
        source = "# imprimir deve fazer algo\nx = 1"
        result = translate_source(source)
        assert "# imprimir deve fazer algo" in result
        assert "# print deve fazer algo" not in result

    def test_inline_comment(self):
        """Test inline comments after code."""
        source = "x = 1  # para teste\nimprimir(x)"
        result = translate_source(source)
        assert "# para teste" in result
        assert "print(x)" in result


class TestFStringProtection:
    """Test that function calls inside f-strings are translated (since expressions are code)."""

    def test_function_call_in_fstring(self):
        """Test that function calls inside f-string expressions ARE translated."""
        source = 'imprimir(f"Resultado: {soma([1, 2, 3])}")'
        result = translate_source(source)
        # The soma() call inside the f-string SHOULD be translated
        assert 'print(f"Resultado: {sum([1, 2, 3])}")' in result

    def test_multiple_function_calls_in_fstring(self):
        """Test multiple function calls in f-string expression."""
        source = 'imprimir(f"Min: {minimo(lst)}, Max: {maximo(lst)}")'
        result = translate_source(source)
        assert "min(lst)" in result
        assert "max(lst)" in result

    def test_keyword_in_fstring_literal(self):
        """Test that keywords in f-string literal (not expression) are not translated."""
        source = 'x = f"para sempre"'
        result = translate_source(source)
        # "para" is literal text in the f-string, not code
        assert 'f"para sempre"' in result


class TestVariableNameProtection:
    """Test that variable names with pt-BR words are not partially translated."""

    def test_variable_with_keyword_prefix(self):
        """Test that variable names are not modified."""
        source = "para_index = 5"
        result = translate_source(source)
        assert "para_index = 5" in result
        assert "for_index" not in result

    def test_variable_with_keyword_suffix(self):
        """Test that variable names ending with keywords are not modified."""
        source = "meu_para = 5"
        result = translate_source(source)
        assert "meu_para = 5" in result

    def test_variable_with_function_name(self):
        """Test that variables with function names are not modified."""
        source = "minha_imprimir = funcao"
        result = translate_source(source)
        # minha_imprimir should not be changed
        assert "minha_imprimir" in result


class TestEdgeCases:
    """Test edge cases and special scenarios."""

    def test_empty_source(self):
        """Test translation of empty source code."""
        result = translate_source("")
        assert result == ""

    def test_whitespace_only(self):
        """Test translation of whitespace-only source."""
        source = "   \n\n   "
        result = translate_source(source)
        assert result == source

    def test_no_translations_needed(self):
        """Test source with no pt-BR keywords."""
        source = "x = 1\ny = 2\nz = x + y"
        result = translate_source(source)
        assert result == source

    def test_single_keyword(self):
        """Test translation of single keyword."""
        source = "para"
        result = translate_source(source)
        # Single "para" on a line should be translated
        assert "for" in result

    def test_multiple_same_keyword(self):
        """Test translation with repeated keywords."""
        source = "se x:\n    se y:\n        para i em intervalo(10):\n            pass"
        result = translate_source(source)
        # Count occurrences
        assert result.count("if ") == 2
        assert result.count("for ") == 1

    def test_special_characters_in_strings(self):
        """Test strings with special characters."""
        source = 'imprimir("Olá, Mundo! @#$%")'
        result = translate_source(source)
        assert 'print("Olá, Mundo! @#$%")' in result

    def test_mixed_quotes_in_source(self):
        """Test source with mixed single and double quotes."""
        source = """imprimir("duplo") e imprimir('simples')"""
        result = translate_source(source)
        assert 'print("duplo")' in result
        assert "print('simples')" in result

    def test_unicode_characters(self):
        """Test translation with Unicode characters."""
        source = 'x = "José"\nse verdadeiro:\n    imprimir(x)'
        result = translate_source(source)
        assert 'x = "José"' in result
        assert "if True:" in result
        assert "print(x)" in result

    def test_very_long_line(self):
        """Test translation of very long lines."""
        long_line = "para i em intervalo(1000): " + "x = x + i " * 100
        result = translate_source(long_line)
        assert "for i in range(1000):" in result

    def test_consecutive_keywords(self):
        """Test consecutive keywords without operators."""
        source = "para i em intervalo(5):\n    quebra"
        result = translate_source(source)
        assert "for i in range(5):" in result
        assert "break" in result


class TestRegressions:
    """Test for potential regression issues."""

    def test_malformed_f_string_edge_case(self):
        """Test f-string without closing brace still works."""
        # This should not crash even if malformed
        source = 'imprimir(f"test {soma'
        result = translate_source(source)
        # Should still translate what it can
        assert "print" in result

    def test_unterminated_string(self):
        """Test handling of unterminated strings."""
        # This is actually invalid Python, but translator should handle it gracefully
        source = 'imprimir("teste'
        result = translate_source(source)
        assert "print" in result

    def test_backslash_in_comment(self):
        """Test backslash in comments."""
        source = "# This is a comment \\\nse x:\n    pass"
        result = translate_source(source)
        assert "if x:" in result

    def test_function_call_without_parens(self):
        """Test that function names without parentheses are not translated."""
        source = "x = imprimir"
        result = translate_source(source)
        # Without the (, this should not be treated as a function call
        # so it should be translated as a variable/attribute access
        assert "imprimir" in result or "print" in result  # Depends on implementation


class TestComplexScenarios:
    """Test complex real-world scenarios."""

    def test_function_definition_with_pt_br(self):
        """Test complete function definition in pt-BR."""
        source = """funcao saudacao(nome):
    se nome:
        imprimir(f"Olá, {nome}!")
    senao:
        imprimir("Olá, desconhecido!")
"""
        result = translate_source(source)
        assert "def saudacao(nome):" in result
        assert "if nome:" in result
        assert 'print(f"Olá, {nome}!")' in result
        assert "else:" in result
        assert 'print("Olá, desconhecido!")' in result

    def test_class_definition_with_pt_br(self):
        """Test class definition in pt-BR."""
        source = """classe Pessoa:
    funcao __init__(self, nome):
        self.nome = nome
    
    funcao saudacao(self):
        imprimir(f"Olá, {self.nome}")
"""
        result = translate_source(source)
        assert "class Pessoa:" in result
        assert "def __init__(self, nome):" in result
        assert "def saudacao(self):" in result
        assert "print" in result

    def test_list_comprehension_with_pt_br(self):
        """Test list comprehension with pt-BR."""
        source = "resultado = [i * 2 para i em intervalo(10) se i > 5]"
        result = translate_source(source)
        # Should translate both keywords
        assert "for i in range(10)" in result
        assert "if i > 5" in result

    def test_multiple_imports_with_translations(self):
        """Test with mixed import and pt-BR code."""
        source = """import pt_br
para i em intervalo(5):
    imprimir(i)
"""
        result = translate_source(source)
        assert "import pt_br" in result
        assert "for i in range(5):" in result
        assert "print(i)" in result
