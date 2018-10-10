import bottle
import random

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
    print('I picked ' + str(secret) + ' (shhh!)')
    return GUESS_FORM.format('')

@bottle.route("/guess")
def guess():
    
    theGuess = int(bottle.request.params['guess'])
    result = checkGuess(theGuess, secret)
    
    if theGuess == secret:
        return """You got it!"""
    else:
        return GUESS_FORM.format(result)
    

GUESS_FORM = """
<html>
<body>
<h1>Welcome to Guess</h1>

I've picked a secret number from 1 to 10.

<form action="/guess">
Enter your guess: <input type="text" name="guess">
<input type="submit" value="Guess">
</form>

{}

</body>
</html>

"""

if __name__ == "__main__":
    bottle.run(host='localhost', debug=True)