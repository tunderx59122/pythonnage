from enum import Enum
from random import shuffle

class Shape(Enum):
    # enum des differentes formes de blocks
    # c'est le vrai nom des blocks c'est pas des lol
    I = 0
    J = 1
    L = 2
    O = 3
    S = 4
    T = 5
    Z = 6

    def getRandomShape():
        shapes: list[Shape] = list()
        shapes.append(Shape.I)
        shapes.append(Shape.J)
        shapes.append(Shape.L)
        shapes.append(Shape.O)
        shapes.append(Shape.S)
        shapes.append(Shape.T)
        shapes.append(Shape.Z)

        shuffle(shapes)
        return shapes[0]