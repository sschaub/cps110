
import bottle
import random
import traceback

WIDTH=700
HEIGHT=700


@bottle.route('/')
def welcome():  
    svgdata = []
    svgdata.append("<rect x='0' y='0' width='{}' height='{}' fill='black' />".format(WIDTH, HEIGHT))

    for x in range(0, WIDTH+1, 100):
        svgdata.append("<line x1='{0}' y1='0' x2='{0}' y2='{1}' stroke='green' />".format(x, HEIGHT))

    for y in range(0, HEIGHT+1, 100):
        svgdata.append("<line x1='0' y1='{0}' x2='{1}' y2='{0}' stroke='green' />".format(y, WIDTH))

    svgdata.append("<image x='{0}' y='{1}' xlink:href='images/{2}' width='50' height='50' />".format(20, 30, 'duck.png'))
    svgdata.append("<text x='{0}' y='{1}' font-family='Verdana' font-size='10' stroke='white'>{2}</text>".format(10, 20, 'Some text here'))
        
    svgstring = '\n'.join(svgdata)
    return HTML_PAGE.format(WIDTH, HEIGHT, svgstring)

@bottle.route('/<filename:path>')
def send_static(filename):
    """Serve up images and sounds."""
    return bottle.static_file(filename, root='.')


HTML_PAGE = """
<!DOCTYPE html>
<html>
<body>

<svg width="{0}" height="{1}">
  {2}
</svg>

</body>
</html>
"""

if __name__ == '__main__':

    # Launch the BottlePy dev server
    bottle.run(host="localhost", port=8080, debug=True)
    