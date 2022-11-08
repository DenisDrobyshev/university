import help_manager as hm
import difficult_level_sys as dls
import word_combination as wc

def winner():
    print('Победитель! Призы в студию!')
    hm.session_record += 1

    if hm.session_record > hm.record:
        print('Это ваш новый рекорд угаданных подряд слов: ' + str(hm.session_record))
        hm.record = hm.session_record
        hm.new_record()

def start_game():
    life_count = 0
    if not dls.set_difficult:
        lifes_count = dls.difficult_live_count()
        dls.lifes = lifes_count
        dls.live_count = True
    else:
        lifes_count = dls.lifes
    current_word = hm.build_random_word()
    lock_word = wc.lock_word(current_word)

    while True:
        print(f'{lock_word} | {hm.love_sym}x{lifes_count}')
        player_answer = input('Назовите букву или слово целиком: ')

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
