import pygame
from pygame.locals import *

from Block import Block
from Point import Point
from Shape import Shape
from Grid import Grid

pygame.init()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# settings
BOX_SIZE = 50
WIDTH = 10 # en nbr de box sur l'ecran
HEIGHT = 15
SPEED = 1000 # vitesse du deplacement vertical du block

grid: Grid = Grid(BOX_SIZE, WIDTH, HEIGHT)


# window
WINDOW = pygame.display.set_mode((grid.getScreenWidth(), grid.getScreenHeight()))
pygame.display.set_caption("Tetris")


# rects
# rectangle: Rect = pygame.Rect(10, 10, BOX_SIZE, BOX_SIZE)
# move_x: int = 50

# block
i_block = Block(Point(0, 0), Shape.I)

def main():
    # start_time = int(time())
    # time:int = int(thread_time())
    time: int = 0

    running = True
    while running:
        # main displaying
        WINDOW.fill(WHITE)

        # block principal
        i_block.display(WINDOW, BLACK)

        grid.displayLines(WINDOW)

        # tout les x sec: descendre le block
        if (time == 0):
            if (i_block.canMoveDown(grid)):
                i_block.moveDown()
            else:
                # ground tout les rects du block O sol
                i_block.ground(grid)

        # events
        for event in pygame.event.get():
            # keys
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_q):
                    if (i_block.canMoveLeft(WIDTH)):
                        i_block.moveLeft()
                if (event.key == pygame.K_d):
                    if (i_block.canMoveRight(WIDTH)):
                        i_block.moveRight()

            # quit
            if event.type == pygame.QUIT:
                running = False


        pygame.display.flip()
        # clock allant de 0 a 1000: quand la val est a 0, on move le block vers le bas
        time = (time + 1) % SPEED

    pygame.quit()


if __name__ == "__main__":
    main()
