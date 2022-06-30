import pygame
from pygame.locals import *

from Point import Point
from Shape import Shape
from Grid import Grid


class Block:
    def __init__(self, topLeft: Point, shape: Shape, boxSize = 50) -> None:
        self.boxSize = boxSize
        self.rects: list[Rect] = []

        if (shape == Shape.I):
            self.rects.append(Rect(topLeft.getX(), topLeft.getY() + boxSize * 0, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX(), topLeft.getY() + boxSize * 1, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX(), topLeft.getY() + boxSize * 2, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX(), topLeft.getY() + boxSize * 3, boxSize, boxSize))
        
        if (shape == Shape.J):
            self.rects.append(Rect(topLeft.getX() + boxSize * 0, topLeft.getY() + boxSize * 0, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 0, topLeft.getY() + boxSize * 1, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 1, topLeft.getY() + boxSize * 1, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 2, topLeft.getY() + boxSize * 1, boxSize, boxSize))
        
        if (shape == Shape.L):
            self.rects.append(Rect(topLeft.getX() + boxSize * 0, topLeft.getY() + boxSize * 1, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 1, topLeft.getY() + boxSize * 1, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 2, topLeft.getY() + boxSize * 1, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 2, topLeft.getY() + boxSize * 0, boxSize, boxSize))
        
        if (shape == Shape.O):
            self.rects.append(Rect(topLeft.getX() + boxSize * 0, topLeft.getY() + boxSize * 0, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 1, topLeft.getY() + boxSize * 0, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 1, topLeft.getY() + boxSize * 1, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 0, topLeft.getY() + boxSize * 1, boxSize, boxSize))
        
        if (shape == Shape.S):
            self.rects.append(Rect(topLeft.getX() + boxSize * 0, topLeft.getY() + boxSize * 1, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 1, topLeft.getY() + boxSize * 1, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 1, topLeft.getY() + boxSize * 0, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 2, topLeft.getY() + boxSize * 0, boxSize, boxSize))
        
        if (shape == Shape.T):
            self.rects.append(Rect(topLeft.getX() + boxSize * 1, topLeft.getY() + boxSize * 0, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 0, topLeft.getY() + boxSize * 1, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 1, topLeft.getY() + boxSize * 1, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 2, topLeft.getY() + boxSize * 1, boxSize, boxSize))
        
        if (shape == Shape.Z):
            self.rects.append(Rect(topLeft.getX() + boxSize * 0, topLeft.getY() + boxSize * 0, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 1, topLeft.getY() + boxSize * 0, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 1, topLeft.getY() + boxSize * 1, boxSize, boxSize))
            self.rects.append(Rect(topLeft.getX() + boxSize * 2, topLeft.getY() + boxSize * 1, boxSize, boxSize))


    def display(self, WINDOW, color) -> None:
        for rect in self.rects:
            # pygame.draw.rect(WINDOW, color, rect)
            pygame.draw.rect(WINDOW, color, rect, width = 2, border_radius = 2, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)

        
    def canMoveDown(self, grid: Grid) -> bool:
        for rect in self.rects:
            if (rect.y + self.boxSize >= grid.getScreenHeight()):
                return False
        return True

    def canMoveRight(self, grid: Grid) -> bool:
        for rect in self.rects:
            if (rect.x + self.boxSize >= grid.getScreenWidth()):
                return False
        return True

    def canMoveLeft(self, grid: Grid) -> bool:
        for rect in self.rects:
            if (rect.x <= 0):
                return False
        return True

    def moveDown(self) -> None:
        for rect in self.rects:
            rect.y += self.boxSize

    def moveRight(self) -> None:
        for rect in self.rects:
            rect.x += self.boxSize

    def moveLeft(self) -> None:
        for rect in self.rects:
            rect.x -= self.boxSize

    def ground(self, grid: Grid) -> None: # pose le block O sol quand il peut plus descendre
        for rect in self.rects:
            grid.groudedRects.append(rect)
        self.rects.clear()