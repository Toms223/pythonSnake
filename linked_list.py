class LinkedList:
    def __init__(self, following, pos):
        self.following = following
        self.pos = pos

    def move(self, move):
        if self.following is not None:
            self.following.move(self.pos)
        self.pos = move
