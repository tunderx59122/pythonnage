from Point import Point

class Box:
    def __init__(self, topLeftPos:Point, size:int = 5) -> None:
        # Box = carre compose de 4 points: topLeft, botLeft, topRight, botRight
        # plus simple pour gerer le collisions
        # size = 5 par default
        self.topLeft = Point(topLeftPos.getX(), topLeftPos.getY())
        self.topRight = Point(topLeftPos.getX() + size, topLeftPos.getY())
        self.botLeft = Point(topLeftPos.getX(), topLeftPos.getY() + size)
        self.botRight = Point(topLeftPos.getX() + size, topLeftPos.getY() + size)

        self.size = size