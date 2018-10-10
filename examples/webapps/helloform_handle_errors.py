# pylint: disable=E1135,E1136

import bottle
import datetime

@bottle.route('/')
def home():
    return HTML_FORM

@bottle.route('/hello')
def hello():
    username = 'World'
    age = 15
    if 'username' in bottle.request.params:
        username = bottle.request.params['username']
    if 'age' in bottle.request.params:
        age = bottle.request.params['age']

    if username == "" or age == "":
        return HTML_FORM

    return """<html><body>
        <h1>Hello, {0}!</h1>
        You are {1} years old.</body></html>""".format(
            username, age)

HTML_FORM = """

<form action="/hello">
    Enter your username: <input type="text" name="username" value="Hello"><br>
    Enter your age: <input type="text" name="age" value="18"><br>
    <input type="submit" value="Click here for a friendly greeting">
</form>
"""


# Launch the BottlePy dev server
if __name__ == "__main__":
    bottle.run(host='localhost', debug=True)

