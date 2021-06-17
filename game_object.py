import abc

import pygame
from pygame import Vector2


# TODO should we teach these concepts? Or stick to vanilla python?
# If not we can use pure python with no abc/other libs other than pygame


class GameObject(metaclass=abc.ABCMeta):
    position: Vector2
    velocity: Vector2

    # Could have acceleration but we won't have complex motion here.
    def __init__(self):
        self.position = Vector2()
        self.velocity = Vector2()

    def update(self, delta: int, events: list[pygame.event.Event]):
        """
        Update this object

        delta=the time since the last frame draw, used to ensure objects animate at the correct speed,
        regardless of FPS count. (aka runs the same on a potato, or a supercomputer. Only difference will be framerate)

        """
        self.position += delta * self.velocity

    @abc.abstractmethod
    def render(self, display: pygame.Surface):
        pass
