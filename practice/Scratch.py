from CalculatorGrad import deg_to_gms

def create_list(*args, **kwargs):
    ls = {}

    for i in range(0, len(args)):
        ls[f'Point_{i}'] = deg_to_gms(args[i])
    for k, w in kwargs.items():    # возвращает (ключ(k), значение(w))
        w = deg_to_gms(w)
        ls[k] = w
    return ls
print(create_list(172.25899161, 321.42304971, 12.697987681352, pole=21.89617856, put_1=140.85706440))
