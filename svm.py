import numpy, math

from cvxopt.solvers import qp
from cvxopt.base import matrix

from data import generateData
from plot import plotFun
from kernels import *

def Pmatrix(data, kernel):
    N = len(data)
    P = numpy.zeros(shape=(N,N))
    for i in range(N):
        for j in range(N):
            P[i][j] = data[i][2]*data[j][2]*kernel(data[i],data[j])
    return P

cA,cB,d = generateData()

#kernel = input('Kernel:\n')
#P = Pmatrix(d, kernel)

P = Pmatrix(d, lin_ker)
q = -numpy.ones(len(d))
c = 1
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
nz_a_l = [x for x in zip(alpha,d) if x[0] >= th]

#array_np = numpy.asarray(alpha)
#zeroind = array_np < 1e-5
#array_np[zeroind] = 0
#a = array_np
#print 'a = ', a
