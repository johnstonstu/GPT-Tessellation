import turtle
import tkinter as tk
import random

# Draw a polygon with a given number of sides and side length


def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(angle)

# Draw a tessellation of (3, 6, 3, 6) pattern


def tessellation_3_6_3_6(size, rows, cols):
    for row in range(rows):
        for col in range(cols):
            if (row + col) % 2 == 0:
                draw_polygon(3, size)
                turtle.forward(size)
            else:
                draw_polygon(6, size)
                turtle.forward(size)
        turtle.backward(cols * size)
        turtle.left(60)
        turtle.forward(size)
        turtle.right(60)

# Draw a tessellation of (4, 8, 8) pattern


def tessellation_4_8_8(size, rows, cols):
    for row in range(rows):
        for col in range(cols):
            if (row + col) % 2 == 0:
                draw_polygon(4, size)
                turtle.forward(size)
            else:
                draw_polygon(8, size)
                turtle.forward(size)
        turtle.backward(cols * size)
        turtle.left(90)
        turtle.forward(size)
        turtle.right(90)


def random_tessellation():
    turtle.clear()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()

    size = 30
    rows = 12
    cols = 12

    tessellations = [tessellation_3_6_3_6, tessellation_4_8_8]
    chosen_tessellation = random.choice(tessellations)
    chosen_tessellation(size, rows, cols)


def main():
    # Set up the turtle graphics window
    turtle_screen = turtle.Screen()
    turtle_screen.title("Random Tessellation Generator")
    turtle.speed(0)

    # Set up the tkinter window and button
    tk_root = tk.Tk()
    tk_root.withdraw()

    button = tk.Button(
        tk_root, text="Generate Random Tessellation", command=random_tessellation)
    button.pack()

    # Show the tkinter window and start the main event loop
    tk_root.deiconify()
    tk_root.mainloop()


main()
