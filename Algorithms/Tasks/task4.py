# Дана последовательность нат. чисел завершающ. нулем
# определить какое наибольшее число подряд идущих элементов
# этой последовательности равны друг другу

count = 1
max_count = 0
num = None
lst = []
while num != 0:
    num = int(input())
    lst.append(num)

for i in range(1, len(lst)):
    if lst[i] == lst[i-1]:
        count += 1
    else:
        max_count = max(max_count, count)
        count = 1
print(max_count)