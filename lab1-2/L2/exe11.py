import turtle
import numpy as m

turtle.shape('turtle')

Acc = 30

def CircleL (R):
    for i in range(Acc):
        turtle.forward(2 * m.pi * R / Acc)
        turtle.left(360 / Acc)

def CircleR (R):
    for i in range(Acc):
        turtle.forward(2 * m.pi * R / Acc)
        turtle.right(360 / Acc)

turtle.left(90)
for i in range(7):
    CircleL(50 + 10*(i+1))
    CircleR(50 + 10*(i+1))

