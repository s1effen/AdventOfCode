import re

grid = []
symbol = '#'

with open("input.txt") as file:
    reader = file.readlines()
    for line in reader:
        row = []
        for col in line.rstrip("\n"):
            row.append(col)
        grid.append(row)

def printGrid(pointer):
    for i in range(len(grid)):
        row = ""
        for j in range(len(grid[i])):
            if(i == pointer[0] and j == pointer[1]):
                row += symbol
            else:
                row += grid[i][j]
        print(row)

def getBounds(pointer,size,axis):
    if axis == 0:
        if(pointer[0] + size) > len(grid[0])-1:
            return (len(grid[0])-1-(size*2),len(grid[0])-1)
        elif(pointer[0] - size) < 0:
            return (0,(size*2))
        else:
            return(pointer[0] - size,pointer[0] + size)
    else:
        if(pointer[1] + size) > len(grid)-1:
            return (len(grid)-1-size,len(grid)-1)
        elif(pointer[1] - size) < 0:
            return (0,size*2)
        else:
            return(pointer[1] - size,pointer[1] + size)

def printdetailGrid(pointer,sizeHoriz,sizeVert):
    horBounds  = getBounds(pointer,sizeHoriz,0)
    vertBounds = getBounds(pointer,sizeVert,1)
    for i in range(horBounds[0],horBounds[1]):
        row = ""
        for j in range(vertBounds[0],vertBounds[1]):
            if(i == pointer[0] and j == pointer[1]):
                row += symbol
            else:
                row += grid[i][j]
        print(row)

def getStartCoord():
    return (0,grid[0].index('|'))

def getSymbol(coord):
    return grid[coord[0]][coord[1]]

cursor = getStartCoord()
direction = (1,0) #down

def getNewDirection(coord,direction):
    directionA = (direction[1],direction[0])
    checkA = (coord[0] + directionA[0], coord[1] + directionA[1])
    directionB = (direction[1]*-1,direction[0]*-1)
    checkB = (coord[0] + directionB[0], coord[1] + directionB[1])

    if getSymbol(checkA) != " ":
        return directionA
    elif getSymbol(checkB) != " ":
        return directionB
    else:
        return (0,0)

def moveCursor(cursor,direction):
    cursor = (cursor[0] + direction[0],cursor[1] + direction[1])
    symb = getSymbol(cursor)
    if symb == '+': #turn
        direction = getNewDirection(cursor,direction)
    return cursor, direction



#print(cursor)
#print(direction)
#printGrid(cursor)

#printdetailGrid(cursor,10,10)
stepsToPrint = 0
letters = ""
stepCount = 1
lastStepWithLetter = 0

while direction != (0,0):
    stepCount += 1
    cursor,direction = moveCursor(cursor,direction)
    if(cursor[0] == 0 or cursor[1] == 0):
        print(letters)
        print(lastStepWithLetter)
        break
    if(getSymbol(cursor) == '+'):
        print("********************************** " + str(cursor) + ", " + str(stepCount) + " steps.")
        printdetailGrid(cursor,5,10)
        stepsToPrint = 3
    else:
        if re.match(r"[A-Z]", getSymbol(cursor)): #Letter
            print("********************************** " + str(cursor) + ", " + str(stepCount) + " steps.")
            printdetailGrid(cursor,5,10)
            letters += getSymbol(cursor)
            lastStepWithLetter = stepCount
        if stepsToPrint > 0:
            print("********************************** " + str(cursor) + ", " + str(stepCount) + " steps.")
            printdetailGrid(cursor,5,10)
            stepsToPrint -= 1