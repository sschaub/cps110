class Shape:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, newx: int, newy: int):
        self.x = newx
        self.y = newy

    
class Rectangle(Shape):
    def __init__(self, x: int, y: int, width: int, height: int, color: str):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = color

    def draw():
        