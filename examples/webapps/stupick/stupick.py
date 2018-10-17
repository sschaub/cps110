import os.path
import bottle
import random

# To create a desktop shortcut using Chrome:
# "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --chrome-frame --app="http://sschaub.pythonanywhere.com/stupick"

SOUNDS = ["236982__devengarber__jacob-allen-evil-laugh",
    "347547__masgame__applause",
    "371339__johanneskristjansson__cheer-crowd",
    "stupick3-men-cheering"]

CUR_DIR = os.path.dirname(__file__)
students = []
    
@bottle.route('/stupick')
def picker():

    with open(CUR_DIR + '/stupick.html') as htmlfile:
        HTML = htmlfile.read()

    if len(students) == 0:
        readStudentFile()
    stuInx = random.randrange(len(students))
    stuName, stuUsername = students[stuInx]
    del students[stuInx]
    effect = SOUNDS[random.randrange(len(SOUNDS))]

    return HTML.format(name=stuName, username=stuUsername, sound=effect)

def readStudentFile():
    with open(CUR_DIR + '/cps110.txt') as stufile: 
        for student in stufile:
            [_, _, firstname, lastname, username] = student.split(',')        
            students.append((firstname[0] + ". " + lastname, username))

    print("Loaded data: ", students)

if __name__ == '__main__':

    @bottle.route('/<filename:path>')
    def send_static(filename):
        """Serve up images and sounds."""
        return bottle.static_file(filename, root='.')

    # Launch the BottlePy dev server
    bottle.run(host='localhost', debug=True)
