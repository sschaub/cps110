
WIDTH=700
HEIGHT=700

class Shape:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def draw(self) -> str:
        return ""

class Circle(Shape):
    def __init__(self, x=0, y=0, radius=0, color='white'):
        super().__init__(x, y)
        self.radius = radius
        self.color = color

    def draw(self) -> str:
        return """
                <circle cx='{}' cy='{}' r='{}' fill='{}' />
            """.format(self.x, self.y, self.radius, self.color)

class Rectangle(Shape):
    def __init__(self, x=0, y=0, width=0, height=0, color='white'):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = color

    def draw(self) -> str:
        return """
            <rect x='{}' y='{}' width='{}' height='{}' fill='{}' />
        """.format(self.x, self.y, self.width, self.height, self.color)
            

class Drawing:
    def __init__(self, width=700, height=700):
        self.width = width
        self.height = height
        self.shapes = []

    def addShape(self, s: Shape):
        self.shapes.append(s)

    def generateSVG(self) -> str:

        svgCommands = ""
        for shape in self.shapes:
            svgCommands += shape.draw()

        return """
<svg width="{0}" height="{1}">
{2}
</svg>
""".format(self.width, self.height, svgCommands)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<body>

{0}

</body>
</html>
"""

drawing = Drawing()
drawing.addShape(Circle(200, 100, 25, 'blue'))
drawing.addShape(Rectangle(40, 70, 20, 30, 'green'))

page = HTML_PAGE.format(drawing.generateSVG())
f = open('demo.html', 'w')
f.write(page)
f.close()
