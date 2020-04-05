# Coding Challenge #003
# Number of Steps to Reduce a Number to Zero
# Joao Pinheiro
# YouTube Channel - ExataMenteS

def NumberOfSteps(n):
    Steps = 0              # Init the steps as 0
    while(n != 0):         # Verify if the number is zero
        if(n % 2 == 0):    # Verify if is even
            n /= 2         # Div by 2
        else:              # If is odd
            n -= 1         # Sub 1
        Steps += 1
    return Steps


# User input ot 'Number'
Number = input('Insert a non-negative integer: ')
print('The number is ' + str(Number))
print('The number os steps is: ' + str(NumberOfSteps(int(Number))))
