from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random

# Create object of screen class
screen = Screen()
# Create object of food class
food = Food()
# Create object of scoreboard class
scoreboard = Scoreboard()

# Create method to setup screen
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
# Create object of snake class
snake = Snake()
# Create method to control the snake using keyboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# Start the game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280,280))
        scoreboard.increase_score()





# Exit on click
screen.exitonclick()
