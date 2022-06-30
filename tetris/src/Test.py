from Shape import Shape
# from Block import Block
# from Point import Point


if __name__ == "__main__":

    # for attr, value in Shape.__dict__.items():
    #     # if (value == 0):
    #     if not (attr.startswith("__")):
    #         print(str(attr) + ": " , value)
    #         print(attr)
    #         print(value == Shape.I)
    print(Shape.getRandomShape())