from pygame.locals import K_RIGHT, K_SPACE, KEYDOWN, KEYUP, K_LEFT
from pygame import Color, Vector2
from src.constants import BLACK, ENEMY_OFFSET, ENEMY_SPEED, EXTRA_ENEMIES_PER_LEVEL, EXTRA_ENEMY_SPEED_PER_LEVEL, INITIAL_NUM_ENEMIES, MAX_PER_ROW, NUMBER_OF_SHIELDS, ROW_GAP, SCREEN_H, SCREEN_W, WHITE
from src.entities.player import Player
from src.entities.enemy import Enemy
from src.entities.shield import Shield


class Game:
    score = 0
    entities: "list"

    def __init__(self):
        self.restart_game()
    
    def restart_game(self):
        self.entities = []
        self.player = Player()
        self.entities.append(self.player)
        self.num_active_enemies = 0
        self.level = 0

        self.start_next_level()

    def start_next_level(self):
        self.generate_enemies()
        self.generate_shields()

        self.level += 1

    def generate_enemies(self):
        extra_enemies = self.level * EXTRA_ENEMIES_PER_LEVEL
        extra_enemy_speed = self.level * EXTRA_ENEMY_SPEED_PER_LEVEL

        total_enemy_count = extra_enemies + INITIAL_NUM_ENEMIES
        self.num_active_enemies = total_enemy_count
        curr_enemy_speed = extra_enemy_speed + ENEMY_SPEED

        col_gap = SCREEN_W // MAX_PER_ROW

        col, row = 0, 0
        for _ in range(total_enemy_count):
            enemy_coords = Vector2(ENEMY_OFFSET + (col * col_gap), ENEMY_OFFSET + (row * ROW_GAP))
            new_enemy = Enemy(enemy_coords, curr_enemy_speed, "res/enemy-green.png")
            self.entities.append(new_enemy)

            col += 1
            if col >= MAX_PER_ROW:
                col = 0
                row += 1
    
    def generate_shields(self):
        n = NUMBER_OF_SHIELDS + 1
        for i in range(1, n):
            self.entities.append(Shield(i * SCREEN_W/n, 350))

    def handle_input(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.player.move_left()
                if event.key == K_RIGHT:
                    self.player.move_right()
                if event.key == K_SPACE:
                    if self.player.expired:
                        self.restart_game()
                    else:
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
                    self.score += 1
                del self.entities[i]

            obj.tick(delta, self.entities)

            obj.move(delta)

        Enemy.random_enemy_shoot(
            self.entities, self.num_active_enemies, delta, NUM_ENEMIES_SHOOT=2)
        
        if self.num_active_enemies == 0:
            self.start_next_level()

    def render_text(self, display, font, text: str, color: Color, position: Vector2):
        surface = font.render(text, True, color)
        display.blit(surface, position)

    def render(self, display, font):
        display.fill(BLACK)

        if not self.player.expired:
            for obj in self.entities:
                obj.render(display)
            self.render_text(display, font, f"Level: {self.level}", WHITE, (50, 50))
            self.render_text(display, font, f"Health: {self.player.health}", WHITE, (50, 100))
        else:
            self.render_text(display, font, "Game Over. Press SPACE to start again!", WHITE, (SCREEN_W // 2 - 200, SCREEN_H // 2))
