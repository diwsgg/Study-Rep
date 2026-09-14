COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = .05
MOVE_INCREMENT = 0.1

from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        #Position of each one at x=280 (right), but "y" a random one between (-280,280)
        self.all_shapes = []
        self.NewTurtle()
        self.speed = STARTING_MOVE_DISTANCE

    
    def createATurtle(self, Yposs):
        turtle = Turtle()
        turtle.penup()
        turtle.color(random.choice(COLORS))
        turtle.shape("square")
        turtle.shapesize(stretch_wid=1,stretch_len=2)
        #Start at right 
        turtle.goto(250, Yposs)
        self.all_shapes.append(turtle)

    def NewTurtle(self):
        #Only creating on Y coordenates
        Yposition = random.randrange(-250,280)
        self.createATurtle(Yposition)

    def Movement(self):
        #We are moving on X from right to left
        for car in self.all_shapes:
            car.setx(car.xcor() - self.speed)

        #Now for not have a large list we are deleting the cars that we "dont see"
        remaining_cars = []

        for car in self.all_shapes:
            if car.xcor() > -295:
                #Keep the cars that are on screen
                remaining_cars.append(car)
            else:
                #We hide the ones that are offside
                car.hideturtle()
        #WE update the list at the end for not have problmes between deleting and showing at same time
        self.all_shapes = remaining_cars

    def Increase_Speed(self):
        self.speed += MOVE_INCREMENT