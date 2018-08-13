# pylint: disable=E1135,E1136

import bottle
import datetime



@bottle.route('/')
def home():
    return """<html><body>Welcome!
    The time is {}.
    <a href="/page2">Click here</a> for page 2.
    </body></html>""".format(datetime.datetime.now())

@bottle.route('/page2')
def page2():
    return """<html><body>Here is page 2.</body></html>"""

@bottle.route('/hello')
def hello():
    name = 'World'
    age = 15
    if 'name' in bottle.request.params:
        name = bottle.request.params['name']
    if 'age' in bottle.request.params:
        age = bottle.request.params['age']

    return """<html><body>
        <h1>Hello, {0}!</h1>
        You are {1} years old.</body></html>""".format(
            name, age)

# Launch the BottlePy dev server
if __name__ == "__main__":
    bottle.run(host='localhost', debug=True)

