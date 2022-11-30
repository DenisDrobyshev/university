import help_manager as hm
import difficulty_level as dl
import word_combination as wc

def winner() -> None:
    """
    Функция засчитывает победу
    """
    print('Победитель! Призы в студию!')
    hm.session_record += 1

    if hm.session_record > hm.record:
        print('Это ваш новый рекорд угаданных подряд слов: ' + str(hm.session_record))
        hm.record = hm.session_record
        hm.new_record()

def start_game() -> None:
    """
    Функция проводит игру до проигрыша или когда слова закончились
    """
    lifes_count: int = 0
    if not dl.set_difficult:
        lifes_count = dl.count_life()
        dl.lifes = lifes_count
        dl.set_difficult = True
    else:
        lifes_count = dl.lifes
    current_word: str = hm.build_random_word()
    lock_word: str = wc.lock_word(current_word)

    while True:
        print(f'{lock_word} | {hm.love_sym}x{lifes_count}')
        player_answer: str = input('Назовите букву или слово целиком: ')

        if player_answer == current_word:
            winner()
            break
        elif player_answer in current_word:
            if player_answer in lock_word:
                print('Эта буква уже открыта')
            else:
                print('Правильно!')
                lock_word = wc.unlock_word(current_word, lock_word, player_answer)

            if hm.lock_sym not in lock_word:
                winner()
                break
        else:
            print('Неправильно. Вы теряете жизнь')
            lifes_count -= 1

        if lifes_count == 0:
            print('Жизни закончились. Вы проиграли')
            print('Ваш рекорд ' + str(hm.record))
            break
