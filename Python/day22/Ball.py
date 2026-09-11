from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        #x, y = position
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        # self.goto(0,0)
        self.xmove = .4
        self.ymove = .4
        self.moveSpeed = .0001


    def move(self):
        #The ball has to move x,y like a diagonal
        newx = self.xcor()+self.xmove
        newy = self.ycor()+self.ymove
        self.goto(newx,newy)

    #Bounce is for when hits a wall to change the direction
    def bounce(self):
        self.ymove *=-1

    def bounce2(self):
        self.xmove *=-1
        self.moveSpeed *= 0.9


    #return ball to the center
    def center(self):
        self.goto(0,0)
        self.moveSpeed = .0001
        self.bounce2()
        