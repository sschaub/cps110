class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self, newX):
        self.x = newX

    def display(self):
        print("({},{})".format(self.x, self.y),  end='')

    def __repr__(self) -> str:
        return "({},{})".format(self.x, self.y)

class LabeledPoint(Point):
    def __init__(self, x, y, label):
        #self.x = x
        #self.y = y
        super().__init__(x, y)
        self.label = label

    def display(self):
        super().display()
        print(self.label)

    def __repr__(self) -> str:
        s = super().__repr__() # call parent's repr
        return "{} {}".format(s, self.label)

    def getLabel(self) -> str:
        return self.label

p = Point(5, 10)
p.display()
print("\n----------------")
lp = LabeledPoint(20, 30, "Bravo")
lp.display()

points = [Point(5, 10), Point(20, 30), LabeledPoint(20, 30, "Bravo"), Point(6, 7)]

for p in points:
    p.setX(p.x + 10)
    if isinstance(p, LabeledPoint):
        print(p.getLabel())

print(points)