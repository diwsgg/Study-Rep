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
#GEt the time for create another car
last_car_time = time.time()

game_is_on = True
while game_is_on:
    time.sleep(0.0001)

    screen.update()

    #Move the cars
    cars.Movement()
    
    #How we can make for every 0.6 seconds add a new car, how? 
    current_time = time.time()
    if current_time - last_car_time >= 0.5:
        cars.NewTurtle()
        last_car_time = current_time

    #SO the logic is, if the user get to the top of the screen pass the level and start again 
    if user.resetPosition():
        score.printingScore()
        #increase the speed of the cars
        cars.Increase_Speed()

    #detect if some car hit us
    #For that we can see the distantce between one car and the user, for that we have to loop for all the objts of cars each one
    for car in cars.all_shapes:
        if user.distance(car)<28:
            score.GameOver()
            game_is_on = False


screen.exitonclick()