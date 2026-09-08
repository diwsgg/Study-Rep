from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False

#Set up allow to set widht and hight
screen.setup(800,500)
#Pop up a dialog window for input a string
user_input = screen.textinput("Choose","What color do you prefer")

#Know we have to create another 6 turtles distribute in the screen, with different colors each one
colors = ["blue","cyan","brown","green","pink","red"]

#AS we can see in turtle race its a lot of code
#SO we are goint to reduce it
y_positions = [-70,-40,-10,20,50,80]

#WE have created the turtle but the one of them need to have color that the user inputs, and the other ones different color
# for index in range(0,6):
#     newTurtle = Turtle(shape="turtle")
#     newTurtle.penup()
#     newTurtle.goto(x=-390,y=y_positions[index])

#A list of turtles/objects
list_turtles = []
for index in range(0,6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.color(colors[index])
    newTurtle.penup()
    newTurtle.goto(x=-390,y=y_positions[index])
    list_turtles.append(newTurtle)

#We need to move that turtles


if user_input:
    is_race_on = True

while is_race_on:
    #Lopp for all turtles
    for turtle in list_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor()>380:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_input:
                screen.title("Hello")
                print("You won")
            else:
                screen.title("Bye")
                print("You lose")
            is_race_on=False
            break

    

screen.exitonclick()