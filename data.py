import numpy, random, math
# generate data of two classes

def generateData():
    classA = [(random.normalvariate(1, 0.8),
        random.normalvariate(1.5, 0.1),
        1)
        for i in range(5)] + \
                [(random.normalvariate(-1, 0.8),
                random.normalvariate(1, 0.1),
                1.0)
                for i in range(5)]
                
    classB = [(random.normalvariate(0.5, 0.8),
        random.normalvariate(0, 0.1),
        1)
        for i in range(5)] + \
                [(random.normalvariate(-1.5, 0.8),
                random.normalvariate(-1, 0.1),
                1.0)
                for i in range(5)]


#    classB = [(random.normalvariate(-0.5, 2),
#        random.normalvariate(-1, 0.2),
#        -1.0)
#        for i in range(10)]

    data = classA + classB
    random.shuffle(data)

    return classA, classB, data
