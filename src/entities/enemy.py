from pygame import Vector2
import random

from src.constants import ENEMY_BULLET_COOLDOWN, ENEMY_BULLET_SPEED, ENEMY_OFFSET, ROW_JUMP_SIZE
from src.entity import Entity
from src.entities.bullet import Bullet
from src.sound import enemy_death


class Enemy(Entity):

    bullet_cooldown = ENEMY_BULLET_COOLDOWN

    turn: bool
    direction: int
    speed: int

    static_id = 1

    def __init__(self, coords, speed, image):
        super().__init__(coords.x, coords.y, 35, 35, image)
        self.turn = False
        self.direction = 1
        self.speed = speed
        self.id = self.static_id
        self.static_id += 1

    def tick(self, delta, objects):

        # Turn the enemy object around upon hitting a wall
        if self.boundary_check():
            self.turn = True

        if self.turn:
            self.direction *= -1
            self.y += ROW_JUMP_SIZE
            self.turn = False

        # Check for collision with bullets
        for obj in objects:
            if isinstance(obj, Bullet) and obj.kill_player is False and self.colliderect(obj):
                enemy_death.play()
                self.kill()
                obj.kill()

        # Velocity = speed * direction
        self.velocity.x = self.speed * self.direction

    @staticmethod
    def random_enemy_shoot(objects, num_enemies, delta, NUM_ENEMIES_SHOOT=1):

        if num_enemies == 0:
            return

        if Enemy.bullet_cooldown >= ENEMY_BULLET_COOLDOWN:
            enemies_to_shoot = []
            index_arr = []
            count = 0

            for i in range(len(objects)):
                if isinstance(objects[i], Enemy):
                    index_arr.append(i)

            while count != NUM_ENEMIES_SHOOT:
                random_index = random.randint(0, len(index_arr) - 1)
                enemies_to_shoot.append(objects[index_arr[random_index]])
                count += 1

            for enemy in enemies_to_shoot:
                objects.append(Bullet(Vector2(enemy.x, enemy.y),
                               ENEMY_BULLET_SPEED, KILL_PLAYER=True))

            Enemy.bullet_cooldown = 0
        else:
            Enemy.bullet_cooldown += delta
