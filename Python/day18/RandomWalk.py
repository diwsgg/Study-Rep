import turtle
import random 

timmy = turtle.Turtle()
turtle.colormode(255)

#We are going to draw a random walk, that means everytime moves its gonna decide if turn left, right, 
#What i see its first decide to turn left, right, up or down, and the we move, and the cicle repeats

#WE can just move and with an angle we can do all the directions 
movements = [0,90,180,270]

#Each time the color will be random for the new direction
#colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

#Another way for colors

#pencolor() accepts string or r,g,b so those are 3 values from 1.0 to 255
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_tuple = (r,g,b)
    return color_tuple

timmy.pensize(10)
timmy.speed("fastest")
for _ in range(100):
    #Chose a color and a direction
    #color = random.choice(colors)
    #direction = random.choice(movements)
    timmy.pencolor(random_color())
    timmy.forward(100)
    timmy.setheading(random.choice(movements))
    

screen = turtle.Screen()
screen.exitonclick()