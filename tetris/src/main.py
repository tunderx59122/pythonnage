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

def main():
    currentBlock = Block(Point(0, 0), Shape.T)
    # start_time = int(time())
    # time:int = int(thread_time())
    time: int = 0

    running = True
    while running:
        # main displaying
        WINDOW.fill(WHITE)

        # affichage du terr1: lignes + blocks grounded
        grid.displayLines(WINDOW, BLACK)
        grid.displayRects(WINDOW, BLACK)

        # current block
        currentBlock.display(WINDOW, BLACK)


        # tout les x sec: descendre le block
        if (time == 0):
            if (currentBlock.canMoveDown(grid)):
                currentBlock.moveDown()
            else:
                # ground tout les rects du block O sol
                currentBlock.ground(grid)
                currentBlock = Block(Point(0, 0), Shape.T)


        # events
        for event in pygame.event.get():
            # keys
            if (event.type == pygame.KEYDOWN):
                # move left/right
                if (event.key == pygame.K_q):
                    if (currentBlock.canMoveLeft(grid)):
                        currentBlock.moveLeft()
                if (event.key == pygame.K_d):
                    if (currentBlock.canMoveRight(grid)):
                        currentBlock.moveRight()
                # roll left/right
                if (event.key == pygame.K_a):
                    pass
                    # roll left
                if (event.key == pygame.K_e):
                    # roll right
                    print("pressed")
                    currentBlock.rollRight()

            # quit
            if event.type == pygame.QUIT:
                running = False


        pygame.display.flip()
        # clock allant de 0 a 1000: quand la val est a 0, on move le block vers le bas
        time = (time + 1) % SPEED

    pygame.quit()


if __name__ == "__main__":
    main()
