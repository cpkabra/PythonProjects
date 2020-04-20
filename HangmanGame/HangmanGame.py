from random import randint

def initial_print(string):
    print("Word : ", end=" ")
    for i in range(0, len(string) - 1):
        print("_", end=" ")
    print()

def print_word(string, indices):
    final_string = ""
    for j in range(len(string) - 1):
        if j in indices:
            final_string += string[j] + " "
        else:
            final_string += "_ "
    final_string.join("\n")
    return final_string

def find_indices(string, letter, indices):
    for j in range(len(string)):
        if string[j] is letter and j not in indices:
            indices.append(j)

word_list = open("words_dict.txt").readlines()
word = word_list[randint(0,len(word_list))]
final_print = []
wrong_counter = 1
winner_string = ""
initial_print(word)
while True:
    if wrong_counter > 6:
        print("No more wrong tries left!")
        print("Word : " + word)
        break
    guess = input("Enter letter: ")
    if guess in word:
        find_indices(word,guess, final_print)
        winner_string =  print_word(word, final_print)
        print(winner_string)
    else:
        winner_string =  print_word(word, final_print)
        print(winner_string)
        wrong_counter += 1
    if winner_string.replace(" ", "") == word.rstrip():
        print("Winner!")
        break






