from pygame import *
import pygame

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

    def displayLines(self, WINDOW: Surface) -> None:
        for row in range(0, self.height): # 0 a 15
            pygame.draw.line(WINDOW, BLACK, (0, row * self.boxSize), (self.getScreenWidth(), row * self.boxSize))
        for column in range(0, self.width): # 0 10
            pygame.draw.line(WINDOW, BLACK, (column * self.boxSize, 0), (column * self.boxSize, self.getScreenHeight()))

    def displayBlocks(self) -> None:
        # TODO
        pass
