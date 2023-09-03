import handler


def play(word):
    # тело функции
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print("Давайте играть в угадайку слов!")
    print(handler.display_hangman(tries))
    print(word_completion)

    while True:
        input_word = input("Введите букву или слово целиком: ").upper()
        if not input_word.isalpha():
            print("Вы ошиблись, введите снова")
            continue
        if input_word in guessed_letters or input_word in guessed_words:
            print("Уже было")
            continue
        if len(input_word) > 1:
            if input_word == word:
                print('Поздравляем, вы угадали слово! Вы победили!')
                break
            else:
                guessed_words.append(input_word)
                tries -= 1
                print(f'Не верно, осталось попыток {tries}')
                print(handler.display_hangman(tries))
                if tries == 0:
                    print(f'Вы не смогли угадать слово: {word}')
                    break
                continue
        if input_word in word:
            guessed_letters.append(input_word)
            for letter in word:
                if letter not in guessed_letters:
                    print('Вы угадали букву')
                    handler.print_word(word, guessed_letters)
                    guessed = False
                    break
                guessed = True
            if guessed:
                handler.print_word(word, guessed_letters)
                print('Поздравляем, вы угадали слово! Вы победили!')
                break
        else:
            guessed_letters.append(input_word)
            tries -= 1
            print(f'Не верно, осталось попыток {tries}')
            print(handler.display_hangman(tries))
            handler.print_word(word, guessed_letters)
        if tries == 0:
            print(f'Вы не смогли угадать слово: {word}')
            break


play(handler.get_word(handler.wordConverter()))
