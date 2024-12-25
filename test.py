import pytest
from main import count_vowels  # Предполагается, что функция находится в файле main.py

def test_only_vowels_latin():
    """Проверяем строку, содержащую только гласные на латинице."""
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5

def test_only_vowels_cyrillic():
    """Проверяем строку, содержащую только гласные на кириллице."""
    assert count_vowels("аеёиоуыэюя") == 10
    assert count_vowels("АЕЁИОУЫЭЮЯ") == 10

def test_no_vowels():
    """Проверяем строку, не содержащую гласных."""
    assert count_vowels("bcdfg") == 0
    assert count_vowels("BCDFG") == 0
    assert count_vowels("бвгд") == 0
    assert count_vowels("БВГД") == 0

def test_mixed_case():
    """Проверяем строку со смешанными символами."""
    # Слово "Hello" на латинице: 2 гласные (e, o). Слово "Мир" на кириллице: 1 гласная (и).
    assert count_vowels("Hello Мир") == 3  # e, o, и

    # Слово "Привет" на кириллице: 2 гласные (и, е). Слово "World" на латинице: 1 гласная (o).
    assert count_vowels("Привет World") == 3  # и, е, o

    # Слово "Python" на латинице: 2 гласные (y, o). Слово "Программирование" на кириллице: 7 гласных (о, а, и, о, а, и, е).
    # Число "3.12" не содержит гласных.
    assert count_vowels("Python 3.12 Программирование") == 9  # y, o, о, а, и, о, а, и, е

