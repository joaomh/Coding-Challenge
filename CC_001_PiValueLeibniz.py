# Coding Challenge #01
# Pi Approximation with Leibniz Series
# Joao Pinheiro
# YouTube Channel - ExataMenteS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

Interaction = input('Insert the number of interactions: ')
print('The number of interactions is ' + Interaction)


x = np.linspace(0, int(Interaction), int(Interaction)+1)
pi = np.zeros(len(x))
error = np.zeros(len(x))


for i in range(int(Interaction)+1):
    pi[i] =  pi[i-1] + 4*( (-1)**i / (2*i + 1) ) 
    error[i] = pi[i] - np.pi
    plt.plot(x[i],pi[i],'ro', markersize=2)
    plt.plot(x[i],error[i],'bo', markersize=2)
    plt.pause(0.0001)

plt.plot(x,np.pi*np.ones(len(x)))
plt.plot(x,np.zeros(len(x)))
plt.show()
