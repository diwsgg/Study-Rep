import turtle
import random

timmy = turtle.Turtle()

screen = turtle.Screen()
screen.colormode(255)

# Disable automatic screen updates
screen.tracer(0)

timmy.speed("fastest")


def random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


def draw_circles(num_circles):
    angle = 360 / num_circles

    for _ in range(num_circles):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.left(angle)


draw_circles(260)

# Update the screen only once
screen.update()

screen.exitonclick()