from src.constants import SCREEN_H
from src.entity import Entity

# Represents the bullet entity, spawned both by the player and enemy class

class Bullet(Entity):
    def __init__(self, player_position, bullet_speed, KILL_PLAYER=True):
        super().__init__(player_position.x + 12, player_position.y, 30, 30, 'res/bullet.png')

        self.velocity.y = -1 * bullet_speed
        self.kill_player = KILL_PLAYER
        if self.kill_player:
            self.velocity.y *= -1 
    
    def tick(self, delta, objects):
        # Despawn the bullet when it crosses boundaries
        if self.y < 0 or self.y > SCREEN_H:
            self.kill()

