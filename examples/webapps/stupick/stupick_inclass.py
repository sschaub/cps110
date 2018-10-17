
import bottle
import random

SOUNDS = ["236982__devengarber__jacob-allen-evil-laugh",
    "347547__masgame__applause",
    "371339__johanneskristjansson__cheer-crowd",
    "stupick3-men-cheering"]
    
@bottle.route('/')
def picker():

    return HTML.format(stuName, stuUsername, effect)

HTML = """
<html>
<body>
<h1>{0}</h1>
<img src="/pics/{1}.bmp" width="200">
<audio autoplay>
  <source src="/sounds/{2}.mp3" type="audio/mpeg" >
</audio>
</body>
</html>
"""

students = []
def readStudentFile():
    stufile = open('cps110.txt')
 
    for student in stufile:
        [_, _, firstname, lastname, username] = student.split(',')
    
        students.append((firstname + " " + lastname, username))

    #print(studentdata)


    print("Loaded data: ", students)

if __name__ == '__main__':
    @bottle.route('/<filename:path>')
    def send_static(filename):
        """Serve up images and sounds."""
        return bottle.static_file(filename, root='.')

    readStudentFile()

    # Launch the BottlePy dev server
    bottle.run(host='localhost', debug=True)
