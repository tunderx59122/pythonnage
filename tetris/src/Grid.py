from pygame import *
import pygame

# from Block import Block
# from Point import Point
# from Shape import Shape

BLACK = (0, 0, 0)

class Grid:
    def __init__(self, boxSize: int, width: int, height: int) -> None:
        self.boxSize = boxSize
        self.width = width
        self.height = height

        self.groudedRects: list[Rect] = []

    def getScreenWidth(self) -> int:
        return self.width * self.boxSize
    
    def getScreenHeight(self) -> int:
        return self.height * self.boxSize

    def displayLines(self, WINDOW: Surface, color) -> None:
        for row in range(0, self.height): # 0 a 15
            pygame.draw.line(WINDOW, color, (0, row * self.boxSize), (self.getScreenWidth(), row * self.boxSize))
        for column in range(0, self.width): # 0 10
            pygame.draw.line(WINDOW, color, (column * self.boxSize, 0), (column * self.boxSize, self.getScreenHeight()))

    def displayRects(self, WINDOW: Surface, color) -> None:
        # TODO
        for rect in self.groudedRects:
            pygame.draw.rect(WINDOW, color, rect, width = 2, border_radius = 2, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)
    
    # def generateRandomBlock(self, coords: Point) -> Block:
    #     # for shape in Shape.at
    #     pass
