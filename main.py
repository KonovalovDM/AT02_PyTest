def count_vowels(s):
    """
    Считает количество гласных в строке (поддерживаются латиница и кириллица).
    :param s: входная строка
    :return: количество гласных
    """
    vowels = "aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for char in s if char in vowels)
