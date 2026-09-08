from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

# def move_Forwards():
#     timmy.forward(10)

# screen.listen()
# screen.onkey(key="d", fun=move_Forwards)
# screen.exitonclick()

#So now we wanted to create a for timmy
# to move in all directions with ours keys

#w
def move_Forwards():
    timmy.forward(10)

#s
def move_Backwards():
    timmy.backward(10)
#a
def move_Counter_Clockwise():
    #timmy.setheading(timmy.heading()+10) 
    timmy.left(10)
#d
def move_Clockwise():
    timmy.right(10)  

#clear the screen
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

def movements():
    screen.listen()
    screen.onkey(key='w', fun=move_Forwards)
    screen.onkey(key='s', fun=move_Backwards)
    screen.onkey(key='a', fun=move_Counter_Clockwise)
    screen.onkey(key='d', fun=move_Clockwise)
    screen.onkey(key='space', fun=clear)

movements()

screen.exitonclick()