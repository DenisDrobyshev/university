year = int(input())
vek = year // 100
if (year % 100) > 0:
    print(vek + 1)
else:
    print(vek)
