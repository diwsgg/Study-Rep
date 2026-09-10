from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0),]
MOVE_DISTANCE = 20
#ANGLES
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.allturtles = []
        #We have created an array, and at same tim, we put the snakes into the array
        self.create_snake()
        #WE put the "head" as the first turtle created
        self.head = self.allturtles[0]
    
    def create_snake(self):
        for positions in STARTING_POSITIONS:
            newTurtles = Turtle(shape="square")
            newTurtles.color("white")
            newTurtles.penup()
            newTurtles.goto(positions)
            self.allturtles.append(newTurtles)

#movement
    def move(self):
        #we move first all the tail and then the head
        #if we move the head first 
        for seg_num in range(len(self.allturtles)-1, 0, -1):
            new_x = self.allturtles[seg_num-1].xcor()
            new_y = self.allturtles[seg_num-1].ycor()
            self.allturtles[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    #Directions
    #If the direction is the opposite we can not change our direction
    def up(self):
        #This means we can move up when we are like -> or <- but not down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
