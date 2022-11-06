num = int(input())
num1 = num // 100   # Первая цифра числа
num2 = (num // 10) % 10    # Вторая цифра числа
num3 = num % 10    # Третья цифра числа
if num1 < num2 < num3:
    print('Да')
else:
    print('Нет')