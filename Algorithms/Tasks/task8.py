# в первой строке вводится количество элементов в массиве
# во второй строке вводятся сами эдементы
# выведите те элементы массива которые встречаются в нем только один раз
# их нужно выводить в том порядке как в массиве

nums = []
count_num = int(input())

for i in range(0, count_num):
    nums.append(int(input()))

for i in range(0, len(nums)):
    if nums.count(nums[i]) == 1:
        print(nums[i], end=' ')


