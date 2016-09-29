import numpy, math

from cvxopt.solvers import qp
from cvxopt.base import matrix

from data import generateData
from plot import plotFun
from kernels import *

cA,cB,d = generateData()

#linK = lin_ker(cA...nat...)
print cA

plotFun(cA,cB)

def Pmatrix(data, kernel):
    N = len(data)
    P = numpy.zeros(shape=(N,N))
    for i in range(N):
        for j in range(N):
            P[i][j] = data[i][2]*data[j][2]*kernel(data[i],data[j])
    return P

P = Pmatrix(d,lin_ker)
print P
