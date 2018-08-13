def makePoint(x, y):
    return { 'x': x, 'y': y }

def distance(point1, point2):
    return ((point1['x'] - point2['x']) ** 2 
              + (point1['y'] - point2['y']) ** 2) ** .5

def toString(point):
    return "({0},{1})".format(point['x'], point['y'])

here = makePoint(3, 5)
there = makePoint(8, 5)

print("here =", toString(here))
print("there =", toString(there))

print("Distance from", toString(here), "to", toString(there),
      "is:", distance(here, there))

print("Setting there's Y to 10.")
there['y'] = 10
print("there =", toString(there))
