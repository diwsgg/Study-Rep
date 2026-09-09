#We are going to create the Snake game

#We have to do 7 steps
'''
1. Create a snake body

2. Move the snake

3. Create a snake food

4. Detect collision with food

5. Create a scoreboard

6. Detect collision with wall

7. Detect collision with tail

'''

from turtle import Screen, Turtle
import time
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame")

#to not notice we have an update for moving our snake
screen.tracer(0)

#1 Step (create the snake)
#The snake body has to be 3 squares line each other

#First at 0,0 20px, then 20px on the left the other one, and 20px of the left of the other one the next one
all_turtles = []
for turtle in range(3):
    #We need to define the shape is a square,color and not to draw any line where they go
    newTurtles = Turtle(shape="square")
    newTurtles.color("white")
    newTurtles.penup()
    
    #Now we put the coordenates
    #As they are on the left, y=0, x-->how
    #(*-20) since 0*20 its 0, but 1*-20=-20, 2*-20=-40 and its 20px of distance of each one
    newTurtles.goto(turtle*-20,0)
    
    #We add those turtles into a list of objects
    all_turtles.append(newTurtles)



#2 Step (move the snake)
game_on = True

#This will only move it now straight 
'''
while game_on:
    screen.update()
    for snake in all_turtles:
        snake.forward(0.5)
'''
#If we wanted to move up, all will be moving up, but has to be the head first and then all has to move in sequence
#So for this we are going to do a loop, where from the tail to previous head we are going to take that coordenate
#and the head will move only, this will be moving first the tail that the head, but this will update everything ok
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(all_turtles)-1, 0, -1):
        new_x= all_turtles[seg_num-1].xcor()
        new_y= all_turtles[seg_num-1].ycor()
        all_turtles[seg_num].goto(new_x,new_y)
    all_turtles[0].forward(20)

screen.exitonclick()

#We are goint to do all by classes ()