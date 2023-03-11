def collats(number: int) -> list[int]:
    '''
    Гипотеза коллатса заключается в том, что для любого сколь угодно большого числа
    если применять к нему алгоритм (подели на 2 если четное или умножь на 3 и прибавь 1 если нечетное)
    получится цикл сводящийся к комбинации 1 2 4.
    Данная функция наглядно показывает что это так.

    :param number: число, для которого применяет алгоритм.
    :return: список чисел, полученный путем применения к числу алгоритма.
    '''
    numbers: list[int] = [number]
    if number < 1:
        return []
    while number > 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        numbers.append(number)
    return numbers


print(collats(int(input("Введите число: "))))
