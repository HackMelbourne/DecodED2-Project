import random

from pygame import Vector2

from game_object import GameObject
# If we have more colors, consider a colors.py
from objects.player import Player

from objects.enemy import Enemy
from constants import MAX_PER_ROW, ROW_GAP, SCREEN_W, TOTAL_GRID_SQUARES, INITIAL_NUM_ENEMIES

BLACK = (0, 0, 0)


def generate_enemies():
    enemy_list = []
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
        enemy_list.append(Enemy(enemy_coords))

    return enemy_list


class SpaceInvaders:
    """Game implementation of Space Invaders"""
    game_objects: list[GameObject] = []

    # TODO set up game player object, aliens etc
    def __init__(self):
        self.game_objects.append(Player())
        for enemy in generate_enemies():
            self.game_objects.append(enemy)

    def update(self, delta, events):
        # Loop through game objects and remove ones which are expired.
        # We are iterating backwards here
        for i in range(len(self.game_objects) - 1, -1, -1):
            obj = self.game_objects[i]
            obj.update(delta, events, self.game_objects)
            if obj.expired:
                del self.game_objects[i]

    def render(self, display):
        display.fill(BLACK)
        for obj in self.game_objects:
            obj.render(display)
