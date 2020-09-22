import numpy as m
import matplotlib.pyplot as plt

x = [0.30, 0.60, 0.90, 1.20, 1.50, 1.80, 2.10, 2.40, 2.70, 3.00]
y = [   5,   14,   22,   28,   29,   27,   19,    6,   -9,  -25]

t = m.arange(0.3, 3.1, 0.1)

p, v = m.polyfit(x, y, deg = 2, cov = True)
p_f = m.poly1d(p)

plt.plot(t, p_f(t))
plt.errorbar(x, y, xerr = 0.02, yerr = 2, fmt = 'r+')
plt.grid(True)
plt.show()
