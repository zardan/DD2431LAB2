import pylab

def plotFun(classA,classB):
    pylab.hold(True)
    pylab.plot([p[0] for p in classA],
            [p[1] for p in classA],
            'bo')
    pylab.plot([p[0] for p in classB],
            [p[1] for p in classB],
            'ro')
    pylab.show()
