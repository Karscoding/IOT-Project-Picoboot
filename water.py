import turtle
from math import sin
import math

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()
turtle.pencolor("blue")

# Set up the wave parameters
amplitude = 20
period = 20
steps = 50

# Draw the waves
for i in range(steps):
    turtle.clear()
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    for x in range(-100, 100):
        y = amplitude * math.sin((x / period) + (i * 0.1))
        turtle.goto(x, y)
    turtle.update()
