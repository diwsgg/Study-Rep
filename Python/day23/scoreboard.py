from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.teleport(-230,260)
        self.level = 0
        self.printingScore()

    def printingScore(self):
        self.clear()
        self.write(arg=f"Level {self.level}",align="center", font=(FONT))
        self.level+=1

    def GameOver(self):
        self.teleport(0,0)
        #self.clear()
        self.write(arg=f"GAME OVER",align="center", font=(FONT))

