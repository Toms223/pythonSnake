from kandinsky import fill_rect, draw_string

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 220


def draw_main_menu():
    draw_string("Snake", int(SCREEN_WIDTH / 2 - 25), int(SCREEN_HEIGHT/2), "black", "yellow")
    draw_string("Press + to begin", int(SCREEN_WIDTH / 2 - len("Press + to begin") * 5), int(SCREEN_HEIGHT/2) + 20, "black")


def draw_game_over(score):
    draw_string("Game Over", int(SCREEN_WIDTH / 2 - len("Game Over") * 5), int(SCREEN_HEIGHT/2), "red", "black")
    draw_string(f"Score: {score}", int(SCREEN_WIDTH / 2 - len(f"Score: ${score}") * 5), int(SCREEN_HEIGHT/2) + 20, "black")

def clear():
    fill_rect(10, 10, SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20, "white")


def draw_snake(snake):
    for part in snake:
        fill_rect(part[0], part[1], 10, 10, (255, 255, 0))


def draw_apple(apple):
    fill_rect(apple.x, apple.y, 10, 10, (255, 0, 0))


def draw_score(score):
    draw_string(score, 0, 500)


def draw_walls(walls):
    for wall in walls:
        fill_rect(wall.pos[0], wall.pos[1], 10, 10, "blue")
