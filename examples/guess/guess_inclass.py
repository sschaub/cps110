import random

def generateSecretNumber():
    """returns a random number from 1 to 10"""

    # generate secret number
    secretNum = random.randrange(1, 11)
    return secretNum

def giveFeedback(guess, secretNum):
    """compares `guess` to `secretNum` and gives appropriate feedback"""
    # Give feedback on guess
    if guess < secretNum:
        print("Your guess is too low.")
    elif guess > secretNum:
        print("Your guess is too high.")
    else:
        print("You got it!!")

def main():

    secretNum = generateSecretNumber()

    numGuesses = 0
    guess = 0
    while guess != secretNum:

        guess = int(input("Enter your guess: "))
        numGuesses += 1
        
        giveFeedback(guess, secretNum)

    print("It took you", numGuesses, "guesses.")  


if __name__ == '__main__':
    main()

