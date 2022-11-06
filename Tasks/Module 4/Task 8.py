print('Введите номер месяца и вам отобразится количество дней в нем.')
num = int(input())
if 1 <= num <= 12:
    if num == 1 or num == 3 or num == 5 or num == 7 or num == 8 or num == 10 or num == 12:
        print(31)
    elif num == 2:
        print(28)
    elif num == 4 or num == 6 or num == 9 or num == 11:
        print(30)
else:
    print('Недопустимый диапазон')