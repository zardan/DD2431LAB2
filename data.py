
# generate data of two classes

def generateData():
    classA = [(random.normalvariate(-1.5, 1),
        random.normalvariate(0.5,1),
        1)
        for i in range(5)] + \
                [(random.normalvariate(1.5, 1),
                random.normalvariate(0.5, 1),
                1.0)
                for i in range(5)]

    classB = [(random.normalvariate(0.0, 0.5),
        random.normalvariate(-0.5, 0.5),
        -1.0)
        for i in range(10)]

    data = classA + classB
    random.shuffle(data)

    return classA, classB, data
