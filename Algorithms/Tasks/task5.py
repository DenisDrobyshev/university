# Определить наименьшее расстояние между двумя локальными макс. последовательности нат. чисел
# если таких максимумов нет то выводим 0
# расстоянием считаем количество пробелов между максимумами
# 3 5 8 6 9

s = []
n = int(input())
index = []
while n != 0:
    s.append(n)
    n = int(input())
count = len(s)
for i in range(1, len(s)):
    if s[i - 1] < s[i] > s[i + 1]:
        index.append(i)
for i in range(1, len(index)):
    if count > index[i] - index[i - 1]:
        count = index[i] - index[i - 1]
print(index, count)
