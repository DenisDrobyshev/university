s = input("Строка: ")
l = len(s)
print(s[l // 2 + l % 2:], s[: l // 2 + l % 2], sep="")