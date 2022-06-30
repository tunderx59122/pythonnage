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
            # pygame.draw.rect(WINDOW, color, rect)
            pygame.draw.rect(WINDOW, color, rect, width = 2, border_radius = 2, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)

    def moveDown(self) -> None:
        for rect in self.rects:
            rect.y += self.boxSize
        
    def canMoveDown(self, HEIGHT) -> bool:
        for rect in self.rects:
            if (rect.y + self.boxSize >= HEIGHT):
                return False
        return True

    def canMoveRight(self, WIDTH: int) -> bool:
        for rect in self.rects:
            if (rect.x + self.boxSize >= WIDTH):
                return False
        return True

    def canMoveLeft(self, WIDTH: int) -> bool:
        for rect in self.rects:
            if (rect.x <= 0):
                return False
        return True

    def moveRight(self) -> None:
        for rect in self.rects:
            rect.x += self.boxSize

    def moveLeft(self) -> None:
        for rect in self.rects:
            rect.x -= self.boxSize