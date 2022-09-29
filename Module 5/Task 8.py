num = int(input())
num_max = num1 = 0

while num != 0:
    num0 = int(input())
    if num == num0:
        num1 += 1
        if num1>num_max:
            num_max = num1
    else:
        num1 = 0
    num = num0
print(num_max + 1)