import pygame

WIDTH, HEIGHT = 900, 500

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
    