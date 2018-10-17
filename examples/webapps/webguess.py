# pylint: disable=E1135,E1136

import bottle
import random
import traceback

def pickSecretNumber():
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
    

@bottle.route("/")
def main():
    global secret
    secret = pickSecretNumber()
    return GUESS_FORM.format('')

@bottle.route("/guess")
def guess():
    try:
        theGuess = int(bottle.request.params['guess'])
        result = checkGuess(theGuess, secret)
    except ValueError:
        traceback.print_exc()
        return GUESS_FORM.format("Please enter a valid number")
    except Exception as e:
        traceback.print_exc()
        return GUESS_FORM.format("Oops! Something weird happened. Please contact the webmaster for help.")

    if theGuess == secret:
        return """You got it!"""
    else:
        return GUESS_FORM.format(result)
    

f = open('guessform.html','r')
GUESS_FORM = f.read()
f.close()

if __name__ == "__main__":
    bottle.run(host='localhost', debug=True)
    