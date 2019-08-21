from collections import namedtuple


coordinates = namedtuple('Coordinato', ['x', 'y', 'z'])


first = coordinates(50, 20, 15)

print(first.x)
print(type(first))
print(type(first.x))


if str(type(coordinates) == 'Coordinato':
    print("yes!")
