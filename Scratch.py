from CalculatorGrad import deg_to_gms

def create_list(*args, **kwargs):
    ls = []

    for a, b in enumerate(args):    # Вернет кортеж вида ('счетчик', 'элемент'), пронумеруем элементы a по индексам
        ls.append(f'Point_{a} = {deg_to_gms(b)}')
    for k, w in kwargs.items():    # возвращает (ключ(k), значение(w))
        ls.append(f'{k} = {deg_to_gms(w)}')
    return ls
print(create_list(172.25899161, 321.42304971, 12.697987681352, pole=21.89617856, put_1=140.85706440))
print(dir())