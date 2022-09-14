num = int(input())
num1 = num // 100
num2 = (num // 10) % 10
num3 = num % 10
print(num1 + num2 + num3)


#   Второй способ
#   num = input()
#   print(sum(map(int, (str(num)))))