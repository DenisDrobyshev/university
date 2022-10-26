# объявление функции
def get_month(language, number):
    ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru':
        return ru[number-1]
    elif language == 'en':
        return en[number-1]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))