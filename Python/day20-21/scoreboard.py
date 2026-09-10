#WE can use turtle.write() to display the score inside the screen
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        #We are creating a new obj
        super().__init__()
        #Put the new objt in top
        self.penup()
        self.goto(0,280)
        #Then we can hide it
        self.hideturtle()
        #Put the text of white
        self.color("white")
        #ANd start the counting
        self.score = 0
        self.counter()

    #HAve the count of 
    def counter(self):
        #WE clean the screen
        self.clear()
        #then print the score 
        self.write(arg= f"Score: {self.score}", align="center")
        #increase the score
        self.score+=1

    #PRINT GAME OVER
    def gameOver(self):
        #WE clean the screen
        self.clear()
        #get the objt to the center
        self.goto(0,0)
        #then print the score 
        self.write(arg= f"\aGAME OVER \nFinal Score: {self.score-1}", align="center", font=("Courier",24,"normal"))
