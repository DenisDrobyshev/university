ls = [int(i) for i in input('Введите числа: ').split()]

view = set()    # Создаем набор

for l in ls:
    if l in view:
        print("ДА")
    else:
        print("НЕТ")
        view.add(l)    # Добавляем l в набор view


print(view)