ls = [int(i) for i in input('Введите числа: ').split()]
ls1 = []

for i in range(len(ls)-1):
    if ls[i] < ls[i+1]:
        ls1.append(ls[i+1])
print(*ls1)
