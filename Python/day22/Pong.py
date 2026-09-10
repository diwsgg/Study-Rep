from turtle import Screen
from Paddle import Padd
from Ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)


#Create the objs
padd1 = Padd((350,0))
padd2 = Padd((-350,0))
ball = Ball()
#Movement
screen.listen()
screen.onkey(padd1.moveUp,"Up")
screen.onkey(padd1.moveDown,"Down")


screen.onkey(padd2.moveUp,"w")
screen.onkey(padd2.moveDown,"s")




game_on = True
while game_on:
    screen.update()
    #for the other padd2 it will be always moving from up to down

    #Move the ball
    ball.move()


screen.exitonclick()
