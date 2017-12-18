


def generateValue(lastVal,factor):
    return (lastVal * factor) % 2147483647

def part1():
    generatorAFactor = 16807
    generatorBFactor = 48271
    iteration = 40000000

    #input
    generatorA = 277
    generatorB = 349

    match = 0

    for i in range(iteration):
        if(i % 100000 == 0):
            print("{:,}".format(i))
        generatorA = generateValue(generatorA,generatorAFactor)
        generatorB = generateValue(generatorB,generatorBFactor)
        generatorABin = "{0:b}".format(generatorA)
        generatorBBin = "{0:b}".format(generatorB)
        if(generatorABin[-16:] == generatorBBin[-16:]):
            match += 1
    return(match)

#part2

def generateValue(lastVal,factor,mod):
    accepted = (lastVal * factor) % 2147483647
    while accepted % mod != 0:
        accepted = (accepted * factor) % 2147483647
    return accepted

def part2():
    generatorAFactor = 16807
    generatorBFactor = 48271
    iteration = 5000000

    #input
    generatorA = 277
    generatorB = 349

    match = 0
    for i in range(iteration):
        if(i % 100000 == 0):
            print("{:,}".format(i))
        generatorA = generateValue(generatorA,generatorAFactor,4)
        generatorB = generateValue(generatorB,generatorBFactor,8)
        generatorABin = "{0:b}".format(generatorA)
        generatorBBin = "{0:b}".format(generatorB)
        if(generatorABin[-16:] == generatorBBin[-16:]):
            match += 1
    return(match)


#print(part1())
print(part2())