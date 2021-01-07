import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
t = 1.0

px = 0.0
py = 0.0
sx = 0.0
sy = 0.0

objects = []
with open('stats.txt', 'r') as stats:
	for line in stats:
		if len(line.strip()) == 0 or line[0] == '#':
			t += 1.0
			x.append( t )
			r = ((px - sx)**2 + (py - sy)**2)**0.5
			y.append( r )
			continue
		object_type = line.split()[0].lower()
		if object_type == "planet":  #fixed
			px = float(line.split()[4])
			py = float(line.split()[5])
		if object_type == "star":  #fixed
			sx = float(line.split()[4])
			sy = float(line.split()[5])

plt.plot(x, y)
plt.grid(True)
plt.show()