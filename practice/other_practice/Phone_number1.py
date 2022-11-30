from ctypes import Union

phone_book: Union(dict, set) = {}

def get_num() -> str:
    """
    :return: номер в правильном формате
    """
    number = input('Введите номер: ')
    number = number.replace(' ', '').replace('-', '')

    if number[:2] == '+7' and len(number) == 12:
        return number
    if number[0] == '8' and len(number) == 11:
        number = number.replace('8', '+7', 1)
        return number
    if number[0] == '9' and len(number) == 10:
        number = '+7' + number
        return number

    return '0'

def get_name() -> str:
    """
    :return: имя в правильном формате
    """
    name = input('Введите имя контакта: \n')
    name.lower()

    name_surname = name.split(' ')
    for i in range(0, len(name_surname)):
        name_surname[i] = name_surname[i].capitalize()

    name = ' '.join(name_surname)

    return name

def add_contact(name: str, number: str) -> None:
    """
    Добавляет новый контакт в записную книжку
    :param name: имя контакта
    :param number: номер контакта
    """
    if number != '0':
        print(number, name)
        phone_book[name] = number
        print('Добавлено')
    else:
        print('Неправильно набран номер')

def remove_contact(name: str):
    """
    Удаляет контакт из записной по имени
    :param name: имя контакта
    """
    print(phone_book.pop(name, 'Такого контакта в книге нет'))
    print('Удалено')

def change_contact(name: str, number: str) -> None:
    """
    Изменяет данные существующего контакта
    :param name: имя контакта
    :param number: номер контакта
    """
    if name in phone_book:
        phone_book[name] = number
    else:
        print('Такого контакта в книге нет')

def show_contacts() -> None:
    """
    Показывает все контакты в книге
    """
    for i in phone_book:
        print(i + ' ' + phone_book[i])

while True:
    print('1 - Добавить контакт \n2 - Удалить контакт (по имени) '
          '\n3 - Просмотреть телефонную книгу \n4 - Изменить номер телефона (по имени) \n5 - Выход')

    command: int = int(input('Введите команду: '))

    if command == 1:
        add_contact(get_name(), get_num())
    elif command == 2:
        remove_contact(get_name())
    elif command == 3:
        show_contacts()
    elif command == 4:
        change_contact(get_name(), get_num())
    elif command == 5:
        break
    else:
        print('Неверная команда')