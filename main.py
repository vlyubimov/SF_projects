import copy
# Игровое поле
game_board = [[" ", 0, 1, 2],
             [0, "-", "-", "-"],
             [1, "-", "-", "-"],
             [2, "-", "-", "-"],]

# Функии механики игры
def restart_board(board):
    global game_board
    clone_board = [[" ", 0, 1, 2],
             [0, "-", "-", "-"],
             [1, "-", "-", "-"],
             [2, "-", "-", "-"],]
    game_board = clone_board
    print("--------------\n НОВЫЙ РАУНД\n--------------")

def drow_board(board):
    for i in board:
        print(*i)

def take_turn(player_turn):
    valid = False
    while not valid:
        colomn = input(f"В какую колонку поставим {player_turn}?\n")
        row = input(f"В какую строку поставим {player_turn}?\n")
        try:
            colomn = int(colomn)
            row = int(row)
        except:
            print("Некорректный ввод")
            continue
        if 0<=colomn<=2 and 0<=row<=2:
            if (game_board[row+1][colomn+1]) == "-":
                game_board[row+1][colomn+1] = player_turn
                valid = True
            else:
                print("Клеточка уже занята:(")
        else:
            print("Введите число от 1 до 2, что бы походить")


def check_win(board):
    win_coard = (([1,1],[1,2],[1,3]),([2,1],[2,2],[2,3]),([3,1],[3,2],[3,3]),([1,1],[2,1],[3,1]),([1,2],[2,2],[3,2]),([1,3],[2,3],[3,3]),([1,1],[2,2],[3,3]),([1,3],[2,2],[3,1]))
    for each in win_coard:
        if board[each[0][0]][each[0][1]] == board[each[1][0]][each[1][1]] == board[each[2][0]][each[2][1]]:
            return board[each[0][0]][each[0][1]]
    return False
def game(board):
    counter = 0
    win = False
    while not win:
        drow_board(board)
        if counter%2 == 0:
            take_turn("X")
        else:
            take_turn("O")
        counter += 1
        if counter > 4:
            temp = check_win(board)
            if temp:
                print(f"{temp} выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    drow_board(board)
    restart_board(game_board)


# Тело игры
while True:
    game(game_board)

