n = int(input())
a = b = 1
c = a + b
while c <= n:
    a = b + c
    a, b, c = b, c, a
print(b == n)