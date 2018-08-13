import os.path
import bottle
import random

SOUNDS = ["236982__devengarber__jacob-allen-evil-laugh",
    "347547__masgame__applause",
    "371339__johanneskristjansson__cheer-crowd",
    "stupick3-men-cheering"]
    
@bottle.route('/stupick')
def picker():
    if len(students) == 0:
        readStudentFile()
    stuInx = random.randrange(len(students))
    stuName, stuUsername = students[stuInx]
    del students[stuInx]
    effect = SOUNDS[random.randrange(len(SOUNDS))]

    return HTML.format(stuName, stuUsername, effect)

HTML = """
<html>
<head>
<style>
html, body {{
    height: 100%;
}}

html {{
    display: table;
    margin: auto;
}}

body {{
    display: table-cell;
    vertical-align: middle;
    background: black;
    color: darkblue;
}}
</style>
</head>
<body>
<img src="/stupics/{1}.bmp" width="200">
<h3>{0}</h3>
<audio autoplay>
  <source src="/sounds/{2}.mp3" type="audio/mpeg" >
</audio>
</body>
</html>
"""

students = []
def readStudentFile():
    with open(os.path.dirname(__file__) + '/cps110.txt') as stufile: 
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
