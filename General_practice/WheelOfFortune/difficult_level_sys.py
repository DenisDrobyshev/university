lifes = 0
set_difficult = False

def difficult_live_count():
    choice = int(input('Введите уровень сложности: 1-легко, 2-средне, 3-сложно '))

    if choice == 1:
        return 7
    elif choice == 2:
        return 5
    elif choice == 3:
        return 3
    else:
        print('Вы не ввели уровень сложности!')
        return difficult_live_count()
