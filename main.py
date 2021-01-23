import random

print("Number guessing game")

number = random.randint(1, 9)

chances = 0

print("Guess a number between 1 and 9 : ")

while chances < 5:

    guess = int(input("Input your guess : "))


    if guess == number:
        print("Your guess was correct !! Congo !! :tada:")
        chances = 6

    elif guess < number:
        print("Your guess was less than the number . Guess a greater number than", guess)

    else:
        print("Your guess was high than the number . Guess a lower number than", guess)

    chances += 1


if chances == 5:
    print("YOU LOSE!!! The number is", number)
