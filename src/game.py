from pygame.locals import K_SPACE, K_LEFT, K_RIGHT, KEYDOWN, KEYUP

BLACK = (0, 0, 0)

class Game:
    """Implementation of overall game logic"""
    def __init__(self):
        self.entities = []
    
    def handle_input(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    print("player move left")
                if event.key == K_RIGHT:
                    print("player move right")
                if event.key == K_SPACE:
                    print("player shoot!")
            if event.type == KEYUP:
                print("key up")

    def update(self, delta):
        # Loop through game objects and remove ones which are expired.
        # We are iterating backwards here
        for i in range(len(self.entities) - 1, -1, -1):
            
            print("execute entity specific logic for " + i + " and move entity")


    def render(self, display):
        display.fill(BLACK)
        for obj in self.entities:
            print("render object")

