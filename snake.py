SCREEN_WIDTH = 320
SCREEN_HEIGHT = 220


class Game:
    def __init__(self, snake, score, apple, walls, over=False, ):
        self.walls = walls
        self.apple = apple
        self.score = score
        self.snake = snake
        self.over = over

    def add_score(self):
        self.score += 10

    def move(self, x, y):
        head = self.snake
        if x < 10 or x > SCREEN_WIDTH - 20 or y < 10 or y > SCREEN_HEIGHT - 20:
            self.over = True
            return

        while head is not None:
            if head.pos == (x, y):
                self.over = True
                return
            head = head.following

        self.snake.move((x, y))

    def add_to_snake(self, part):
        head = self.snake
        while head.following is not None:
            head = head.following
        head.following = part
