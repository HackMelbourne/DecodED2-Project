import enum

GENERATIONS = 50
# Whether we are training. If false, we instead run the best bot
TRAIN_MODE = True
TRAINING_THREADS = 12
MIN_MAX_OUTPUT = [0, 1]
DELTA = 2

class Action(enum.Enum):
    MOVE_LEFT = 0
    MOVE_RIGHT = enum.auto()
    MOVE_LEFT_AND_SHOOT = enum.auto()
    MOVE_RIGHT_AND_SHOOT = enum.auto()
    SHOOT = enum.auto()
    DO_NOTHING = enum.auto()