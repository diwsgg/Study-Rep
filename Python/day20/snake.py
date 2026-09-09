from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0),]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.allturtles = []
        self.create_snake()

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            newTurtles = Turtle(shape="square")
            newTurtles.color("white")
            newTurtles.penup()
            newTurtles.goto(positions)
            self.allturtles.append(newTurtles)

#movement
    def move(self):
        for seg_num in range(len(self.allturtles)-1, 0, -1):
            new_x = self.allturtles[seg_num-1].xcor()
            new_y = self.allturtles[seg_num-1].ycor()
            self.allturtles[seg_num].goto(new_x,new_y)
        self.allturtles[0].forward(MOVE_DISTANCE)
