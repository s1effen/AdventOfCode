import pprint
import sys
pipes = {}

def getConnectedPipes(pipe):
    system = set()
    targetsToProof = set()
    targetsToProof.add(pipe)
    while targetsToProof:
        target = targetsToProof.pop()
        for target in pipes[target]:
            if target not in system:
                system.add(target)
                targetsToProof.add(target)
    return system

#0 <-> 1352, 1864
with open("input.txt") as file:
    reader = file.readlines()
    for line in reader:
        line = line.rstrip("\n").split(" <-> ")
        pipe = int(line[0])
        targets = map(lambda x: int(x),line[1].split(", "))
        pipes[pipe] = targets

#part1
print(len(getConnectedPipes(0)))

#part2
systems = set()
for pipe in pipes.keys():
    system = list(getConnectedPipes(pipe))
    system.sort()
    systems.add(str(system))

print(len(systems))