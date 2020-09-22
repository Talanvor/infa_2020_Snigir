import turtle
import numpy as m

turtle.shape('turtle')

R = 50
turtle.penup()
turtle.forward(R)
turtle.left(90)
turtle.pendown()

N = 100
for i in range(N):
    turtle.forward(2 * m.pi * R / N)
    turtle.left(360 / N)
