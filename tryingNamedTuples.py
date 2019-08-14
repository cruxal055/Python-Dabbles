from collections import namedtuple


coordinates = namedtuple('Coordinate', ['x', 'y', 'z'])


first = coordinates(50, 20, 15)

print (first.x)

