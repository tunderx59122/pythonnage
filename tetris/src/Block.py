import pygame
from pygame.locals import *

from Point import Point
from Shape import Shape


class Block:
    def __init__(self, topLeft: Point, shape: Shape, boxSize = 50) -> None:
        self.boxSize = boxSize
        self.rects: list[Rect] = []

        if (shape == Shape.I):
            self.rects.append(Rect(topLeft.getX(), topLeft.getY() + boxSize * 0, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX(), topLeft.getY() + boxSize * 1, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX(), topLeft.getY() + boxSize * 2, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX(), topLeft.getY() + boxSize * 3, boxSize, boxSize))

    def display(self, WINDOW, color) -> None:
        for rect in self.rects:
            pygame.draw.rect(WINDOW, color, rect)

    def moveDown(self) -> None:
        for rect in self.rects:
            rect.y += self.boxSize