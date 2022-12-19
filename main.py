import time
from wall import Wall
import ion
from snake import Game
from apple import Apple
import draw
from kandinsky import display

fps = (1.0 / 3.0)


def get_direction(direction):
    if ion.keydown(ion.KEY_DOWN) and direction != "up":
        return "down"
    elif ion.keydown(ion.KEY_LEFT) and direction != "right":
        return "left"
    elif ion.keydown(ion.KEY_UP) and direction != "down":
        return "up"
    elif ion.keydown(ion.KEY_RIGHT) and direction != "left":
        return "right"
    else:
        return None


SCREEN_WIDTH = 320
SCREEN_HEIGHT = 220

y = 0
walls = []
x = 10
while y < SCREEN_HEIGHT:
    walls.append(Wall(0, y))
    walls.append(Wall(SCREEN_WIDTH - 10, y))
    y += 10

walls.pop(-2)

while x < SCREEN_WIDTH:
    walls.append(Wall(x, 0))
    walls.append(Wall(x, SCREEN_HEIGHT - 8))
    x += 10

game = Game([[int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)]], 0, Apple(30, 30), walls)
direction = "down"
draw.draw_walls(walls)
draw.draw_string(str(game.score), 0, SCREEN_HEIGHT - 15)
draw.draw_apple(game.apple)
if __name__ == "__main__":
    while not ion.keydown(ion.KEY_PLUS):
        draw.draw_main_menu()
    while True:
        start = time.time()
        while time.time() - start < fps:
            change = get_direction(direction)
            if change is not None:
                direction = change
                end = time.time()
                time.sleep(fps + 0.1 - (end - start))
                break
            end = time.time()

        if direction == "down":
            game.move(0, 10)
        if direction == "up":
            game.move(0, -10)
        if direction == "left":
            game.move(-10, 0)
        if direction == "right":
            game.move(10, 0)

        if game.over:
            break

        if game.snake[0] == [game.apple.x, game.apple.y]:
            game.apple.new_pos()
            game.add_score()

            if direction == "down":
                game.add_to_snake([game.snake[len(game.snake)-1][0], game.snake[len(game.snake)-1][1] - 10])
            if direction == "up":
                game.add_to_snake([game.snake[len(game.snake)-1][0], game.snake[len(game.snake)-1][1] + 10])
            if direction == "left":
                game.add_to_snake([game.snake[len(game.snake)-1][0] + 10, game.snake[len(game.snake)-1][1]])
            if direction == "right":
                game.add_to_snake([game.snake[len(game.snake)-1][0] - 10, game.snake[len(game.snake)-1][1]])

        display(True)
        draw.clear()
        draw.draw_apple(game.apple)
        draw.draw_string(str(game.score), 0, SCREEN_HEIGHT - 15)
        draw.draw_snake(game.snake)
    draw.draw_game_over(game.score)
    time.sleep(2.5)
