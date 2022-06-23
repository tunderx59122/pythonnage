from Box import Box
from Point import Point
from Shape import Shape


class Block:
    def __init__(self, shape:Shape, topLeftBox:Box) -> None:
        # shape -> forme du block
        
        self.boxes: list[Box] = []

        if (shape == Shape.I):
            x = topLeftBox.topLeft.getX()
            y = topLeftBox.topLeft.getY()
            size = topLeftBox.size

            # pour i allant de topGauche jusque topGauche + 4 * la taille d'un block
            for countY in range(y, y + (size * 4), size):
                self.boxes.append(
                    Box(Point(x, countY))
                )