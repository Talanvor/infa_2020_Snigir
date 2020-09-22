import turtle
import numpy as m

turtle.shape('turtle')

N = 100
for j in range(1, 10, 1):
    for i in range(4):
        turtle.forward(20*j)
        turtle.left(90)
    turtle.penup()
    turtle.goto(-10*j, -10*j)
    turtle.pendown()
