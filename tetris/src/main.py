import pygame
from pygame.locals import *

pygame.init()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# window
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# settings
BOX_SIZE = 50
GRID_SIZE = (10, 20) # 10 de large, 20 de haut
SPEED = 1000 # vitesse du deplacement vertical du block

# rects
rectangle: Rect = pygame.Rect(10, 10, BOX_SIZE, BOX_SIZE)
move_x: int = 50


def main():
    # start_time = int(time())
    # time:int = int(thread_time())
    time: int = 0

    running = True
    while running:
        # main displaying
        WINDOW.fill(WHITE)

        pygame.draw.rect(WINDOW, BLACK, rectangle)
        if (time == 0):
            rectangle.y += BOX_SIZE


        # events
        for event in pygame.event.get():
            # keys
            if (event.type == pygame.KEYDOWN):
                print("KEYDOWN")
                if (event.key == pygame.K_q):
                    rectangle.x -= BOX_SIZE
                if (event.key == pygame.K_d):
                    rectangle.x += BOX_SIZE

            # quit
            if event.type == pygame.QUIT:
                running = False


        pygame.display.flip()
        # clock allant de 0 a 1000: quand la val est a 0, on move le block vers le bas
        time = (time + 1) % SPEED

    pygame.quit()


if __name__ == "__main__":
    main()
