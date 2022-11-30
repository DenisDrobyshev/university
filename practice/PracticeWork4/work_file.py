from ctypes import Union
def read_file(name) -> list:
    """
    Считывает текст и возвращает список уникальных слов в нижнем регистре
    :param name: имя файла с текстом, где нужно считать слова
    :return: список уникальных слов в нижнем регистре
    """
    with open(name, 'r') as rf:
        words = rf.read().split()   # Преобразовываем в список
    for i in range(len(words)):
        words[i] = words[i].lower()   # Приводим к нижнему регистру
        words[i] = ''.join(j for j in words[i] if j.isalpha())   # Собираем строку с проверкой на символы
    for word in words:
        if word == '' or len(word) == 1:
            words.remove(word)   # Удаляем элемент состоящий состоящий только из символов или одиночную букву
    words = set(words)   # Создаем множество дабы избавиться от дубликатов
    return list(words)   # Возвращаем список без дубликатов
def save_file(name: str, words: list) -> None:
    """
    Записывает в файл список отсортированных по алфавиту уникальных слов в нижнем регистре
    :param name: имя файла, куда нужно записать слова
    :param words: список уникальных слов в нижнем регистре
    """
    words = sorted(words)
    with open('outread_file.txt', 'w') as sf:
        sf.write(f'Количество уникальных слов: {str(len(words))}\n')
        sf.write('\n'.join(words))

save_file('outread_file.txt', read_file('read_file.txt'))