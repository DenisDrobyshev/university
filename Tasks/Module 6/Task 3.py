ls = [int(i) for i in input('Введите числа: ').split()]

for i in range(0, len(ls)-1, 2):
    ls[i], ls[i+1] = ls[i+1], ls[i]

print(*ls)