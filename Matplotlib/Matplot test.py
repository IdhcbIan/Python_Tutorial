
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib as mpl
from numpy import *
import math


figure = Figure()
x = linspace(-100, 100)

y = x**2 + 2 * x + 30

# plt.style.use('fast')
plt.plot(x,y)

#mpl.scatter(numbers, names)    #plosts the x and the y

plt.ylabel('some numbers')
plt.show()

