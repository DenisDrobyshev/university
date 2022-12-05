# Подробно о регулярных выражениях: https://clck.ru/H3xmB
# Отладка https://regex101.com

# Основы:
# . - любой одиночный символ
# [ ] - любой из них, диапазоны
# $ - конец строки
# ^ - начало строки
# \ - экранирование
# \d - любую цифру
# \D - все что угодно, кроме цифр
# \s - пробелы
# \S - все кроме пробелов
# \w - буква
# \W - все кроме букв
# \b - граница слова
# \B - не граница
#
# Квантификация
# n{4} - искать n подряд 4 раза
# n{4,6} - искать n от 4 до 6
# * от нуля и выше
# + от 1 и выше
# ? - нуль или 1 раз


# import re
# string = r"s@dsfg.ty sa32@mail.com \nas_wer@ya.ua as_wer@ya/ua"
# pattern = r"\b[A-Za-z0-9\._-]+@[A-z0-9]+\.[A-z]+"
# match = re.findall(pattern, string)

import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
tel_nums = urllib.request.urlopen("https://www.summet.com/dmsi/html/codesamples/addresses.html").read().decode()
print(tel_nums)


# match = pattern.findall(tel_nums)
# print(match)

#
#
# pattern = r"(?:<li>)(?P<names>[^<]*)(?:<[^>]*>)(?P<street>[^<]*)(?:<[^>]*>)(?P<state>[^<]*)(?:<[^>]*>)(?P<numbers>[^<]*)"

# name_pattern = r"(?:(?:<li>)(\w+ \w+\b[^<]*))
# street_pattern = r"(?:>)((?:P.O.|Ap|\d+)[^<]*)"
# state_pattern = r"(?:/>)([^(?:P.O.|Ap|\d+)][^<]*)"
# or
# state_pattern = r"((?:[^>]*)(?:\b[\d]{5}\b))"
# num_pattern = r"(\(\d{3}\) \d{3}-\d{4})"

# match = re.findall(pattern, tel_nums)
# match = re.finditer(pattern, tel_nums)

# match = ["".join(x) for x in pattern.findall(tel_nums)]

#
# response = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry").read().decode()
# print(response)
# pattern = r"(?:class=\"org-widget\-header__title-link\">[^\w]*|<span class=\"org-widget\-header__meta org-widget\-header__meta\--location\">[^\w]*|<dt class=\"spec__index\"><span class=\"spec__index-inner\">Телефон</span></dt>\n*\s*<dd class=\"spec__value\">[^\w]*|<dt class=\"spec__index\"><span class=\"spec__index-inner\">Часы работы</span></dt>\n*\s*<dd class=\"spec__value\"[^\w]*>)(?P<value>[^<]*\b)"
# match = re.findall(pattern, response)
# match = [match[i:i+4] for i in range(0, len(match), 4)]
# print(match)
