a, b = map(int, input().split())

tp = tuple(i**2 for i in range(a, b+1) if a < b)
print(tp)

