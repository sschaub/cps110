class Point:
  
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return "({0},{1})".format(self.x, self.y)

    def __repr__(self):
        return self.toString()

pointlist = [
    Point(3, 5),
    Point(10, 20)
]

print(pointlist)