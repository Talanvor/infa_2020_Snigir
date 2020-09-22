import turtle
import numpy as m

turtle.shape('turtle')

Acc = 90

def Nbody(N, R):
    turtle.penup()
    turtle.left(90/N)
    turtle.forward(R)
    turtle.left(180 - 90/N)
    turtle.pendown()
    for i in range(N):
        turtle.forward(2*R*m.abs(m.sin(90/N)))
        turtle.left(180 - 180/N)
    turtle.penup()
    turtle.left(90/N)
    turtle.forward(R)
    turtle.left(180 - 90/N)
    turtle.pendown()

Nbody(5, 100)
turtle.penup()
turtle.forward(300)
turtle.pendown()
Nbody(11, 100)
