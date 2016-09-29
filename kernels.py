import numpy, math

# a linear kernel functionn (2D)
# takes two lists/arrays as vectors
# and computes K(x,y)

def lin_ker(x,y):
    product = 0
    for i in range(len(x)-1):
        product = product + x[i]*y[i]
    return product+1

def quad_ker(x,y):
    res = lin_ker(x,y)
    return res*lin_ker(x,y)

def cube_ker(x,y):
    res = quad_ker(x,y)
    return res*lin_ker(x,y)
