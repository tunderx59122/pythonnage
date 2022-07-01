import pygame
from pygame.locals import *

from Point import Point
from Shape import Shape
from Grid import Grid

def collidesDown(topRect: Rect, botRect: Rect) -> bool:
    return ((topRect.y + topRect.height >= botRect.y - 1) and (topRect.x == botRect.x))

def collidesLeft(rightRect: Rect, leftRect: Rect) -> bool:
    if (rightRect.x < leftRect.x):
        return False
    return ((rightRect.x <= leftRect.x + leftRect.width + 1) and (leftRect.y == rightRect.y))

def collidesRight(leftRect: Rect, rightRect: Rect) -> bool:
    if (leftRect.x > rightRect.x):
        return False
    return ((leftRect.x + leftRect.width >= rightRect.x - 1) and (leftRect.y == rightRect.y)) 

def moveRect(rect: Rect, plusX: int, plusY: int) -> None:
    rect.x += plusX
    rect.y += plusY

def moveTopRight(rect: Rect, boxSize: int) -> None:
    moveRect(rect, boxSize * 1, -boxSize * 1)
def moveBotRight(rect: Rect, boxSize: int) -> None:
    moveRect(rect, boxSize * 1, boxSize * 1)
def moveBotLeft(rect: Rect, boxSize: int) -> None:
    moveRect(rect, -boxSize * 1, boxSize * 1)
def moveTopLeft(rect: Rect, boxSize: int) -> None:
    moveRect(rect, -boxSize * 1, -boxSize * 1)

class Block:
    def __init__(self, topLeft: Point, shape: Shape, boxSize = 50) -> None:
        self.boxSize = boxSize
        self.rects: list[Rect] = []

        self.shape: Shape = shape

        self.rollIndex = 0 # int allant de 0 a 3 determinant la position de la rotation du block

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
        
    def hasGroundedNeihbours(self, grid: Grid):
        for rect in grid.groudedRects:
            for rect2 in self.rects:
                if (collidesDown(rect2, rect)):
                    return True
        return False
            


    def canMoveDown(self, grid: Grid) -> bool:
        for rect in self.rects:
            if (rect.y + self.boxSize >= grid.getScreenHeight()):
                return False
            
            # tester si les blocks alentours sont empty
            if (self.hasGroundedNeihbours(grid)):
                return False

        return True

    def canMoveRight(self, grid: Grid) -> bool:
        for rect in self.rects:
            if (rect.x + self.boxSize >= grid.getScreenWidth()):
                return False

            for rect2 in grid.groudedRects:
                if (collidesRight(rect, rect2)):
                    return False
        return True

    def canMoveLeft(self, grid: Grid) -> bool:
        for rect in self.rects:
            if (rect.x <= 0):
                return False
            
            for rect2 in grid.groudedRects:
                if (collidesLeft(rect, rect2)):
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

    def rollRight(self) -> None:
        if (self.shape == Shape.T):
            if (self.rollIndex == 0):
                moveTopRight(self.rects[1], self.boxSize)
                moveBotRight(self.rects[0], self.boxSize)
                moveBotLeft(self.rects[3], self.boxSize)
                # moveRect(self.rects[3], -self.boxSize * 1, self.boxSize * 1)
            elif (self.rollIndex == 1):
                moveBotRight(self.rects[1], self.boxSize)
                moveBotLeft(self.rects[0], self.boxSize)
                moveTopLeft(self.rects[3], self.boxSize)
            elif (self.rollIndex == 2):
                moveBotLeft(self.rects[1], self.boxSize)
                moveTopLeft(self.rects[0], self.boxSize)
                moveTopRight(self.rects[3], self.boxSize)
            elif (self.rollIndex == 3):
                moveTopLeft(self.rects[1], self.boxSize)
                moveTopRight(self.rects[0], self.boxSize)
                moveBotRight(self.rects[3], self.boxSize)
            # !!!! attention aux formes redondantes e.g le I a 2 etats donc test rollIndex == 0 ou 2
            self.rollIndex = (self.rollIndex + 1) % 4

    
    def rollLeft() -> None:
        pass