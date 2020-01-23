# Game Map Initialization
import numpy as np
from colorama import Fore, Back, Style, init
init()
# Defaults to 3x3
game_size = 3

def game_board(game_map, player=0, row=0, col=0, just_display=False):
    try_again = False
    try:
        if not just_display:
            if game_map[row][col] == 0:
                game_map[row][col] = player
            else:
                print('Hey try another row or column , its occupied!!')
                try_again = True


        s = '   ' + '  '.join([str(i) for i in range(game_size)])
        print(s)
        for rownum, row in enumerate(game_map):
            print(rownum, row)
    except IndexError as e:
        print('something went wrong', e)
    return game_map, try_again

def win(current_game):

    # Vertical Win
    check = [[] for i in range(game_size)]
    won = False
    for t in range(len(current_game)):
        for i, row in enumerate(current_game):
            check[t].append(row[t])
        if len(check[t]) == check[t].count(check[t][0]) and check[t][0] != 0:
            won = True
            print(f"We have a winner player number : {check[t][0]}")
            break


    for row in current_game:
        if len(row) == row.count(row[0]) and row[0] != 0:
            print(f"Winner Player number: ', {row[0]}")
            won = True
            break

    check = []
    for i in range(len(current_game)):
        check.append(current_game[i][i])
    if len(check) == check.count(check[0]) and check[0] != 0:
        won = True
        print(f"Winner Player number: , {check[0]}")

    check = []
    cols = list(reversed(range(len(current_game))))
    rows = list(range(len(current_game)))

    for ids in range(len(rows)):
        check.append(current_game[rows[ids]][cols[ids]])

    if len(check) == check.count(check[0]) and check[0] != 0:
        won = True
        print('Winner Player number: ', check[0])


    return current_game, won


play = True
players = [1,2]

while play:
    print(Fore.RED + 'Hello')
    game_size = int(input(Fore.GREEN + 'Enter Game Size :').strip())
    #game = np.zeros((game_size,game_size)).astype(int).tolist()

    game = [[0 for j in range(game_size)] for i in range(game_size)]

    game_won = False
    mod_player = 3
    game, try_again = game_board(game, just_display=True)
    while not game_won:


        current_player = players[(mod_player+1)%len(players)]

        print(f"Its Player {current_player}'s turn")
        row_choice = int(input("Enter Row Number : "))
        col_choice = int(input("Enter Column Number : "))
        game, try_again = game_board(game, player=current_player, row=row_choice, col=col_choice, just_display=False)
        if try_again:
            continue
        else:
            mod_player += 1
        game, winner = win(game)
        if winner:
            break
    continue_play = input(Fore.RED + "Do you want to play another game ? ( yes/no )").strip().lower()

    if continue_play == 'no':
        play = False





