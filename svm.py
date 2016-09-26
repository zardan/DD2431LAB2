import numpy, random, math

from cvxopt.solvers import qp
from cvxopt.base import matrix

from data import generateData
from plot import plotFun

cA,cB,d = generateData()

plotFun(cA,cB)


