import pygame

from game_object import GameObject
# If we have more colors, consider a colors.py
from objects.Player import Player

BLACK = (0, 0, 0)

class SpaceInvaders:
    """Game implementation of Space Invaders"""
    game_objects = []

    # TODO set up game player object, aliens etc
    def __init__(self):
        self.game_objects.append(Player())

    def update(self, delta, events):
        for obj in self.game_objects:
            obj.update(delta, events)

    def render(self, display):
        display.fill(BLACK)
        for obj in self.game_objects:
            obj.render(display)
