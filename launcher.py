import pygame
from pygame.locals import QUIT

from constants import SCREEN_H, SCREEN_W, FPS
from game import SpaceInvaders


def main():
    # Use this to render anything to the screen (of type pygame.Surface)
    display = pygame.display.set_mode((SCREEN_W, SCREEN_H), 0, 32)

    running = True
    game = SpaceInvaders()
    game_clock = pygame.time.Clock()
    while running:
        # Game Loop
        delta = game_clock.tick(FPS)
        events = pygame.event.get()
        game.update(delta, events)
        game.render(display)
        pygame.display.update()

        # Events not related to the game
        for e in events:
            if e.type == QUIT:
                running = False


if __name__ == "__main__":
    main()
