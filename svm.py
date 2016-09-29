import numpy, math

from cvxopt.solvers import qp
from cvxopt.base import matrix

from data import generateData
from plot import plotFun, contour
from kernels import *

def Pmatrix(data, kernel):
    # Computes matrix P using data and the specified kernel function

    N = len(data)
    P = numpy.zeros(shape=(N,N))
    for i in range(N):
        for j in range(N):
            P[i][j] = data[i][2]*data[j][2]*kernel(data[i],data[j])
    return P

def ind(x,nz_a_d,kernel):
    # indicator function takes new point data point x and classify using 
    # list of previous data points in list nz_a_d

    x.append(0) # makes x a 3-element list as is the classifying data

    res = 0
    for i in range(len(nz_a_d)):
        res += nz_a_d[i][0]*nz_a_d[i][1][2]*kernel(x,nz_a_d[i][1])
        #        alpha_i       t_i             K(x*,x)
    return res



cA,cB,d = generateData()

#kernel = input('Kernel:\n')
kernel = quad_ker 
#kernel = lin_ker

P = Pmatrix(d, kernel)
q = -numpy.ones(len(d))
c = 100
G = -numpy.identity(len(d))
G = numpy.append(G,-G,0)
h = numpy.zeros(len(d))
h = numpy.append(h,c*numpy.ones(len(d)),0)

res = qp(matrix(P), matrix(q), matrix(G), matrix(h))
alpha = list(res['x'])

th = 1e-5
# Set ~0 values to exactly 0 in alpha
alpha = [x if x >= th else 0 for x in alpha]

#make list of non-zero alphas and data points
nz_a_d = [x for x in zip(alpha,d) if x[0] >= th]

print 'alpha = ',alpha
print 'd = ',d
print 'nz_a_d = ',nz_a_d



# plot decision boundary
xRange = numpy.arange(-4,4,0.05)
yRange = xRange
grid = matrix([[ind([x,y],nz_a_d,kernel) for x in xRange] for y in yRange])

contour(xRange,yRange,grid,cA,cB)





