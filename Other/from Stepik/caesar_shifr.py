# Шифр Цезаря

print('Шифр Цезаря')

lang = input('Выберите язык. Русский или английский. Введите ru или en: ')
direction = input('Что вы ходите сделать? Шифрование или дешифрование? Введите cipher или decipher: ')
if direction == 'decipher':
    question = input('Вы знаете шаг сдвига? yes или no: ')
    if question == 'yes':
        step = input('Введите шаг сдвига: ')
else:
    step = input('Введите шаг сдвига: ')
original_text = input('Введите текст: ')

ru_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # 32 буквы (0-31)
en_alphabet = 'abcdefghijklmnopqrstuvwxyz'  # 26 букв (0-25)
symbols = '1234567890 .,?"!\'-'

# Алгоритм шифрования
def ceasar_cipher(text, alphabet, step):
    result_text = []
    for letter in text:
        steps = alphabet.find(letter.lower()) + int(step)  # Находим сдвиг буквы
        if letter in symbols:  # Если есть символы оставляем без изменений
            result_text.append(letter)  # Добавляем в список
            continue
        elif steps < len(alphabet):  # Если шаг в пределах индексов списка алфавитов
            if steps < 0:  # Действия при расшифровки
                if lang == 'en':
                    steps += 26
                else:
                    steps += 32
            if letter == letter.upper():  # Если была прописная буква, то новая будет в том же регистре
                ch_letter = alphabet[steps]
                result_text.append(ch_letter.upper())
            else:
                ch_letter = alphabet[steps]
                result_text.append(ch_letter)
        elif steps >= len(alphabet):  # Если шаг вышел за пределы индексов списка алфавитов
            if letter == letter.upper():
                ch_letter = alphabet[steps - len(alphabet)]
                result_text.append(ch_letter.upper())
            else:
                ch_letter = alphabet[steps - len(alphabet)]
                result_text.append(ch_letter)
    result_text = ''.join(result_text)
    return result_text


def is_valid_input(direction, lang):
    if direction == 'cipher' or direction == 'decipher':
        if lang == 'ru' or lang == 'en':
            return True
    else:
        return False


if is_valid_input(direction, lang):
    if direction == 'cipher':
        if lang == 'en':
            print(ceasar_cipher(original_text, en_alphabet, step))
        else:
            print(ceasar_cipher(original_text, ru_alphabet, step))
    elif direction == 'decipher':
        if lang == 'en':
            if question == 'yes':
                print(ceasar_cipher(original_text, en_alphabet, -(int(step))))
            else:
                for i in range(len(en_alphabet)):
                    print('Вариант', i, ceasar_cipher(original_text, en_alphabet, i))
        elif lang == 'ru':
            if question == 'yes':
                print(ceasar_cipher(original_text, ru_alphabet, -(int(step))))
            else:
                for i in range(len(ru_alphabet)):
                    print('Вариант', i, ceasar_cipher(original_text, ru_alphabet, i))
else:
    print('Вы ошиблись в вводе, повторите попытку')


