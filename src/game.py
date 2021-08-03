from pygame import Vector2, Color
from pygame.locals import K_SPACE, K_LEFT, K_RIGHT, KEYDOWN, KEYUP

from src.constants import BLACK, WHITE

class Game:

    """Implementation of overall game logic"""
    entities: "list"

    def __init__(self):
        self.entities = []

    def handle_input(self, events):
        for event in events:
            
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    print("Move left")
                if event.key == K_RIGHT:
                    print("Move right")
                if event.key == K_SPACE:
                    print("Shoot!")
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    print("Stop moving left")
                if event.key == K_RIGHT:
                    print("Stop moving right")

    def update(self, delta):
        # Loop through game objects
        # We are iterating backwards here
        for i in range(len(self.entities) - 1, -1, -1):
            obj = self.entities[i]

            # Execute entity specific logic

            # Move the entity

    def render_text(self, display, font, text: str, color: Color, position: Vector2):
        surface = font.render(text, True, color)
        display.blit(surface, position)

    def render(self, display, font):
        display.fill(BLACK)
        
        # Loop through the entities and render each entity
            
        self.render_text(display, font, "Space Invaders", WHITE, (50, 50))

