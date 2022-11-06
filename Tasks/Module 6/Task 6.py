ls1 = [int(i) for i in input('Введите числа: ').split()]
ls2 = [int(i) for i in input('Введите числа: ').split()]

ls3 = []
for i in ls1:
    for j in ls2:
        if i == j:
            ls3.append(i)
            break
print(f'Повторяющиеся элементы: {ls3}')