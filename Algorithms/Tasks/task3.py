# вводится последовательность нат. чисел, оканчивающаяся нулем
# напечатать второй по величине элемент массива

num = 1
max2 = 0
max1 = 0

while num != 0:
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
print(max2)


