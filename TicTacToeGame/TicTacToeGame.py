import sys
board = {"tl" :" ", "tm": " ", "tr": " ",
         "ml" :" ", "mm": " ", "mr": " ",
         "bl" :" ", "bm": " ", "br": " "}
def print_board():
   print(board["tl"] + "|" + board["tm"] + "|" + board["tr"])
   print("-+-+-")
   print(board["ml"] + "|" + board["mm"] + "|" + board["mr"])
   print("-+-+-")
   print(board["bl"] + "|" + board["bm"] + "|" + board["br"])

def check_win(piece):
    wins = [["tl", "tm", "tr"],
          ["bl", "bm", "br"],
          ["tl", "ml", "bl"],
          ["tr", "mr", "br"],
          ["tl", "mm", "br"],
          ["tr", "mm", "bl"],
          ["tm", "mm", "bm"],
          ["ml", "mm", "mr"]]

    for i in range(0, len(wins)):
        all_same = True
        for j in wins[i]:
            if board[j] != piece:
                all_same = False
        if all_same:
            return True
    return False

def valid_input(check_va):
    for keys in board.keys():
        if check_va == keys:
            return True
    return False

switcher = input("Please pick either you want X or O or quit: ")
if switcher == "quit":
    sys.exit()
while True:
    print_board()
    player_input = ""
    while not valid_input(player_input):
        player_input = input("Please enter which position you would like to insert your piece or quit: ")
    if player_input == "quit":
        sys.exit()
    board[player_input] = switcher
    if check_win(switcher):
        print_board()
        print(switcher + " player win!")
        break
    if switcher == "X":
        switcher = "O"
    else:
        switcher = "X"
