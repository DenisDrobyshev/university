num1, num2, num3 = int(input()), int(input()), int(input())
if num1 == num2 == num3:
    print(3)
elif num1 == num2 or num1 == num3 or num2 == num3:
    print(2)
else:
    print(0)