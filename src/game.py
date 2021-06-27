import random

from pygame import Vector2
from pygame.locals import K_SPACE, K_LEFT, K_RIGHT, KEYDOWN, KEYUP, QUIT

from src.entity import Entity
# If we have more colors, consider a colors.py
from src.entities.player import Player
from src.entities.bullet import Bullet

from src.entities.enemy import Enemy
from src.constants import MAX_PER_ROW, ROW_GAP, SCREEN_W, TOTAL_GRID_SQUARES, INITIAL_NUM_ENEMIES

BLACK = (0, 0, 0)

class Game:
    """Implementation of overall game logic"""
    def __init__(self):
        self.entities = []
        self.player = Player()
        self.entities.append(self.player)
        self.generate_enemies()

    def generate_enemies(self):
        coords_check = []
        OFFSET = 50

        NUM_ROWS = TOTAL_GRID_SQUARES // MAX_PER_ROW
        COL_GAP = SCREEN_W // MAX_PER_ROW

        for i in range(NUM_ROWS):
            coords_check.append([0 for x in range(MAX_PER_ROW)])

        for num in range(INITIAL_NUM_ENEMIES):
            rand_row = random.randint(0, NUM_ROWS - 1)
            rand_col = random.randint(0, MAX_PER_ROW - 1)

            # This loop is done to ensure that randomly initialised coordinates do not repeat
            while True:
                rand_row = random.randint(0, NUM_ROWS - 1)
                rand_col = random.randint(0, MAX_PER_ROW - 1)
                if coords_check[rand_row][rand_col] == 0:
                    coords_check[rand_row][rand_col] = 1
                    break

            enemy_coords = Vector2(OFFSET + (rand_col * COL_GAP), OFFSET + (rand_row * ROW_GAP))
            self.entities.append(Enemy(enemy_coords))
    
    def handle_input(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.player.move_left()
                if event.key == K_RIGHT:
                    self.player.move_right()
                if event.key == K_SPACE:
                    if not self.player.expired:
                        self.player.shoot()
            if event.type == KEYUP:
                if event.key == K_LEFT and self.player.move_direction < 0:
                    self.player.stop_moving()
                if event.key == K_RIGHT and self.player.move_direction > 0:
                    self.player.stop_moving()

    def update(self, delta):
        # Loop through game objects and remove ones which are expired.
        # We are iterating backwards here
        for i in range(len(self.entities) - 1, -1, -1):
            # Kill expired entities
            obj = self.entities[i]
            if obj.expired:
                del self.entities[i]

            # Execute entity specific logic
            obj.tick(delta, self.entities)

            # Move the entity
            obj.move(delta)

    def render(self, display):
        display.fill(BLACK)
        for obj in self.entities:
            obj.render(display)
