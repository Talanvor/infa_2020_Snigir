import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
t = 1.0

objects = []
with open('stats.txt', 'r') as stats:
	for line in stats:
		if len(line.strip()) == 0 or line[0] == '#':
			continue  # пустые строки и строки-комментарии пропускаем
		object_type = line.split()[0].lower()
		if object_type == "planet":  #fixed
			y.append( (float(line.split()[6])**2 + float(line.split()[7])**2)**0.5 )
			x.append( t )
			t += 1.0

plt.plot(x, y)
plt.grid(True)
plt.show()