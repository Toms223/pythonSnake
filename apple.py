from random import randint

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 220


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def new_pos(self):
        self.x = int(randint(10, SCREEN_WIDTH - 20) / 10) * 10
        self.y = int(randint(10, SCREEN_HEIGHT - 20) / 10) * 10
