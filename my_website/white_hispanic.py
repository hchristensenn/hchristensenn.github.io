import matplotlib.pyplot as plt
import os.path
import numpy as np

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'white_hispanic.csv')
datafile = open(filename, 'r')
data = datafile.readlines()

def sumzip(*items):
    return [sum(values) for values in zip(*items)]

population=[]
whites=[]
hispanics=[]
states=[]
other=[]
total=[]

for line in data:
    state, total, white, hispanic = line.split(",")
    population.append(int(total))
    whites.append(int(white))
    hispanics.append(int(hispanic))
    states.append(state)
    other.append(int(total)-int(white)-int(hispanic))

    
width = 0.35

p1 = plt.bar(range(len(states)), hispanics, width, color='black')
p2 = plt.bar(range(len(states)), whites, width, bottom=hispanics, color='blue')
p3 = plt.bar(range(len(states)), other, width, color='purple', bottom=sumzip(whites,hispanics))

plt.ylabel('population')
plt.title('population of hispanic vs white')
plt.xticks(range(len(states)), ('Washington', 'Oregon', 'California'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0], p3[0]), ('hispanic', 'white', 'other'))

plt.show()
    