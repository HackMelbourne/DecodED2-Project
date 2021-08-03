import pygame
from pygame.locals import QUIT

from src.constants import SCREEN_H, SCREEN_W, FPS
from src.game import Game

def main():
    # Initialize all pygame submodules
    pygame.init()

    # Use this to render anything to the screen (of type pygame.Surface)
    display  = pygame.display.set_mode((SCREEN_W, SCREEN_H), 0, 32)
    font = pygame.font.SysFont("Arial", 24)

    running = True
    game = Game()
    game_clock = pygame.time.Clock()
    while running:
        # Game Loop
        delta = game_clock.tick(FPS)
        events = pygame.event.get()
        game.handle_input(events)
        game.update(delta)
        game.render(display, font)
        pygame.display.update()

        # Events not related to the game
        for e in events:
            if e.type == QUIT: 
                running = False


if __name__ == "__main__":
    main()

