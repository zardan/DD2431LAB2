import numpy, pylab, random, math

# a linear kernel functionn (2D)
def lin_ker(x,y):
    product = x[0]*y[0] + x[1]*y[1]
    return product
