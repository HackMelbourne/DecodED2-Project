from pygame import Vector2

SCREEN_W = 800
SCREEN_H = 600
# If we have more colors, consider a colors.py
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# The target framerate of our game. Set to 0 for no limit
FPS = 144
# Bullet properities
PLAYER_BULLET_SPEED = 1
ENEMY_BULLET_SPEED = 0.4
PLAYER_BULLET_COOLDOWN = 500  # In milliseconds
ENEMY_BULLET_COOLDOWN = 1500

# Enemy Properties
ENEMY_SPEED = 0.3
ENEMY_OFFSET = 50
TOTAL_GRID_SQUARES = 30
MAX_PER_ROW = 10  # Thus there will be TOTAL_GRID_SQUARES/MAX_PER_ROW rows for enemies
INITIAL_NUM_ENEMIES = 1
ROW_JUMP_SIZE = 35
ROW_GAP = 35

# Level system
EXTRA_ENEMIES_PER_LEVEL = 2
EXTRA_ENEMY_SPEED_PER_LEVEL = 0.05

# Player properties
PLAYER_START_VECTOR = Vector2(370, 480)
PLAYER_HEALTH = 5
PLAYER_SPEED = 0.8
# Shield properties
NUMBER_OF_SHIELDS = 4
