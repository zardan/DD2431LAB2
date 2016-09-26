import numpy, pylab, random, math

# a linear kernel functionn (2D)
def lin_ker(x,y):
    product = 0
    for i in range(len(x)-1):
        product = product + x[i]*y[i]
    return product+1
