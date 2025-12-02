from turtle import Turtle, Screen
# Creating a turtle and screen instance
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.heading() + 10

def turn_right():
    tim.heading() - 10

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Setting up key bindings
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
clear_drawing()
