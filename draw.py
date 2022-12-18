from kandinsky import fill_rect, draw_string

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 220


def clear():
    fill_rect(10, 10, SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20, "white")


def draw_snake(snake):
    temp = snake
    while temp is not None:
        fill_rect(temp.pos[0], temp.pos[1], 10, 10, (255, 255, 0))
        temp = temp.following


def draw_apple(apple):
    fill_rect(apple.x, apple.y, 10, 10, (255, 0, 0))


def draw_score(score):
    draw_string(score, 0, 500)


def draw_walls(walls):
    for wall in walls:
        fill_rect(wall.pos[0], wall.pos[1], 10, 10, "blue")
