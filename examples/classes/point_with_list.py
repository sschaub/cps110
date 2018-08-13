def makePoint(x, y):
    return [x, y]

def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 
              + (point1[1] - point2[1]) ** 2) ** .5

def toString(point):
    return "({0},{1})".format(point[0], point[1])

here = makePoint(3, 5)
there = makePoint(8, 5)

print("here = ({0},{1})".format(here[0], here[1]))
print("there =", toString(there))

print("Distance from", toString(here), "to", toString(there),
      "is:", distance(here, there))

print("Setting there's Y to 10.")
there[1] = 10
print("there =", toString(there))
