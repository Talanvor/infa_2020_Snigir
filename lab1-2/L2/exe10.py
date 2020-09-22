import turtle
import numpy as m

turtle.shape('turtle')

Acc = 90

def CircleL (R):
    for i in range(Acc):
        turtle.forward(2 * m.pi * R / Acc)
        turtle.left(360 / Acc)

def CircleR (R):
    for i in range(Acc):
        turtle.forward(2 * m.pi * R / Acc)
        turtle.right(360 / Acc)

for i in range(3):
    CircleL(30)
    CircleR(30)
    turtle.left(60)

