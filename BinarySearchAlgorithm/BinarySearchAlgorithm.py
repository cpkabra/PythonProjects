from random import randint
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

data = []
for i in range(0,101):
    num = randint(0,1000)
    while num in data:
        num = randint(0,1000)
    data.append(num)
data = sorted(data)
print(data)
num_to_search = int(input("Please enter the number to search : "))
print(str(num_to_search) + " : " + binary_search_algorithm(data, num_to_search))
