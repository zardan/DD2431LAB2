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


