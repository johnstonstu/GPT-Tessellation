import turtle


def draw_hexagon(size):
    for _ in range(6):
        turtle.forward(size)
        turtle.left(60)


def hexagon_row(size, count):
    for _ in range(count):
        draw_hexagon(size)
        turtle.forward(size)


def hexagon_tessellation(size, rows, cols):
    turtle.speed(0)
    turtle.bgcolor("white")

    for row in range(rows):
        turtle.penup()
        turtle.goto(-size * cols / 2, size * 1.5 * row - size * rows / 2)
        turtle.pendown()

        # If it's an even row, draw one less hexagon
        hexagon_count = cols - (row % 2)
        hexagon_row(size, hexagon_count)

        # If it's an odd row, start with a horizontal offset
        if row % 2 == 1:
            turtle.penup()
            turtle.goto(-size * cols / 2 + size / 2, size *
                        1.5 * (row + 1) - size * rows / 2)
            turtle.pendown()


# Customize the tessellation pattern
size = 30
rows = 10
cols = 10

hexagon_tessellation(size, rows, cols)

turtle.done()
