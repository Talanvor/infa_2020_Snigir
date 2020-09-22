import turtle
import numpy as m

turtle.shape('turtle')

Acc = 90

def Arc (R, phi):
    for i in range(round(Acc * phi / 360)):
        turtle.forward(2 * m.pi * R / Acc)
        turtle.right(360 / Acc)

turtle.left(90)
for i in range(4):
    Arc(60, 180)
    Arc(10, 180)
