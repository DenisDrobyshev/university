import random

count: int = 0
lives: int = 3

print('''
Вам предстоит сыграть в игру. 
Правила просты: Вам нужно выбрать математическую операцию, затем компьютер сгенерирует пример, на который Вам нужно дать правильный ответ.
На это у Вас есть в наличии 3 жизни. 
С каждым неправильным ответом жизни убавляются. 
В конце счетчик выдаст Вам количество правильно решенных примеров.
''')

print('Выберите операцию и напишите правильный ответ!')

print('Список операций: Сложение, Вычитание, Деление, Умножение, Степень')

sumi1: str = 'Сложение'
razn1: str = 'Вычитание'
delen1: str = 'Деление'
umnozh1: str = 'Умножение'
stepen1: str = 'Степень'

while lives > 0:
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    choice = input('Введите операцию: ')

    sumi = a + b
    razn = a - b
    delen = a // b
    umnozh = a * b
    stepen = a ** b

    if choice == sumi1:
        answ = float(input(f'Введите ответ: {a} + {b} = '))
        if answ == sumi:
            print('Правильный ответ!')
            count += 1
        else:
            lives -= 1
            print(f'Неправильный ответ! Жизней: {lives}')

    elif choice == razn1:
        answ = float(input(f'Введите ответ: {a} - {b} = '))
        if answ == razn:
            print('Правильный ответ!')
            count += 1
        else:
            lives -= 1
            print(f'Неправильный ответ! Жизней: {lives}')

    elif choice == delen1:
        answ = float(input(f'Введите ответ: {a} // {b} = '))
        if answ == delen:
            print('Правильный ответ!')
            count += 1
        else:
            lives -= 1
            print(f'Неправильный ответ! Жизней: {lives}')

    elif choice == umnozh1:
        answ = float(input(f'Введите ответ: {a} * {b} = '))
        if answ == umnozh:
            print('Правильный ответ!')
            count += 1
        else:
            lives -= 1
            print(f'Неправильный ответ! Жизней: {lives}')

    elif choice == stepen1:
        answ = float(input(f'Введите ответ: {a} ^ {b} = '))
        if answ == stepen:
            print('Правильный ответ!')
            count += 1
        else:
            lives -= 1
            print(f'Неправильный ответ! Жизней: {lives}')

    else:
        print('Недопустимая операция! Введите еще раз.')


print(f'Игра закончилась! Жизни кончились. Правильно решенных примеров: {count}.')