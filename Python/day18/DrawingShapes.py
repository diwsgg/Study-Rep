from turtle import Turtle, Screen
import random 
timmy = Turtle()

#We are going to draw the next figures
# Triangule-3
# Square-4
# Pentagone-5
# Hexagon-6
# Heptagon-7
# Octogan-8
# nonagon-9
# Decagon-10

#Each figure need a random color
# SO we can create a list of colors and with random.choice choose one, but has to not be the same, for that we can use sample?
# But we can not repeat colors? We can, just not one after other the same

colors = ["blue","cyan","brown","chartreuse","DarkViolet","gray","lavender","gold","green","pink","snow"]

#WE start with the triangule, we know how many sides have the figures so we can divide the 360/number of sides


#The range is from 3 to 10 (inclusive 10)
def drawing():
    for i in range(3,11):
        #We assing the color
        color = random.choice(colors)
        timmy.pencolor(color)
        #WE calculate the angle
        angle = 360/i
        for _ in range(i):
            #WE are moving i times 
            timmy.forward(100)
            timmy.right(angle)

#Then we start to move 
drawing()


#for the first time we can move our point for the first vertice 


screen = Screen()
screen.exitonclick()