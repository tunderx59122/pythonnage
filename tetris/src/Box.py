from Point import Point


class Box:
    def __init__(self, topLeftPos: Point, size: int = 5) -> None:
        # Box = carre compose de 4 points: topLeft, botLeft, topRight, botRight
        # plus simple pour gerer le collisions
        # size = 5 par default
        self.topLeft: Point = Point(topLeftPos.getX(), topLeftPos.getY())
        self.topRight = Point(topLeftPos.getX() + size, topLeftPos.getY())
        self.botLeft = Point(topLeftPos.getX(), topLeftPos.getY() + size)
        self.botRight = Point(topLeftPos.getX() + size,
                              topLeftPos.getY() + size)
        self.size = size

    def moveX(self, xToAdd: int) -> None:
        self.topLeft.moveX(xToAdd)
        self.topRight.moveX(xToAdd)
        self.botLeft.moveX(xToAdd)
        self.botRight.moveX(xToAdd)

    def moveY(self, yToAdd: int) -> None:
        self.topLeft.moveY(yToAdd)
        self.topRight.moveY(yToAdd)
        self.botLeft.moveY(yToAdd)
        self.botRight.moveY(yToAdd)

    def __str__(self) -> str:
        return ("Top Left: " + self.topLeft.__str__() + "\n" +
                "Top Right: " + self.topRight.__str__() + "\n" +
                "Bot Left: " + self.botLeft.__str__() + "\n" +
                "Bot Left: " + self.botRight.__str__() + "\n"
                )
