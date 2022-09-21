import random

count = 0
lives = 3

while lives > 0:
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    sumi = a + b

    answ = int(input(f'Введите ответ: {a} + {b} = '))
    if answ == sumi:
        print('Правильный ответ!')
        count += 1
    else:
        lives -= 1
        print(f'Неправильный ответ! Жизней: {lives}')

print(f'Игра закончилась! Жизни кончились. Правильно решенных примеров {count}.')