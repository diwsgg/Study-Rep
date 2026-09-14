#WE can use turtle.write() to display the score inside the screen
from turtle import Turtle

#Create the path for the new file in the current dir
from pathlib import Path
#get the folder 
PATH_FOLDER = Path(__file__).parent
#and then only for the file
PATH_FILE = PATH_FOLDER / "data.txt" 

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
        #we need to read the data from our file
        with open(PATH_FILE,mode="r") as file:
            #Convert it to an int
            self.high_score = int(file.read())
        self.counter()

    #HAve the count of 
    def counter(self):
        #WE clean the screen
        self.clear()
        #then print the score 
        if self.high_score > 0:
            self.write(arg= f"Score: {self.score} High Score: {self.high_score-1}", align="center")
        else:
            self.write(arg= f"Score: {self.score} High Score: {self.high_score}", align="center")
        #increase the score
        self.score+=1

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            #Save our highscore
            with open(PATH_FILE,mode="w") as file:
                #We do not append the highscore only the highest and write it in the file
                #file.write(str(self.score))
                #we can do also
                file.write(f"{self.score}")
        self.score = 0
        self.counter()

    #PRINT GAME OVER
    def gameOver(self):
        #WE clean the screen
        self.clear()
        #get the objt to the center
        self.goto(0,0)
        #then print the score 
        self.write(arg= f"\aGAME OVER \nFinal Score: {self.score-1}", align="center", font=("Courier",24,"normal"))
        return True
