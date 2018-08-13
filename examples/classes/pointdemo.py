class Point:
  
    def __init__(self):
        self.x = 0
        self.y = 0

    def toString(self):
        return "({0},{1})".format(self.x, self.y)

here = Point()
here.x = 10
here.y = 20

there = Point()
there.x = 50
there.y = 60

print("here = " + here.toString())
print("there = " + there.toString())
