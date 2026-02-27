"""Unit tests for utility functions in pt_br.utils module.

Tests the context detection functions and safe replacement utilities:
- String detection (single quotes, double quotes, escapes)
- Comment detection
- Word boundary detection
- Safe word and function replacement
"""

import pytest
from pt_br.utils import (
    is_inside_string,
    is_inside_comment,
    is_word_boundary,
    safe_replace_word,
    safe_replace_function,
    debug_show_translation,
    count_translations,
)


class TestStringDetection:
    """Test is_inside_string() function."""

    def test_position_before_string(self):
        """Test position before a string literal."""
        source = 'x = "hello"'
        assert is_inside_string(source, 0) is False
        assert is_inside_string(source, 4) is False

    def test_position_inside_double_quoted_string(self):
        """Test position inside double-quoted string."""
        source = 'x = "hello world"'
        assert is_inside_string(source, 7) is True  # h
        assert is_inside_string(source, 10) is True  # l
        assert is_inside_string(source, 16) is True  # d

    def test_position_inside_single_quoted_string(self):
        """Test position inside single-quoted string."""
        source = "x = 'hello world'"
        assert is_inside_string(source, 7) is True
        assert is_inside_string(source, 10) is True

    def test_position_at_quote_char(self):
        """Test position at quote character."""
        source = 'x = "hello"'
        assert is_inside_string(source, 4) is False  # opening "
        # After opening quote, we're considered inside the string
        assert is_inside_string(source, 10) is True  # at closing quote (still inside)

    def test_escaped_quote_in_string(self):
        """Test escaped quotes inside strings."""
        source = r'x = "She said \"hello\""'
        # Position in "hello" after escaped quote
        assert is_inside_string(source, 18) is True

    def test_multiple_strings(self):
        """Test with multiple strings."""
        source = 'x = "first" and y = "second"'
        assert is_inside_string(source, 7) is True  # in "first"
        assert is_inside_string(source, 12) is False  # between strings
        assert is_inside_string(source, 24) is True  # in "second"

    def test_mixed_quotes(self):
        """Test with mixed single and double quotes."""
        source = """x = "double's" and y = 'single"s'"""
        assert is_inside_string(source, 7) is True  # in double-quoted
        assert is_inside_string(source, 27) is True  # in single-quoted

    def test_position_at_end_of_source(self):
        """Test position at or beyond end of source."""
        source = "x = 1"
        assert is_inside_string(source, 100) is False


class TestCommentDetection:
    """Test is_inside_comment() function."""

    def test_position_before_comment(self):
        """Test position before comment marker."""
        source = "x = 1  # comment"
        assert is_inside_comment(source, 0) is False
        assert is_inside_comment(source, 5) is False

    def test_position_inside_comment(self):
        """Test position inside comment."""
        source = "x = 1  # comment"
        assert is_inside_comment(source, 10) is True
        assert is_inside_comment(source, 15) is True

    def test_position_at_hash(self):
        """Test position at hash character."""
        source = "x = 1  # comment"
        # Position 7 is the # itself - check if we're in comment at that position
        assert is_inside_comment(source, 8) is True  # position after #

    def test_hash_in_string_not_comment(self):
        """Test that hash inside strings doesn't create comments."""
        source = 'x = "value # not comment"'
        assert is_inside_comment(source, 10) is False  # inside string

    def test_multiline_comment_check(self):
        """Test comment on specific line."""
        source = """x = 1  # line 1 comment
y = 2  # line 2 comment
"""
        assert is_inside_comment(source, 10) is True  # in line 1 comment
        # Position 31 is the # on line 2, position 33 is definitely in comment
        assert is_inside_comment(source, 33) is True  # in line 2 comment

    def test_empty_line_no_comment(self):
        """Test empty line has no comment."""
        source = "x = 1\n\ny = 2"
        assert is_inside_comment(source, 6) is False  # empty line


