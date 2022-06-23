from Box import Box
from Point import Point
from Shape import Shape


class Block:
    def __init__(self, shape:Shape, topLeftBox:Box) -> None:
        # shape -> forme du block
        
        self.boxes: list[Box] = []
        self.shape = shape

        if (shape == Shape.I):
            x = topLeftBox.topLeft.getX()
            y = topLeftBox.topLeft.getY()
            size = topLeftBox.size

            # pour i allant de topGauche jusque topGauche + 4 * la taille d'un block
            for countY in range(y, y + (size * 4), size):
                self.boxes.append(
                    Box(Point(x, countY))
                )

    def moveX(self, xToAdd: int) -> None:
        for box in self.boxes:
            box.moveX(xToAdd)

    def moveY(self, yToAdd: int) -> None:
        for box in self.boxes:
            box.moveY(yToAdd)

    def __str__(self) -> str:
        temp: str = self.shape.__str__() + ": \n"
        for box in self.boxes:
            temp += box.__str__() + "\n"
        return temp