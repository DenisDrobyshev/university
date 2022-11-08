import general_sys as gs

def start_game():
    while True:
        command = int(input('1 - Начать игру, 2 - Выход \n'))

        if command == 1:
            gs.start_game()
            print('Хотите сыграть еще?')
        elif command == 2:
            break
start_game()