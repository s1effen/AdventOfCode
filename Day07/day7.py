nodes = {}
parents = []
unbalancedNodes = {}

#Bottom means, is no ones parent
def getBottom(nodeDict):
    nodesTemp = dict(nodeDict)
    for key in nodeDict:
        for parent in nodeDict[key][1]:
            nodesTemp.pop(parent)
    return nodesTemp.popitem()

def calcSumOfTower(name):
    return calcSumOfTowerRec(name, 0)

def calcSumOfTowerRec(name, level):
    level += 1
    sum = nodes[name][0]
    for parent in nodes[name][1]:
        sum += calcSumOfTowerRec(parent,level)
    nodes[name].append(sum)
    return sum

def getHierachyCalc(parent):
    getHierachyCalcRec(parent,"")

def getHierachyCalcRec(parent,indent):
    indent += indent + "\t"
    valuesAsSet = set()
    for node in nodes[parent][1]:
        valuesAsSet.add(nodes[node][2])
        if(len(valuesAsSet) > 1):
            print(indent + node + ": " + str(nodes[node][0]) + "(" +str(nodes[node][2]) + ") ######" )
        else:
            print(indent + node + ": " + str(nodes[node][0]) + "(" +str(nodes[node][2]) + ")" )

        getHierachyCalcRec(node,indent)

with open("input.txt") as file:
    rawLine = file.read().splitlines()
    for raw in rawLine:
        name  = raw.split(" ",1)[0]
        value = int(raw.split("(")[1].split(")")[0])
        if "->" in raw:
            parents = raw.split(" -> ")[1].split(", ")
        else:
            parents = []
        nodes[name] = [value,parents]

#part1
bottom = getBottom(nodes)
print(bottom)

#part2
calcSumOfTower(bottom[0])

for key in nodes:
    if nodes[key][1]:
        sum = nodes[nodes[key][1][0]][2]
        #print("----------\nNode: " + str(nodes[key]))

        for parent in nodes[key][1]:
            if(sum == nodes[parent][2]):
                True
                #print("Parent: " + parent + ", Sum: " + str(nodes[parent][2]) + ", " + str(nodes[parent]))
            else:
                unbalancedNodes[key] = nodes[key]
                #print(str(nodes[key])  + "\t-> Parent:\t" + str(nodes[parent]))
            sum = nodes[parent][2]

getHierachyCalc(bottom[0])