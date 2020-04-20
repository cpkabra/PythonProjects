from random import randint


best, out = input("Best ______ out of _______?").split()
best = int(best)
out = int(out)
moves = ["rock", "paper", "scissors"]
comp_wins, player_wins =  0, 0

def comp_win(comp_param, player_param, win_param):
    print("Computer played " + moves[comp_param] + " and player played " + player_param)
    print("Computer wins : " + str(win_param))
    print("Player wins   : " + str(player_wins))
    print()
def player_win(comp_param, player_param, win_param):
    print("Computer played " + moves[comp_param] + " and player played " + player_param)
    print("Computer wins : " + str(comp_wins))
    print("Player wins   : " + str(win_param))
    print()


for i in range(0, out):
    if player_wins == best:
        print("Player won!")
        break
    elif comp_wins == best:
        print("Computer won")
        break
    comp_move = randint(0,2)
    player_move = input("Please enter your play(rock, paper, scissors): ")
    if player_move not in moves:
        print("Invalid Entry")
    player_index = moves.index(player_move)
    if player_index == comp_move:
        print("Both played the same move")
    elif player_index == 0:
        if comp_move == 1:
            comp_wins += 1
            comp_win(comp_move, player_move, comp_wins)
        elif comp_move == 2:
            player_wins += 1
            player_win(comp_move, player_move, player_wins)
    elif player_index == 1:
        if comp_move == 0:
            player_wins += 1
            player_win(comp_move, player_move, player_wins)
        elif comp_move == 2:
            comp_wins += 1
            comp_win(comp_move, player_move, comp_wins)
    elif player_index == 2:
        if comp_move == 0:
            comp_wins += 1
            comp_win(comp_move, player_move, comp_wins)
        elif comp_move == 1:
            player_wins += 1
            player_win(comp_move, player_move, player_wins)
    print()


if player_wins != best and comp_wins != best:
    if player_wins > comp_wins:
        print("Player won more games than computer!")
    elif player_wins == comp_wins:
        print("Game Tied!")
    else:
        print("Computer won more games than player!")
    print()





