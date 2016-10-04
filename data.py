import numpy, random, math
# generate data of two classes

def generateData():
    classA = [(random.normalvariate(2, 1),
        random.normalvariate(2, 0.3),
        1)
        for i in range(5)] + \
                [(random.normalvariate(1, 1),
                random.normalvariate(0, 0.3),
                1.0)
                for i in range(5)]

    classB = [(random.normalvariate(2, 1),
        random.normalvariate(1, 0.1),
        -1.0)
        for i in range(10)]

    data = classA + classB
    random.shuffle(data)

    return classA, classB, data
