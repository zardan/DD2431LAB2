import numpy, pylab, random, math

# a linear kernel functionn (2D)
# takes two lists/arrays as vectors
# and computes K(x,y)
def lin_ker(x,y):
    product = 0
    for i in range(len(x)-1):
        product = product + x[i]*y[i]
    return product+1
