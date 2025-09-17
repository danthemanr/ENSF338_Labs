import sys
import math

def do_stuff():

    #Requires 3 args from the command line
    #I added a check to make sure that all of the arguments are there
    if len(sys.argv) != 4:
        print(f'Requires 3 extra comand line arguments.\nNumber of extra args: {len(sys.argv) - 1}')
        exit(0)
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    d = b**2 - 4*a*c #d is the determinant of the quadratic ax^2 + bx + c
    #if a=0 was not originally part of this file
    if a == 0: #this avoids division by zero
        if b == 0:
            print("A constant function has no roots.")
        else:
            root = -c / b
            print(f'This function is linear, not quadratic.\nThe solution is: {root}')
    #the remaining if block computes the roots using the quadratic formula
    elif d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f'The solutions are: {root1}, {root2}')
    elif d == 0:
        root = -b / (2*a)
        print(f'The solution is: {root}')
    else:
        print('There are no real solutions.')
      
do_stuff()