from random import randint

low = int(input("Please enter the low boundary: "))
high = int(input("Please enter the high boundary: "))
actual_number = randint(low,high)
counter = 0

while True:
    guess = int(input("Please enter your guess: "))
    counter += 1
    if guess < actual_number:
        print("Your guess is lower than the actual number.")
    elif guess > actual_number:
        print("Your guess is higher than the actual number.")
    else:
        print("You guessed it!")
        print("You took " + str(counter) + " tries.")
        break



