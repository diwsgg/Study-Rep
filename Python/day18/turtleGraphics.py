from turtle import Turtle, Screen

#You can use a library with an alias like this
#import turtle as tut

#But you can not do import the methods from that alias
# from tut import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("red")

#DO the turtle draw a square

#1. way
def do_square():
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
do_square()

#Space
timmy.left(90)
timmy.forward(100)
timmy.right(90)

#2. way
for  _ in range(4):
    timmy.forward(100)
    timmy.right(90)

#Space
timmy.left(90)
timmy.forward(100)
timmy.right(90)

#Now we want to move forwards but also draw like this
# - - - - - - - >
#Where we draw some lines we left space and we continue drawing again

for _ in range(20):
    #By default we arestarting with pendown
    timmy.forward(10)
    #After we move 10 mts we do not draw for the same distance
    timmy.penup()
    #timmy.pencolor("white") #WE can simulate the same result changing the color for an amount of distance
    timmy.forward(10)
    #And we now draw for the next cicle
    timmy.pendown()
    #timmy.pencolor("blue")

#Space
timmy.left(90)
timmy.forward(100)
timmy.right(90)


screen = Screen()
screen.exitonclick()