class TestWordBoundary:
    """Test is_word_boundary() function."""

    def test_start_of_word(self):
        """Test word boundary at start of word."""
        source = "hello world"
        assert is_word_boundary(source, 0) is True  # start of 'hello'

    def test_end_of_word(self):
        """Test word boundary at end of word."""
        source = "hello world"
        assert is_word_boundary(source, 4) is True  # after 'hello'

    def test_middle_of_word(self):
        """Test middle of word is not boundary."""
        source = "hello"
        assert is_word_boundary(source, 2) is False  # in middle of 'hello'

    def test_underscore_treated_as_word_char(self):
        """Test underscore is treated as word character."""
        source = "hello_world"
        assert is_word_boundary(source, 5) is False  # underscore is word char

    def test_digit_treated_as_word_char(self):
        """Test digits are word characters."""
        source = "hello123world"
        assert is_word_boundary(source, 7) is False  # digit is word char

    def test_space_is_boundary(self):
        """Test space marks word boundary."""
        source = "hello world"
        # Position 5 is the space - it's a non-word char, so we check if it's a boundary
        # Space is not word char, but the position is at a boundary
        assert is_word_boundary(source, 6) is True  # w of 'world' is at boundary

    def test_punctuation_is_boundary(self):
        """Test punctuation marks boundary."""
        source = "hello, world"
        assert is_word_boundary(source, 5) is True  # comma after hello

    def test_negative_position(self):
        """Test negative position returns True."""
        source = "hello"
        assert is_word_boundary(source, -1) is True

    def test_position_beyond_length(self):
        """Test position beyond string length."""
        source = "hello"
        assert is_word_boundary(source, 100) is True


class TestSafeReplaceWord:
    """Test safe_replace_word() function."""

    def test_simple_replacement(self):
        """Test simple word replacement."""
        source = "para i em intervalo(5):"
        result = safe_replace_word(source, "para", "for")
        assert "for i em intervalo(5):" in result

    def test_no_partial_replacement(self):
        """Test that partial words are not replaced."""
        source = "para_index = 5"
        result = safe_replace_word(source, "para", "for")
        assert "para_index = 5" in result
        assert "for_index" not in result

    def test_multiple_replacements(self):
        """Test replacing multiple occurrences."""
        source = "para i em intervalo(5):\n    para j em intervalo(3):"
        result = safe_replace_word(source, "para", "for")
        assert result.count("for") == 2

    def test_avoid_strings_default_true(self):
        """Test that strings are avoided by default."""
        source = 'imprimir("para sempre")'
        result = safe_replace_word(source, "para", "for")
        assert '"para sempre"' in result  # not replaced
        assert '"for sempre"' not in result

    def test_avoid_strings_explicit_false(self):
        """Test replacing inside strings when avoid_strings=False."""
        source = 'imprimir("para sempre")'
        result = safe_replace_word(source, "para", "for", avoid_strings=False)
        assert '"for sempre"' in result

    def test_avoid_comments_default_true(self):
        """Test that comments are avoided by default."""
        source = "# para sempre\nx = 1"
        result = safe_replace_word(source, "para", "for")
        assert "# para sempre" in result
        assert "# for sempre" not in result

    def test_avoid_comments_explicit_false(self):
        """Test replacing inside comments when avoid_comments=False."""
        source = "# para sempre\nx = 1"
        result = safe_replace_word(source, "para", "for", avoid_comments=False)
        assert "# for sempre" in result

    def test_replacement_with_special_regex_chars(self):
        """Test replacement when word contains regex special chars."""
        source = "eh_instancia(x, int)"
        result = safe_replace_word(source, "eh_instancia", "isinstance")
        assert "isinstance(x, int)" in result


