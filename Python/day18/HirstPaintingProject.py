import colorgram
import turtle as t
from pathlib import Path
import random
#realtive path 
# 'Python/day18/images/image.jpg'

#We can use Path file, with this we can say
#if main is here the path is Python/day18/images...
image_path = Path(__file__).parent / "images" / "image.jpg"


rgb_colors = []
colors = colorgram.extract(image_path, 35)
for color in colors:
    #ALl the information
    #rgb_colors.append(color.rgb)
    
    #If we wanted a list of tuples of only the values (not Rgb(r=2,g=5,b=9),RGB....)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    #Create the tuples
    newcolor = (r,g,b)
    #Added to the list
    rgb_colors.append(newcolor)

print(rgb_colors)
print(len(rgb_colors))

#remove an element by index and not value
#start:end not including "end"
del rgb_colors[0:2]

print(rgb_colors)

# We are going to paint a painting with 10 rows, and 10 columns 
# * Use turtle 
# * Each of the dots,
#   * Should have 20 of size, and 50 space apart

timmy = t.Turtle()
t.colormode(255)

#To hide turtle
timmy.hideturtle()

#We have a function call goto(CoordX, CoordY)

# Draw a grid of dots
for i in range(10):
    timmy.penup()
    timmy.goto(1, i*50)
    for j in range(10):
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        timmy.dot(10, random.choice(rgb_colors)) #change the color everytime 

        
screen = t.Screen()
screen.exitonclick()