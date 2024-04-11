# дан список упорядоченных по неубыванию элементов в нем
# список запрашивается с клавиатуры
# определить сколько в нем различных элементов


data = set()
while True:
    number = int(input())
    if number == 0:
        break
    else:
        data.add(number)
print(len(data))