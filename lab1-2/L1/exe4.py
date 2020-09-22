import numpy as m
import matplotlib.pyplot as plt

x = m.arange(-10, 10.01, 0.01)
y = eval(input())

with plt.xkcd():
    plt.plot(x, y)
    plt.show()

