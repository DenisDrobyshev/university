# Ввести натуральное число и распечатать все квадраты
# натуральных чисел не превосходящих n в порядке возрастания

n = int(input("Введите число: "))
for i in range(1, n):
    if i**2 < n:
        print(i**2)
