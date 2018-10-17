import random

# generate secret number
secretNum = random.randrange(1, 11)

numGuesses = 0
guess = 0
while guess != secretNum:

    guess = int(input("Enter your guess: "))
    numGuesses += 1
    
    # Give feedback on guess
    if guess < secretNum:
        print("Your guess is too low.")
    elif guess > secretNum:
        print("Your guess is too high.")
    else:
        print("You got it!!")

print("It took you", numGuesses, "guesses.")  
