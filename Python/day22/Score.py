#WE can use turtle.write() to display the score inside the screen
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        #We are creating a new obj
        super().__init__()
        #Put the new objt in top
        self.penup()
        self.goto(0,260)
        #Then we can hide it
        self.hideturtle()
        #Put the text of white
        self.color("white")
        #ANd start the counting
        self.scorePc = 0
        self.scoreUser = 0
        self.printing()

    #HAve the count of 
    def printing(self):
        #WE clean the screen
        self.clear()
        #then print the score 
        self.write(arg= f'{self.scorePc} \t{self.scoreUser}', 
                   align="center", font=("Courier",24,"normal"))

    def increaseCounter(self,option):
        if option:
            self.scoreUser+=1
        else:
            self.scorePc+=1

    #PRINT GAME OVER
    def gameOver(self):
        #WE clean the screen
        self.clear()
        #get the objt to the center
        self.goto(0,0)
        #then print the score 
        self.write(arg= f'\aGAME OVER \nFinal Score: {self.scorePc-1} {self.scoreUser-1}'
                   , align="center", font=("Courier",24,"normal"))
