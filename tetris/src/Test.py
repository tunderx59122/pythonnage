from Block import Block
from Box import Box
from Point import Point
from Shape import Shape

if __name__ == "__main__":
    i_block = Block(Shape.I, Box(Point(0, 0)))

    for box in i_block.boxes:
        print("-> " + box.topLeft.getX().__str__() + ", " + box.topLeft.getY().__str__())
