# Вывести на экран инструкцию для игрока
# решить кому принадлежит первый ход
# создать пустую доску для игры в крестики нолики
# отобразить ее
# пока никто не выиграл или не состоялась ничья
#   если ход игрока
#       получить ход из пользовательского ввода
#       изменить вид доски
#   иначе
#       рассчитать ход компьютера
#       изменить вид доски
#   вывести на экран обновленный вид доски
#   осуществить переход хода
# поздравить победителя или объявить ничью
X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9


def instructions() -> None:
    """Выводит на экран инструкцию для игрока"""
    print(
        """Ответь на вопрос будешь ли ты играть, если да, то смотри таблицу
    Чтобы сделать ход, введи число от 0 до 8, как показано ниже:
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8 \n
    """)


def ask_yes_no(question: str) -> str:
    """
    Задает вопрос с ответом "да" или "нет"
    :param question: принимает "Да" "Нет"
    :return: возвращает "y" "n"
    """
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question: str, low: int, high: int) -> int:
    """
    Просит ввести число из диапазона
    :param question: текст вопроса
    :param low: нижняя граница
    :param high: верхняя граница
    :return: число из данного диапазона
    """
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Определяет принадлежность первого хода"""
    go_first = ask_yes_no("Хочешь оставить за собой первый ход? (y/n): ")
    if go_first == "y":
        print("\nНу что ж, даю тебе фору играй крестиками.")
        human = X
        computer = O
    else:
        computer = X
        human = O
    return computer, human


def new_board():
    """Создает новую игровую доску"""
    board: list = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Отображает игровую доску на экране """
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8])


def legal_moves(board):
    """Создает список доступных ходов"""
    moves: list = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Определяет победителя в игре"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None


def human_move(board, human):
    """Получает ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nВыберите другое поле, это уже занято!")
        print("Ладно...")
        return move


def computer_move(board, computer, human):
    """Делает ход за компьютерного противника."""
    # Создадим рабочую копию доски, потому что эта функция будет менять некоторые значение в списке
    board = board[:]
    # Поля от лучшего к худшему
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер:", end=" ")

    for move in legal_moves(board):
        board[move] = computer
        # если следующим ходом может победить компьютер, выберем этот ход
        if winner(board) == computer:
            print(move)
            return move
        # выволнив проверку, отменим все внесенные изменения
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        # если следующим ходом может победить человек, блокируем этот ход
        if winner(board) == human:
            print(move)
            return move
        # выволнив проверку, отменим все внесенные изменения
        board[move] = EMPTY

    # поскольку следующим ходом ни одна сторона не может победить
    # выберем лучшее из допустимых полей
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Осуществляет переход хода"""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """Поздравляет победителя игры"""
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья\n")
    if the_winner == computer:
        print("Победа за ИИ")
    elif the_winner == human:
        print("Победа за вами")
    elif the_winner == TIE:
        print("Ничья!")


def main():
    instructions()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()
