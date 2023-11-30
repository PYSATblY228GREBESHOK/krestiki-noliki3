import json

print("Крестики-нолики")

board = list(range(1, 10))
game_results = []

def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)

    results = {
        'board': board,
        'winner': tmp if tmp else None,
        'draw': counter == 9
    }
    game_results.append(results)

def save_game_results():
    with open('game_results.json', 'w') as file:
        json.dump(game_results, file)

def load_game_results():
    try:
        with open('game_results.json', 'r') as file:
            game_results.extend(json.load(file))
    except FileNotFoundError:
        pass

def show_game_results():
    for i, result in enumerate(game_results, start=1):
        print(f"Game {i}:")
        draw_board(result['board'])
        if result['winner']:
            print(result['winner'], "выиграл!")
        elif result['draw']:
            print("Ничья!")
        print()

load_game_results()

while True:
    print("Меню:")
    print("1. Начать новую игру")
    print("2. Посмотреть результаты игр")
    print("3. Выйти")
    choice = input("Выберите пункт меню: ")

    if choice == '1':
        board = list(range(1, 10))
        main(board)
        save_choice = input("Хотите сохранить игру? (y/n): ")
        if save_choice.lower() == 'y':
            save_game_results()
    elif choice == '2':
        show_game_results()
    elif choice == '3':
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
