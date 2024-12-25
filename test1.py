import unittest
from main import count_vowels  # Предполагается, что функция находится в файле main.py

class TestCountVowels(unittest.TestCase):
    def test_only_vowels(self):
        """Проверяем строку, содержащую только гласные (латиница и кириллица)."""
        self.assertEqual(count_vowels("aeiouy"), 6)
        self.assertEqual(count_vowels("AEIOUY"), 6)
        self.assertEqual(count_vowels("аеёиоуыэюя"), 10)  # Все гласные на кириллице
        self.assertEqual(count_vowels("АЕЁИОУЫЭЮЯ"), 10)  # Гласные на кириллице в верхнем регистре

    def test_no_vowels(self):
        """Проверяем строку, не содержащую гласных."""
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("BCDFG"), 0)
        self.assertEqual(count_vowels("жзхцчшщ"), 0)  # Согласные на кириллице
        self.assertEqual(count_vowels("ЖЗХЦЧШЩ"), 0)  # Согласные на кириллице в верхнем регистре

    def test_mixed_case(self):
        """Проверяем строку со смешанными символами (буквы, цифры, пробелы, латиница и кириллица)."""
        self.assertEqual(count_vowels("Hello Мир"), 3)  # e, o, и
        self.assertEqual(count_vowels("Привет World"), 3)  # и, е, o
        self.assertEqual(count_vowels("Python 3.12 Программирование"), 9)  # y, o, о, а, и, о, а, и, е
        self.assertEqual(count_vowels("A quick рыжий fox"), 6)  # A, u, i, y, и, o

if __name__ == '__main__':
    unittest.main()
