ls = [int(i) for i in input('Введите числа: ').split()]

x = ls.index(max(ls))
y = ls.index(min(ls))
ls[x], ls[y] = ls[y], ls[x]
print(*ls)