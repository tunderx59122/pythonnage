from Block import Block
from Point import Point
from Shape import Shape


if __name__ == "__main__":
    i_block = Block(Point(0, 0), Shape.I)

    for rect in i_block.rects:
        print(rect)

    i_block.moveDown()

    for rect in i_block.rects:
        print(rect)

