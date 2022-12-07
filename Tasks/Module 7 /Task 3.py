numbers = int(input())
dict = {}
for i in range(0, numbers):
    name, number = input().split(' ')
    if name in dict:
        dict[name] = str(int(number) + int(dict[name]))
    else:
        dict[name] = number

for name, number in sorted(dict.items()):
    print(name + ' ' + number)
