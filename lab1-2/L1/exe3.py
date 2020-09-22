import numpy as m
import matplotlib.pyplot as plt

x = m.arange(-10, 10.01, 0.01)
y = m.log((x**2 + 1)*m.exp(-m.abs(x) / 10)) / m.log(1 + m.tan(1 / (1 + m.sin(x)**2)))

plt.plot(x, y)
plt.grid(True)
plt.show()
