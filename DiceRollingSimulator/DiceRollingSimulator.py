
# @author Neel Patel
# @file DiceRollingSimulator.py

from random import randint

def print_one():
    print(" ---------\n|         |\n|    0    |\n|         |\n ---------")
def print_two():
    print(" ---------\n|         |\n|  0   0  |\n|         |\n ---------")
def print_three():
    print(" ---------\n| 0       |\n|    0    |\n|       0 |\n ---------")
def print_four():
    print(" ---------\n| 0     0 |\n|         |\n| 0     0 |\n ---------")
def print_five():
    print(" ---------\n| 0     0 |\n|    0    |\n| 0     0 |\n ---------")
def print_six():
    print(" ---------\n| 0  0  0 |\n|         |\n| 0  0  0 |\n ---------")

#-----START------#
num = randint(1,6)
if num == 1:
    print_one()
elif num == 2:
    print_two()
elif num == 3:
    print_three()
elif num == 4:
    print_four()
elif num == 5:
    print_five()
elif num == 6:
    print_six()
