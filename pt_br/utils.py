"""Utility functions for pt-BR translation.

This module provides helper functions for the translator:
- Context detection (strings, comments, etc.)
- Safe word replacement
- Debug utilities
"""

import re
from typing import Tuple


def is_inside_string(source: str, position: int) -> bool:
    """Check if a position is inside a string literal.

    Detects if the given position falls within a string delimited by
    single quotes (') or double quotes (").

    Args:
        source: The source code string
        position: The character position to check

    Returns:
        True if position is inside a string literal, False otherwise
    """
    # Track whether we're inside a string and what quote char started it
    in_string = False
    string_char = None
    i = 0

    while i < position and i < len(source):
        char = source[i]

        # Handle escape sequences (skip next character)
        if in_string and char == "\\" and i + 1 < len(source):
            i += 2
            continue

        # Toggle string state if we encounter a quote
        if char in ("'", '"'):
            if not in_string:
                in_string = True
                string_char = char
            elif char == string_char:
                in_string = False
                string_char = None

        i += 1

    return in_string


def is_inside_comment(source: str, position: int) -> bool:
    """Check if a position is inside a comment.

    Detects if the given position falls within a comment (anything after '#').

    Args:
        source: The source code string
        position: The character position to check

    Returns:
        True if position is inside a comment, False otherwise
    """
    # Find the last newline before position
    last_newline = source.rfind("\n", 0, position)
    line_start = last_newline + 1 if last_newline != -1 else 0

    # Find the first '#' on this line
    hash_pos = source.find("#", line_start, position)

    # If we found a '#' before our position, we're in a comment
    # (but make sure the '#' is not inside a string)
    if hash_pos != -1 and hash_pos < position:
        # Make sure the '#' itself is not in a string
        if not is_inside_string(source, hash_pos):
            return True

    return False


def is_word_boundary(source: str, position: int) -> bool:
    """Check if a position is at a word boundary.

    A word boundary is where a word character transitions to a non-word character
    or vice versa. Used to avoid replacing partial words.

    Args:
        source: The source code string
        position: The character position to check

    Returns:
        True if position is at a word boundary, False otherwise
    """
    if position < 0 or position >= len(source):
        return True

    # Check character at position and before/after
    is_word_char = lambda ch: ch.isalnum() or ch == "_"

    at_position = is_word_char(source[position])
    before = is_word_char(source[position - 1]) if position > 0 else False
    after = is_word_char(source[position + 1]) if position < len(source) - 1 else False

    # It's a boundary if the current char is different from its neighbors
    return (not before) or (not after)


def safe_replace_word(
    source: str,
    old: str,
    new: str,
    avoid_strings: bool = True,
    avoid_comments: bool = True,
) -> str:
    """Safely replace a word in source code.

    Replaces all occurrences of 'old' with 'new', respecting word boundaries
    and optionally avoiding strings and comments.

    Args:
        source: The source code string
        old: The word to replace
        new: The replacement word
        avoid_strings: If True, don't replace inside strings
        avoid_comments: If True, don't replace inside comments

    Returns:
        The source code with replacements made
    """
    # Use regex with word boundaries
    pattern = r"\b" + re.escape(old) + r"\b"

    def replacer(match):
        pos = match.start()

        # Check if we should skip this match
        if avoid_strings and is_inside_string(source, pos):
            return match.group()
        if avoid_comments and is_inside_comment(source, pos):
            return match.group()

        return new

    return re.sub(pattern, replacer, source)


def safe_replace_function(source: str, old: str, new: str) -> str:
    """Safely replace a function name in source code.

    Replaces function names (detects by opening parenthesis) while respecting
    word boundaries and avoiding strings/comments.

    Note: This function WILL translate function calls inside f-strings because
    those are executable Python expressions, not string literals.

    Args:
        source: The source code string
        old: The function name to replace
        new: The replacement function name

    Returns:
        The source code with replacements made
    """
    # Pattern: word boundary, function name, opening paren
    pattern = r"\b" + re.escape(old) + r"(?=\()"

    def replacer(match):
        pos = match.start()

        # Don't replace if inside a comment
        if is_inside_comment(source, pos):
            return match.group()

        # Special handling for f-strings: we DO want to replace inside f-strings
        # because the expressions inside {} are Python code, not string content
        if is_inside_string(source, pos):
            # Check if this is an f-string by looking backwards for 'f"' or "f'"
            # Find the start of this string by scanning backwards
            quote_pos = pos - 1
            while quote_pos >= 0 and source[quote_pos] not in ('"', "'"):
                quote_pos -= 1

            # Check if there's an 'f' before the quote
            if quote_pos > 0 and source[quote_pos - 1] in ("f", "F"):
                # It's an f-string, so we DO translate (expressions in {} are code)
                return new
            else:
                # Regular string, don't translate
                return match.group()

        return new

    return re.sub(pattern, replacer, source)


def debug_show_translation(pt_br_code: str, python_code: str) -> None:
    """Display side-by-side comparison of pt-BR and Python code.

    Useful for debugging and verifying translations are correct.

    Args:
        pt_br_code: The original pt-BR source code
        python_code: The translated Python source code
    """
    pt_br_lines = pt_br_code.split("\n")
    python_lines = python_code.split("\n")

    print("=" * 100)
    print("TRANSLATION DEBUG VIEW")
    print("=" * 100)

    # Show side-by-side (Python's max line length ~80, so we use ~40 per side)
    max_lines = max(len(pt_br_lines), len(python_lines))

    print(f"{'PT-BR':<45} | {'Python':<50}")
    print("-" * 100)

    for i in range(max_lines):
        pt_br = pt_br_lines[i] if i < len(pt_br_lines) else ""
        py = python_lines[i] if i < len(python_lines) else ""

        # Truncate long lines for display
        pt_br = pt_br[:42] + "..." if len(pt_br) > 45 else pt_br
        py = py[:47] + "..." if len(py) > 50 else py

        print(f"{pt_br:<45} | {py:<50}")

    print("=" * 100)


def count_translations(source: str) -> Tuple[int, int]:
    """Count how many keywords and functions are in source code.

    This is a rough estimate - actual translation depends on context.

    Args:
        source: The source code string

    Returns:
        Tuple of (keywords_found, functions_found)
    """
    from .mappings import PT_BR_KEYWORDS, PT_BR_BUILTINS

    keywords_found = 0
    functions_found = 0

    for keyword in PT_BR_KEYWORDS:
        keywords_found += len(re.findall(r"\b" + keyword + r"\b", source))

    for func in PT_BR_BUILTINS:
        functions_found += len(re.findall(r"\b" + func + r"(?=\()", source))

    return keywords_found, functions_found
