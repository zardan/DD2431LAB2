import pylab

def plotFun(cA,cB):
    pylab.hold(True)
    pylab.plot([p[0] for p in cA],
            [p[1] for p in cA],
            'bo')
    pylab.plot([p[0] for p in cB],
            [p[1] for p in cB],
            'ro')
    pylab.show()

def contour(xR,yR,grid,cA,cB):
    pylab.hold(True)
    pylab.plot([p[0] for p in cA],
            [p[1] for p in cA],
            'bo')
    pylab.plot([p[0] for p in cB],
            [p[1] for p in cB],
            'ro')

    pylab.contour(xR,yR,grid,
            (-1.0,0.0,1.0),
            colors = ('red','black','blue'),
            linewidths = (1, 3, 1))

    pylab.show()
