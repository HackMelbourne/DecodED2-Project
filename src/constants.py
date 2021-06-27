from pygame import Vector2

SCREEN_W = 800
SCREEN_H = 600
# If we have more colors, consider a colors.py
WHITE = (255, 255, 255)
# The target framerate of our game. Set to 0 for no limit
FPS = 144
# Bullet properities
BULLET_SPEED = 1
BULLET_COOLDOWN = 500 # In milliseconds

# Enemy Properties
ENEMY_SPEED = 0.3
TOTAL_GRID_SQUARES = 30
MAX_PER_ROW = 10         # Thus there will be TOTAL_GRID_SQUARES/MAX_PER_ROW rows for enemies
INITIAL_NUM_ENEMIES = 7
ROW_JUMP_SIZE = 7
ROW_GAP = 50

# Player properties
PLAYER_START_VECTOR = Vector2(370, 480)
PLAYER_START_SPEED = 0.8