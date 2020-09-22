import turtle
import numpy as m

turtle.shape('turtle')

def Nbody (N, radius):
    turtle.penup()
    turtle.forward(radius)
    turtle.left(90 + 180/N)
    turtle.pendown()
    
    for i in range(N):
        turtle.forward(2 * radius * m.sin(m.pi / N))
        turtle.left(360 / N)

    turtle.penup()
    turtle.right(90 + 180/N)
    turtle.backward(radius)
    
for i in range(3, 10, 1):
    Nbody(i, 20*(i-2))

