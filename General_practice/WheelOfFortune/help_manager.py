import random

lock_sym = '\u25A0'
love_sym = '\u2764'
session_record = 0
record = 0
words_list = []

with open('/Users/denis.drobyshev/Desktop/project_1/General_practice/WheelOfFortune/words_file') as hm:
    words_list = hm.read().splitlines()

with open('/Users/denis.drobyshev/Desktop/project_1/General_practice/WheelOfFortune/record_file') as hm:
    record = int(hm.read())
def new_record():
    with open('record_file', mode='w') as hm:
        hm.write(str(record))

def build_random_word():
    word = random.choice(words_list)
    words_list.remove(word)
    return word
