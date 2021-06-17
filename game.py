import pygame

from game_object import GameObject
# If we have more colors, consider a colors.py
from objects.player import Player

BLACK = (0, 0, 0)


class SpaceInvaders:
    """Game implementation of Space Invaders"""
    game_objects: list[GameObject] = []

    # TODO set up game player object, aliens etc
    def __init__(self):
        self.game_objects.append(Player())

    def update(self, delta: int, events: list[pygame.event.Event]):
        for obj in self.game_objects:
            obj.update(delta, events)

    def render(self, display: pygame.Surface):
        display.fill(BLACK)
        for obj in self.game_objects:
            obj.render(display)
