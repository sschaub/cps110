import random

def pickSecretNumber():
    """Returns random number between 1 and 10"""    
    return random.randrange(1, 11)

def checkGuess(guess, secretNum):
    """Prints a hint showing relation of `guess` to `secretNum`"""    
    if guess < secretNum:
        print("Your guess is too low.")
    elif guess > secretNum:
        print("Your guess is too high.")
    else:
        print("You got it!!")
    
def main():
    secretNum = pickSecretNumber()

    numGuesses = 0
    guess = 0
    while guess != secretNum:

        guess = int(input("Enter your guess: "))
        numGuesses += 1
        checkGuess(guess, secretNum)

    print("It took you", numGuesses, "guesses.")    

if __name__ == '__main__':
    main()

