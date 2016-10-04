import math

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

def rad_ker(x,y):
    xmy2 = 0
    for i in range(len(x)-1):
        xmy2 += (x[i]-y[i])**2
    sigma = 1
    return math.exp(-xmy2/(2*sigma**2))

def sig_ker(x,y):
    k = 0.15
    d = -0.1
    xdy = 0
    for i in range(len(x)-1):
        xdy += x[i]*y[i]
    arg = k*xdy-d
    #print math.tanh(arg)
    return math.tanh(arg)
