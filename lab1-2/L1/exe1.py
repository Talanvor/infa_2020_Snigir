import numpy as m

x = m.array([1, 10, 1000])
y = m.log((m.exp(1/(m.sin(x) + 1))) / (5/4 + 1/(5*x))) / m.log(1 + x**2)
print(y)

