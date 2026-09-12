import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Objs
user = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()

screen.onkeypress(user.moveUp, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.0001)

    screen.update()

    #SO the logic is, if the user get to the top of the screen pass the level and start again 
    if user.ycor()>=280:
        user.resetPosition()
        score.printingScore()
        cars.NewTurtle()
    cars.Movement()

    #detect if some car hit us
    




screen.exitonclick()