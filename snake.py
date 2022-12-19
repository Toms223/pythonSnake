SCREEN_WIDTH = 320
SCREEN_HEIGHT = 220


class Game:
    def __init__(self, snake, score, apple, walls, over=False):
        self.walls = walls
        self.apple = apple
        self.score = score
        self.snake = snake
        self.over = over

    def add_score(self):
        self.score += 10

    def move(self, x, y):
        if x + self.snake[0][0] < 10 or x + self.snake[0][0] > SCREEN_WIDTH - 20 or y + self.snake[0][1] < 10 or y + \
                self.snake[0][1] > SCREEN_HEIGHT - 20:
            self.over = True
            return
        if len(self.snake) > 1:
            for i in range(1, len(self.snake)):
                if self.snake[i][0] == x + self.snake[0][0] and self.snake[i][1] == y + self.snake[0][1]:
                    self.over = True
                    return
        if len(self.snake) == 1:
            self.snake[0][0] += x
            self.snake[0][1] += y
        else:
            previous = [self.snake[0][0], self.snake[0][1]]
            self.snake[0][0] += x
            self.snake[0][1] += y
            for i in range(1, len(self.snake)):
                temp = self.snake[i]
                self.snake[i] = previous
                previous = temp

    def add_to_snake(self, part):
        self.snake.append(part)
