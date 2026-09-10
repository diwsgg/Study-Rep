from turtle import Turtle

class Padd(Turtle):
    def __init__(self, position):
        #x, y = position
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)


    def moveUp(self):
        #We need to verify that our "turtle" does not go out of the map
        # why 230 it is because the height is "600" divided by 2 "300" and for the stretch_wid that is 5
        # we have on camera 240 px that is almost 90px that we "lose"
        if self.ycor() < 230:
            new_y = self.ycor()+20
            #self.goto(0,new_y), its the same 
            self.sety(new_y)

    def moveDown(self):
        if self.ycor() > -230:
            new_y = self.ycor()-20
            self.sety(new_y)