def makePoint(x: int, y: int) -> list:
    return [x, y]

def getX(point: list) -> int:
    return point[0]

def getY(point: list) -> int:
    return point[1]

def setX(point, newX):
    point[0] = newX

def setY(point, newY):
    point[1] = newY

def distance(point1, point2):
    return ((getX(point1) - getX(point2)) ** 2 
              + (getY(point1) - getY(point2)) ** 2) ** .5

def toString(point):
    return "({0},{1})".format(getX(point), getY(point))

here = makePoint(3, 5)
there = makePoint(8, 5)

print("here =", toString(here))
print("there =", toString(there))

print("Distance from", toString(here), "to", toString(there),
      "is:", distance(here, there))

print("Setting there's Y to 10.")
setY(there, 10)
print("there =", toString(there))
