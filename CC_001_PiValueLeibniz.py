# Coding Challenge #001
# Pi Approximation with Leibniz Series
# Joao Pinheiro
# YouTube Channel - ExataMenteS

# Import some packages
import numpy as np 
import matplotlib.pyplot as plt 

# User input ot 'n'
Interaction = input('Insert the number of interactions: ')
print('The number of interactions is ' + Interaction)

# Init the variables
n = np.linspace(0, int(Interaction), int(Interaction)+1)
pi = np.zeros(len(n))
error = np.zeros(len(n))

# Loop
for i in range(int(Interaction)+1):
    pi[i] = pi[i-1] + 4*( (-1)**i / (2*i+1) )   # Leibniz Formula Aprox
    error[i] = pi[i] - np.pi                    # Comparing with the real value of Pi
    plt.plot(n[i],pi[i],'ro',markersize=2)      # Plot the pi[i] for each 'n'
    plt.plot(n[i],error[i],'bo',markersize=2)   # Plot the error[i] for each 'n'
    plt.pause(0.001)

# Plot and see if the series converg
plt.plot(n,np.pi*np.ones(len(n)))               # Plot a constant line with value of Pi
plt.plot(n,np.zeros(len(n)))                    # Plot a constant line with value of 0
plt.show()
