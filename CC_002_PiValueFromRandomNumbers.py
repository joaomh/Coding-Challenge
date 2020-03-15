# Calculating the Value of Pi using Random Numbers (0,1)
# Joao Pinheiro
# Import packages
import random
import numpy as np
import matplotlib.pyplot as plt

# User input
n = input('Insert the number of random points: ')
print('The number of random points is ' + n)

# The function to calculate pi
def calc_pi(n):
    NumPointsCircle = 0 
    NumTotalPoints  = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        Distance = np.sqrt( x**2 + y**2 ) # Euclidian distance
        if Distance <= 1:
            NumPointsCircle += 1
        NumTotalPoints += 1
    # pi / 4 = Number of Points in Circule / Number of Total Points
    pi = 4 * ( NumPointsCircle / NumTotalPoints )    

    return pi    

print( 'The value of pi is: ' + str(calc_pi( int(n) )) )
