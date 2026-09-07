import turtle
import random 

timmy = turtle.Turtle()
turtle.colormode(255)

timmy.speed("fastest")

# we are goint to draw N circles with 100 of radius
# ALl in the center, each one of a random color

#To draw a circle we do 
# Draw a circle with radius 100
#timmy.circle(100)

#Now we need to change the direction that we are, 
# we can calculate the number of the changes we are gonna do with the number of circle drawing like

#cicleschanges = 360/5

#Now do all in a cicle

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_tuple = (r,g,b)
    return color_tuple

def draw_circles(numCircles):
    angle = 360/numCircles
    for _ in range(numCircles):
        #Chose a color and a direction
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.left(angle)


draw_circles(205)

screen = turtle.Screen()
screen.exitonclick()