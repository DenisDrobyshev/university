import random

lock_sym: str = '\u25A0'
love_sym: str = '\u2764'
session_record: int = 0
record: int = 0
words_list: list = []

with open('/Users/denis.drobyshev/Desktop/project_1/General_practice/WheelOfFortune/words_file') as hm:
    words_list = hm.read().splitlines()

with open('/Users/denis.drobyshev/Desktop/project_1/General_practice/WheelOfFortune/record_file') as hm:
    record = int(hm.read())
def new_record():
    """
    функция делает обновление текущего рекорда
    """
    with open('record_file', mode='w') as hm:
        hm.write(str(record))

def build_random_word():
    """
    :return: случайное уникальное слово из всех слов
    """
    word = random.choice(words_list)
    words_list.remove(word)
    return word
