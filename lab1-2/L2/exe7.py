import turtle
import numpy as m

turtle.shape('turtle')

dphi = 5
phi = 0
k = 0.002

N = 300
for i in range(N):
    turtle.left(dphi)
    turtle.forward(k*dphi*(1 + phi**2)**(1/2))
    phi = phi + dphi
