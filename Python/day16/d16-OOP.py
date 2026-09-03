#In Python files we do not have to worry about running the code, without restarting something for turtle
import turtle

#This will create an object from turtle
# With the name of "timmy"
timmy = turtle.Turtle() #THAT CREATES A SCREEN

my_screen = turtle.Screen() #IF A SCREEN ALREADY EXISTS, IT DOES NOT CREATE ANOTHER ONE 
#THIS WILL  BE REPRESENTEND AS

'''
              ┌─────────────────┐
              │  Turtle Screen  │
              │                 │
              │     Timmy 🐢    │
              └─────────────────┘
                    ↑       ↑
                    │       │
             Turtle()    Screen()
'''

#This will gave us the address of where is timmy on the stack
print(timmy)

timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
print(my_screen.canvheight)
my_screen.exitonclick()


#Now we are gonna user prettyTable

#import prettytable
from prettytable import PrettyTable

# Create a PrettyTable object and save it to a variable called table
table = PrettyTable()
print(table)

table.add_column("Pokemon Name ",["Pikachu","Squirtle","Charmander"])
table.add_column("Type ",["Electric","Water","Fire"])

print(table)