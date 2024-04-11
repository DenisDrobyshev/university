# переставьте все элементы массива попарно между собой
# если длина последовательности нечетная то выводится последний элемент массива

def example1():
    lst = []
    n = int(input())
    while n != 0:
        lst.append(n)
        n = int(input())

    k = 0
    for i in range(0, len(lst), 2):
        try:
            k = lst[i]
            lst[i] = lst[i + 1]
            lst[i + 1] = k
        except:
            print(lst[i])
    print(*lst)


# --------------------------------------------------------------

def example2():
    nums = []
    reverse_nums = []

    while True:
        num = int(input())

        if num == 0:
            break
        nums.append(num)

    for i in range(0, len(nums)):
        if i % 2 == 0 and i != len(nums) - 1:
            reverse_nums.append(nums[i + 1])
            reverse_nums.append(nums[i])
        elif i == len(nums) - 1 and len(nums) % 2 != 0:
            reverse_nums.append(i + 1)
    print(reverse_nums)


example1()
