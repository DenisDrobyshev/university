
ls1 = [int(i) for i in input('Введите числа: ').split()]
ls2 = [int(i) for i in input('Введите числа: ').split()]
# count = len([i for i in zip(ls1, ls2) if i[0] == i[1]])
# print(f'Количество совпадающих: {count}')
# print(list(zip(ls1, ls2)))
k = 0
ls3 = []
for i in ls1:
    for j in ls2:
        if i == j:
            ls3.append(i)
            k += 1
            break
print(f'Количество совпадающих: {k}')