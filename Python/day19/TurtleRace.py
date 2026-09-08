from turtle import Turtle, Screen
from random import sample



timmy = Turtle(shape="turtle")
screen = Screen()

#Set up allow to set widht and hight
screen.setup(800,500)

#Pop up a dialog window for input a string
user_input = screen.textinput("Choose","What color do you prefer")

#define the color and not draw the line
timmy.color(user_input)
timmy.penup()

#Start line, (left line)
timmy.goto(-390,180)

#Know we have to create another 6 turtles distribute in the screen, with different colors each one
colors = ["blue","cyan","brown","DarkViolet","green","pink"]

color2,color3,color4,color5,color6= sample(colors,5)

#Create objects
tim2 = Turtle(shape="turtle")
tim3 = Turtle(shape="turtle")
tim4 = Turtle(shape="turtle")
tim5 = Turtle(shape="turtle")
tim6 = Turtle(shape="turtle")
#Assign colors
tim2.color(color2)
tim3.color(color3)
tim4.color(color4)
tim5.color(color5)
tim6.color(color6)
#pen ups
tim2.penup()
tim3.penup()
tim4.penup()
tim5.penup()
tim6.penup()

#Positions, 
# timmy.goto(-390,240)
tim2.goto(-390,120)
tim3.goto(-390,60)

tim4.goto(-390,-60)
tim5.goto(-390,-120)
tim6.goto(-390,-180)


screen.exitonclick()
