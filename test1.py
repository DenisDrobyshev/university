def check_parentheses(stroka):
    """
    Функция определяет является ли порядок круглых скобок допустимым или нет
    :param stroka: строка со скобками
    :return: True если допустимый порядок и False если нет
    """
    try:
        count: int = 0
        for i in stroka:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
            else:
                count = 0
            if count < 0:
                return False
        if count:
            return False
        return True
    except NameError:
        print('Ошибка!')
    except TypeError:
        print('Неверный тип данных!')


print(check_parentheses('()'))
print(check_parentheses(')(()))'))
print(check_parentheses('('))
print(check_parentheses(')('))
help(check_parentheses)



