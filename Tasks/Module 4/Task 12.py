month = int(input('Введите номер месяца: '))
day = int(input('Введите номер дня: '))
year = 2022
if (1 <= month <= 12) and (1 <= day <= 31):
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and (day == 31):
        print(f'1 - {month+1} - {year}')
    elif month == 12 and day == 31:
        print(f'1 - {month-11} - {year+1}')
    elif month == 2 and day == 28:
        print(f'1 - {month+1} - {year}')
    elif (month == 4 or month == 6 or month == 9 or month == 11) and (day == 30):
        print(f'1 - {month+1} - {year}')
    else:
        print(f'{day+1} - {month} - {year}')
else:
    print('Ошибка! Введите корректные данные.')



