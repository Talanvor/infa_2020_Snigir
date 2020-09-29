from random import randint
import turtle


number_of_turtles = 10
steps_of_time_number = 100


pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.left(randint(0, 359))
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
    for unit in pool:
        if (unit.xcor() > 200) or (unit.xcor() < -200):
            unit.left(180 - 2*unit.heading())
        if (unit.ycor() > 200) or (unit.ycor() < -200):
            unit.right(2*unit.heading())
        unit.forward(20)

exit()