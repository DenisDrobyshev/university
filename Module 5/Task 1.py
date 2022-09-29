num = int(input('Введите число: '))
num1 = 1
while num1 <= num:
    num1 += 1
    if num % num1 == 0:
        print(f'Наименьший делитель: {num1}')
        break









