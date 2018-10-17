import random

def pickSecretNumber() -> int:
    """Returns random number between 1 and 10"""    
    return random.randrange(1, 11)

def checkGuess(guess, secretNum):
    """Prints a hint showing relation of `guess` to `secretNum`"""    
    if guess < secretNum:
        return "Your guess is too low."
    elif guess > secretNum:
        return "Your guess is too high."
    else:
        return "You got it!!"

def test_pickSecretNumber():
    num = pickSecretNumber()
    assert 1 <= num <= 10

def test_checkGuess():
    assert checkGuess(4, 7) == "Your guess is too low."
    
def main():
    secretNum = pickSecretNumber()

    numGuesses = 0
    guess = 0
    while guess != secretNum:

        guess = int(input("Enter your guess: "))
        numGuesses += 1
        print(checkGuess(guess, secretNum))

    print("It took you", numGuesses, "guesses.")    

if __name__ == '__main__':
    main()

