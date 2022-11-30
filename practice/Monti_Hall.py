import random

def MontyHall(count_iter):
    count = 0
    count_choice = 0

    for i in range(0, count_iter):
        a = [0, 0, 1]
        player_choice = random.choice(a)
        if player_choice == 1:
            count += 1
        else:
            a.remove(0)
            a.remove(player_choice)
            if a[0] == 1:
                count_choice += 1
    return f'количество не меняя выбор: {count} количество поменяв выбор: {count_choice} вероятность выиграша ' \
           f'при своем выборе: {(count * 100) / (count + count_choice)} '




