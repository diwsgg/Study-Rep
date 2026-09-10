from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame")

screen.tracer(0)

#Create the objt 
snake = Snake()
food = Food()
scorebd = ScoreBoard()

#We need to listen the user (keys to move)
screen.listen()
#We need to define a function to detect when we move

#ON KEY TAKES TWO ARGUMENTS, a funct and a key, the function can be anything to determinate the movement of that key
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
counter = 0
#We are moving always, but the scree.onkey with list can be executed
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Check if we eat the food (collision with the obj food)
    if snake.head.distance(food) < 15:
        #need to create another food but also deleate the one that we put on the screen
        #WE can change the logic, we can create a method to put the objt into a new direction
        #And just call that method without creating a new obj
        food.refresh()
        #increase the score
        scorebd.counter()
    #Also need to increase the size of the snake...
        snake.extend()
    #Check if we have a collision with a wall
    if abs(snake.head.xcor())>290 or abs(snake.head.ycor())>290:
        scorebd.gameOver()  
        game_on=False
    
    #check if we have collision with ourselfs (tail)


screen.exitonclick()
