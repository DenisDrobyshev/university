def get_NOD(a, b) -> int:
    """
    Вычисляется НОД для натуральных чисел a и b по алгоритму Евклида
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def get_nod(a, b):
    """
    Вычисляется НОД для натуральных чисел a и b по БЫСТРОМУ алгоритму Евклида
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a










# def test_NOD(func):
#     # --- тест №1 ---
#     a = 28
#     b = 35
#     res = func(a, b)
#     if res == 7:
#         print('тест №1 пройден')
#     else:
#         print('тест №1 не пройден')
#
# test_NOD(get_NOD)
