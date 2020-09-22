import numpy as m
import matplotlib.pyplot as plt

a = 2.3
b = 0.5
Saccuracy = 250
Gaccuracy = 0.0001

x = m.arange(-2, (2+Gaccuracy), Gaccuracy)
y = m.zeros(round(4/Gaccuracy + 1))

n = 0
while n <= Saccuracy:
    y = y + (b**n)*m.cos((a**n)*m.pi*x)
    n = n + 1

plt.plot(x, y)
plt.grid(True)
plt.show()
