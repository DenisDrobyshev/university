n = int(input())
lst = [1]
while len(lst) < n:
    f = sum(lst[-2:])
    lst.append(f)
print(*lst)