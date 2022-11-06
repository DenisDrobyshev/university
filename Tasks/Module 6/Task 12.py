s = input("Строка: ")
first = s.find("h")
last = s.rfind("h")
new_s = list(s.replace("h", "H"))
new_s[first], new_s[last] = "h", "h"
print("".join(new_s))