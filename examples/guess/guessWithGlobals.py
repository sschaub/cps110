import random

secretNum = 0
guess = 0

def pickSecretNumber():
    global secretNum
    secretNum = random.randrange(1, 11)

def checkGuess():
    if guess < secretNum:
        print("Your guess is too low.")
    elif guess > secretNum:
        print("Your guess is too high.")
    else:
        print("You got it!!")
    
def main():
    global guess

    pickSecretNumber()

    numGuesses = 0
    guess = 0
    while guess != secretNum:

        guess = int(input("Enter your guess: "))
        numGuesses += 1
        checkGuess()

    print("It took you", numGuesses, "guesses.")    

if __name__ == '__main__':
    main()

    