from Block import Block

if __name__ == "__main__":
    squareMatrix = [
        [True, True, False, False],
        [True, True, False, False],
        [False, False, False, False],
        [False, False, False, False]
    ]
    square = Block("square", squareMatrix, "red")

    print(square.getBoxesPos())
