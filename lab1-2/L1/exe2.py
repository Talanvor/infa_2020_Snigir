import numpy as m
import matplotlib.pyplot as plt

x = m.arange(-10, 10.01, 0.01)
y = x*x - x - 6

plt.plot(x, y)
plt.grid(True)
plt.show()

print("Первый корень -2, второй 3")
