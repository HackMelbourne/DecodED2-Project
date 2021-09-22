from pygame.locals import K_RIGHT, K_SPACE, KEYDOWN, KEYUP, K_LEFT
from pygame import Color, Vector2
from src.constants import BLACK, ENEMY_SPEED, WHITE
from src.entities.player import Player
from src.entities.enemy import Enemy


class Game:

    entities: "list"

    def __init__(self):
        self.entities = []
        self.player = Player()
        self.entities.append(self.player)
        self.generate_enemies()

    def generate_enemies(self):
        test_enemy_1 = Enemy(
            Vector2(100, 100), ENEMY_SPEED, 'res/enemy-blue.png')
        test_enemy_2 = Enemy(
            Vector2(150, 100), ENEMY_SPEED, 'res/enemy-green.png')
        test_enemy_3 = Enemy(
            Vector2(200, 100), ENEMY_SPEED, 'res/enemy-red.png')

        self.entities.append(test_enemy_1)
        self.entities.append(test_enemy_2)
        self.entities.append(test_enemy_3)

        self.num_active_enemies = 3

    def handle_input(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.player.move_left()
                if event.key == K_RIGHT:
                    self.player.move_right()
                if event.key == K_SPACE:
                    self.player.shoot()
            if event.type == KEYUP:
                if event.key == K_LEFT and self.player.move_direction < 0:
                    self.player.stop_moving()
                if event.key == K_RIGHT and self.player.move_direction > 0:
                    self.player.stop_moving()

    def update(self, delta):
        for i in range(len(self.entities) - 1, -1, -1):
            obj = self.entities[i]

            if obj.expired:
                if isinstance(obj, Enemy):
                    self.num_active_enemies -= 1
                del self.entities[i]

            obj.tick(delta, self.entities)

            obj.move(delta)

        Enemy.random_enemy_shoot(
            self.entities, self.num_active_enemies, delta, NUM_ENEMIES_SHOOT=2)

    def render_text(self, display, font, text: str, color: Color, position: Vector2):
        surface = font.render(text, True, color)
        display.blit(surface, position)

    def render(self, display, font):
        display.fill(BLACK)
        for obj in self.entities:
            obj.render(display)
        self.render_text(display, font, "Space Invaders", WHITE, (50, 50))
