import classes.solitaire as solitaire
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Solitaire")
    clock = pygame.time.Clock()

    game = solitaire.Solitaire()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 128, 0)) # green background