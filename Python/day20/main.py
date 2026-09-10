from turtle import Screen, Turtle
from snake import Snake
import time
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame")

screen.tracer(0)

#Create the objt 

snake = Snake()

#We need to listen the user (keys to move)
screen.listen()
#We need to define a function to detect when we move

#ON KEY TAKES TWO ARGUMENTS, a funct and a key, the function can be anything to determinate the movement of that key
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

#We are moving always, but the scree.onkey with list can be executed
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
screen.exitonclick()
