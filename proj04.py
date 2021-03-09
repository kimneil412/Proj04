#####################################################
# Computer Project #4
# Algorithms
# Asks for different options
# Prompt for inputs
# Using the inputs for calculations
# Display the calculations
# Diplay a closing message
#####################################################

import math

EPSILON = 1.0e-7

# Diplays the prompt for the user to choose from
def display_options():
    ''' This function displays the menu of options'''

    MENU = '''\nPlease choose one of the options below:
             A. Display the sum of squares of the first N natural numbers.
             B. Display the approximate value of Pi.
             C. Display the approximate value of the sine of X.
             D. Display the approximate value of the cosine of X.
             M. Display the menu of options.
             X. Exit from the program.'''

    print(MENU)

# This function adds up the squares of the number inputed by the user
def sum_natural_squares(N):
    '''Insert docstring here.'''
    if N.isdigit() == False:
        return None
    N = int(N)
    if not(N>0):
        return None
    a = 0
    total = 0
    while a <= N:
        total = total + a*a
        a += 1
    return total
    pass

# Approximates pi depending on the user input
def approximate_pi():
    sumpi = 0
    t = 1
    n = 1
    while (abs(t) >= EPSILON):
        sumpi+=t
        t = ((-1)**n)/((2*n+1))
        n+= 1
    return round(4*sumpi,10)

# Approximates sin depending on the user input
def approximate_sin(x):
    try:
        flt_x = float(x)
    except:
        return None
    total = 0
    for i in range(1000):
        t = (((-1)**i)*(flt_x**(2*i+1)))/ (math.factorial(2.0*i + 1))
        if abs(t) < EPSILON:
            break
        total += t
    return round(total, 10)

# Approximates cos depending on the user input
def approximate_cos(x):
    try:
        flt_x = float(x)
    except:
        return None
    total = 0
    for i in range (1000):
        x = (((-1) ** i) * (flt_x ** (2 * i))) / (math.factorial(2.0 * i))
        if abs(x) < EPSILON:
            break
        total += x
    return round(total,10)

# Displays the prompts for the six options
def main():
    display_options()
    z = input("\n\tEnter option: ")
    ans = z.lower()
    while True:
        if not (ans == 'a' or ans == 'b' or ans == 'c' or ans == 'd' or ans == 'm' or ans == 'x'):
            print("\nError:  unrecognized option [{}]".format(z.upper()))
        if ans == 'a': # Display the value of the sum of squares of the first N natural numbers
            n = input("\nEnter N: ")
            if sum_natural_squares(n) == None:
                print("\n\tError: N was not a valid natural number. [{}]".format(n))
                z = input("\n\tEnter option: ")
                ans = z.lower()
                continue
            else:
                print("\n\tThe sum: " + str(sum_natural_squares(n)))
                z = input("\n\tEnter option: ")
                ans = z.lower()
                continue
        if ans == 'b': # Display the approximate value of Pi
            print("\n\tApproximation: {:.10f}".format(approximate_pi()))
            print("\tMath module:   {:.10f}".format(math.pi))
            print("\tdifference:    {:.10f}".format(abs(math.pi - approximate_pi())))
            z = input("\n\tEnter option: ")
            ans = z.lower()
            continue
            pass
        if ans == 'c': # Display the approximate value of the sine of X
            x = input("\n\tEnter X: ")
            if approximate_sin(x) == None:
                print("\n\tError: X was not a valid float. [{}]".format(x))
                z = input("\n\tEnter option: ")
                ans = z.lower()
                continue
            x = float(x)
            print("\n\tApproximation: {:.10f}".format(approximate_sin(x)))
            print("\tMath module:   {:.10f}".format(math.sin(x)))
            dif = abs(math.sin(x) - approximate_sin(x))
            print("\tdifference:    {:.10f}".format(dif))
            z = input("\n\tEnter option: ")
            ans = z.lower()
            continue
            pass
        if ans == 'd': # Display the approximate value of the cosine of X
            x = input("\n\tEnter X: ")
            if approximate_sin(x) == None:
                print("\n\tError: X was not a valid float. [{}]".format(x))
                z = input("\n\tEnter option: ")
                ans = z.lower()
                continue
            x = float(x)
            print("\n\tApproximation: {:.10f}".format(approximate_cos(x)))
            print("\tMath module:   {:.10f}".format(math.cos(x)))
            dif = abs(math.cos(x) - approximate_cos(x))
            print("\tdifference:    {:.10f}".format(dif))
            z = input("\n\tEnter option: ")
            ans = z.lower()
            continue
            pass
        if ans == 'm': # Display the menu of options
            pass
        if ans == 'x': # Exit the program
            print('Hope to see you again.')
            break
        display_options()
        z = input("\n\tEnter option: ")
        ans = z.lower()

if __name__ == "__main__":
    main()

