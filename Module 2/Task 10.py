a = int(input())    # Ученики
b = int(input())
c = int(input())

a1 = a // 2    # Столы для учеников
b1 = b // 2
c1 = c // 2

print(a1 + b1 + c1 + a % 2 + b % 2 + c % 2)


