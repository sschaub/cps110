class Point:
    def __init__(self, initX: float, initY: float):
        self.x = initX
        self.y = initY
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, newX):
        self.x = newX
    
    def setY(self, newY):
        self.y = newY
    
    def __str__(self):
        return "({0},{1})".format(self.getX(), self.getY())
    
    def distanceTo(self, other):
        return ((self.getX() - other.getX()) ** 2 + (self.getY() - other.getY()) ** 2) ** .5


here = Point(3, 5)
there = Point(8, 5)

print("Distance from", here, "to", there,
      "is:", here.distanceTo(there))

print(here)
here.setX(42)
print(here)
