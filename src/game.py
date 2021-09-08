from pygame.locals import K_RIGHT, K_SPACE, KEYDOWN, KEYUP, K_LEFT
from pygame import Color, Vector2
from src.constants import BLACK, WHITE
from src.entities.player import Player

class Game:

    entities: "list"

    def __init__(self):
        self.entities = []
        self.player = Player()
        self.entities.append(self.player)

    def handle_input(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.player.move_left()
                if event.key == K_RIGHT:
                    self.player.move_right()
                if event.key == K_SPACE:
                    print("Shoot bullet!")
            if event.type == KEYUP:
                if event.key == K_LEFT and self.player.move_direction < 0:
                    self.player.stop_moving()
                if event.key == K_RIGHT and self.player.move_direction > 0:
                    self.player.stop_moving()

    def update(self,delta):
        for i in range(len(self.entities) - 1, -1, -1):
            obj = self.entities[i]
            # Execute entity logic
            obj.tick(delta, self.entities)

            obj.move(delta)

    def render_text(self, display, font, text: str, color: Color, position: Vector2):
        surface = font.render(text, True, color)
        display.blit(surface, position)

    def render(self, display, font):
        display.fill(BLACK)
        for obj in self.entities:
            obj.render(display)
        self.render_text(display, font, "Space Invaders", WHITE, (50,50))