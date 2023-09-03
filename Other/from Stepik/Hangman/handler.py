import random


def wordConverter() -> list:
    words_list = []
    with open("word_rus.txt", mode="r", encoding="UTF-8") as file:
        for line in file:
            words_list.append(line.strip())
    return words_list


def get_word(words_list) -> str:
    result = random.choice(words_list).upper()
    return result


def display_hangman(tries):
    stages = [
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / \
        |
        |  ПИЗДЕЦ!

        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / 
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |     |
        |     |
        |     
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    
        |     
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     
        |    
        |       
        |  
        '''
    ]
    return stages[tries]


def print_word(word_, list_):
    for letter in word_:
        if letter in list_:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()











