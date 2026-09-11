#LIbraries
from turtle import Screen
from Paddle import Padd
from Ball import Ball
from Score import ScoreBoard
import time

#Define the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)


#Create the objs
padd1 = Padd((350,0))
padd2 = Padd((-350,0))
ball = Ball()
scores = ScoreBoard()

#Movements
screen.listen()

screen.onkeypress(padd1.moveUp,"Up")
screen.onkeypress(padd1.moveDown,"Down")

screen.onkeypress(padd2.moveUp,"w")
screen.onkeypress(padd2.moveDown,"s")

#game 
game_on = True
while game_on:
    time.sleep(ball.moveSpeed)
    screen.update()
    
    #print the scores
    scores.printing()

    #for the other padd2 it will be always moving from up to down

    #Move the ball
    ball.move()

    #Detect collision with wall
    if abs(ball.ycor())>280:
        ball.bounce()

    #Detect Collision with padd1, or padd2
    if (ball.distance(padd1)<50 or ball.distance(padd2)<50) and abs(ball.xcor())>340 :
         ball.bounce2()

    #If its not touching the padd then we can count on the score, 
    # If the baall is xcor()>390 is on side of the player that means is point for pc, and otherwise for user
    if ball.xcor()>=390:
        #Point for pc
        scores.increaseCounter(False)
        ball.center()
    elif ball.xcor()<=-390: 
        #point for user
        scores.increaseCounter(True)
        ball.center()


screen.exitonclick()
