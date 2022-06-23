from Block import Block
from Box import Box
from Point import Point
from Shape import Shape

if __name__ == "__main__":
    # box test
    # box:Box = Box(Point(5, 5))

    # print(box)

    # box.moveX(10)
    # box.moveY(10)

    # print(box)

    # I
    i_block = Block(Shape.I, Box(Point(0, 0)))

    print(i_block)

    i_block.moveY(5)

    print(i_block)

    # print("I: ")
    # for box in i_block.boxes:
    #     print("-> " + box.topLeft.getX().__str__() + ", " + box.topLeft.getY().__str__())

    

    # 
