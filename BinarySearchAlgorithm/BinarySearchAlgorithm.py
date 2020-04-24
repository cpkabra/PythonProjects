
# @author Neel Patel
# @file BinarySearchAlgorithm.py

import random
import sys
import pandas

def binary_search_algorithm(nums, num):
    if len(nums) == 0:
        return "Number not in the list"
    mid_value = nums[int(len(nums)/2)]
    if mid_value == num:
        return "Number found!"
    elif len(nums) == 1 and mid_value != num:
        return "Number not in the list"
    elif num < mid_value:
        left = nums[0:int(len(nums) / 2)]
        return binary_search_algorithm(left, num)
    elif num > mid_value:
        right = nums[int(len(nums)/2) + 1: len(nums)]
        return binary_search_algorithm(right, num)

#------------------------MAIN PROGRAM--------------------------#
data = list()
for i in range(0,10):
    num = random.randrange(0,101,2)
    #Eliminate duplicates
    while num in data:
        num = random.randrange(0,101,2)
    data.append(num)

data = sorted(data)
print(data)
while True:
    user_input = input("Please enter the number to search or type 'quit': ")
    if user_input == "quit" or user_input == "QUIT" or user_input == "q" or user_input == "Q":
        sys.exit()
    else:
        print(str(int(user_input)) + " : " + binary_search_algorithm(data, int(user_input)))
