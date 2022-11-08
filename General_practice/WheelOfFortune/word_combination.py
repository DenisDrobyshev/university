from WheelOfFortune.help_manager import lock_sym

def lock_word(word):
    word_list = [x for x in word]
    output = ''

    for i in range(0, len(word)):
        word_list[i] = lock_sym
    return output.join(word_list)


def unlock_word(unlocked_word, lock_word, part):  # part - повторяющаяся буква в слове
    all_part_indexs = []

    locked_word_list = [x for x in lock_word]
    output = ''

    for i in range(0, len(unlocked_word)):
        if unlocked_word[i] == part:
            all_part_indexs.append(i)

    for j in all_part_indexs:
        locked_word_list[j] = part

    return output.join(locked_word_list)