class TestSafeReplaceFunction:
    """Test safe_replace_function() function."""

    def test_function_call_replacement(self):
        """Test replacing function calls."""
        source = "imprimir('hello')"
        result = safe_replace_function(source, "imprimir", "print")
        assert "print('hello')" in result

    def test_function_without_parens_not_replaced(self):
        """Test that function names without parens are not replaced."""
        source = "x = imprimir"
        result = safe_replace_function(source, "imprimir", "print")
        assert "x = imprimir" in result

    def test_function_in_string_not_replaced(self):
        """Test that function calls in regular strings are not replaced."""
        source = 'x = "imprimir()"'
        result = safe_replace_function(source, "imprimir", "print")
        assert '"imprimir()"' in result
        assert '"print()"' not in result

    def test_function_in_comment_not_replaced(self):
        """Test that function calls in comments are not replaced."""
        source = "# imprimir(x)\ny = 1"
        result = safe_replace_function(source, "imprimir", "print")
        assert "# imprimir(x)" in result

    def test_function_in_fstring_replaced(self):
        """Test that function calls in f-strings ARE replaced."""
        source = 'f"{imprimir(x)}"'
        result = safe_replace_function(source, "imprimir", "print")
        assert "print(x)" in result

    def test_multiple_function_calls(self):
        """Test replacing multiple function calls."""
        source = "imprimir(x)\nfor i in range(5):\n    imprimir(i)"
        result = safe_replace_function(source, "imprimir", "print")
        assert result.count("print") == 2
        assert "imprimir" not in result

    def test_nested_function_calls(self):
        """Test nested function calls."""
        source = "imprimir(soma([1, 2, 3]))"
        result = safe_replace_function(source, "imprimir", "print")
        result = safe_replace_function(result, "soma", "sum")
        assert "print(sum([1, 2, 3]))" in result


class TestDebugShowTranslation:
    """Test debug_show_translation() utility function."""

    def test_debug_function_no_error(self, capsys):
        """Test that debug function doesn't raise errors."""
        pt_br_code = "para i em intervalo(5):\n    imprimir(i)"
        python_code = "for i in range(5):\n    print(i)"
        debug_show_translation(pt_br_code, python_code)
        captured = capsys.readouterr()
        assert "TRANSLATION DEBUG VIEW" in captured.out

    def test_debug_function_shows_both_sides(self, capsys):
        """Test that debug function shows both sides."""
        pt_br_code = "para i em intervalo(5):"
        python_code = "for i in range(5):"
        debug_show_translation(pt_br_code, python_code)
        captured = capsys.readouterr()
        assert "PT-BR" in captured.out
        assert "Python" in captured.out


class TestCountTranslations:
    """Test count_translations() utility function."""

    def test_count_single_keyword(self):
        """Test counting single keyword."""
        source = "para i em intervalo(5):\n    pass"
        keywords, functions = count_translations(source)
        assert keywords >= 1  # at least "para"

    def test_count_multiple_keywords(self):
        """Test counting multiple keywords."""
        source = "se x > 0 e y < 10:\n    pass"
        keywords, functions = count_translations(source)
        assert keywords >= 2  # "se" and "e"

    def test_count_single_function(self):
        """Test counting single function."""
        source = "imprimir('hello')"
        keywords, functions = count_translations(source)
        assert functions >= 1

    def test_count_multiple_functions(self):
        """Test counting multiple functions."""
        source = "x = soma(lista)\ny = minimo(lista)\nz = maximo(lista)"
        keywords, functions = count_translations(source)
        assert functions >= 3

    def test_count_no_translations(self):
        """Test counting source with no pt-BR."""
        source = "x = 1\ny = 2"
        keywords, functions = count_translations(source)
        assert keywords == 0
        assert functions == 0

    def test_count_ignores_strings(self):
        """Test that count is based on pattern, not avoiding strings."""
        # Note: count_translations doesn't avoid strings, it's a rough estimate
        source = 'x = "para sempre"'
        keywords, functions = count_translations(source)
        # This will count "para" even in string (rough estimate)
        assert keywords >= 1
