import turtle
import numpy as m

turtle.shape('turtle')

Acc = 90

def Circle (R):
    for i in range(Acc):
        turtle.forward(2 * m.pi * R / Acc)
        turtle.right(360 / Acc)

def Arc (R, phi):
    for i in range(round(Acc * phi / 360)):
        turtle.forward(2 * m.pi * R / Acc)
        turtle.right(360 / Acc)
        
turtle.penup()
turtle.backward(200)
turtle.left(90)
turtle.pendown()

turtle.begin_fill()
Circle(200)
turtle.color('yellow')
turtle.end_fill()

turtle.width(10)

turtle.color('black')
turtle.penup()
turtle.goto(-140, 100)
turtle.pendown()
turtle.begin_fill()
Circle(40)
turtle.end_fill()

turtle.penup()
turtle.goto(60, 100)
turtle.pendown()
turtle.begin_fill()
Circle(40)
turtle.end_fill()

turtle.color('blue')
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.goto(0, 0)

turtle.color('red')
turtle.penup()
turtle.goto(-70, -100)
turtle.pendown()
Arc(70, 180)
