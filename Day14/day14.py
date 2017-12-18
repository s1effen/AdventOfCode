import pprint
import numpy as np
import binascii

# Stuff of day 10 ######
def getReversedSublist(list,cursor,length):
    reverse = list[cursor:cursor+length]
    if(cursor+length > len(list)):
        reverse += list[0:cursor+length - len(list)]
    reverse.reverse()
    return reverse

def replaceSublist(numbers,cursor,length):
    sublist = getReversedSublist(numbers,cursor,length)
    if cursor+length > len(numbers):    # sublist list sublist
        return sublist[len(numbers)-cursor:] + numbers[(cursor+length) % len(numbers):cursor] + sublist[0:len(numbers)-cursor]
    elif cursor+length < len(numbers):  #list sublist list
        return numbers[0:cursor] + sublist + numbers[cursor+length:]
    else:
        return numbers[0:cursor] + sublist #list sublist

def getHashValue(input):
    input = list((map(lambda x:ord(x), input)))
    input += [17, 31, 73, 47, 23]

    numbers = list(range(0, 256))
    cursor = 0
    skipSize = 0

    for i in range(0,64):
        for length in input:
            numbers = replaceSublist(numbers,cursor,length)
            cursor = (cursor + length + skipSize) % len(numbers)
            skipSize += 1

    result = ""
    for i in range(0,16):
        sum = \
        numbers[i * 16] ^ \
        numbers[i * 16 +1] ^ \
        numbers[i * 16 +2] ^ \
        numbers[i * 16 +3] ^ \
        numbers[i * 16 +4] ^ \
        numbers[i * 16 +5] ^ \
        numbers[i * 16 +6] ^ \
        numbers[i * 16 +7] ^ \
        numbers[i * 16 +8] ^ \
        numbers[i * 16 +9] ^ \
        numbers[i * 16 +10] ^ \
        numbers[i * 16 +11] ^ \
        numbers[i * 16 +12] ^ \
        numbers[i * 16 +13] ^ \
        numbers[i * 16 +14] ^ \
        numbers[i * 16 +15]
        result += hex(sum)[2:].zfill(2)
    return result
########################

def hex2bin(hexString):
    binString = ""
    for digit in hexString:
        binString += bin(int(digit,16))[2:].rjust(4,'0')
    return binString

def bin2usedArray(binString):
    line = []
    for char in binString:
        if char == '0':
            char = '.'
        else:
            char = '#'
        line.append(char)
    return line


#Part1
used = 0
grid = [['' for i in range(128)]for i in range(128)]

def printGrid(grid):
    header0 = ""
    for i in range(2):
        header0 += str(i%100).ljust(100)
    header1 = ""
    for i in range(13):
        header1 += str(i%10).ljust(10)
    header2 = '0123456789' * 13

    print("    " + header0[:128])
    print("    " + header1[:128])
    print("    " + header2[:128])
    i = 0

    for row in grid:
        line = ""
        for char in row:
            line += char
        print(str(i).ljust(4) + line)
        i += 1


for i in range(0,128):
    input = "vbqugkhl-" + str(i)
    hexVal = getHashValue(input)
    binVal = hex2bin(hexVal)
    grid[i] = bin2usedArray(binVal)
    used += grid[i].count('#')

printGrid(grid)
print("Total number #: " + str(used))

#Part2

def pos2key(i,j):
    return(str(i) + "-" + str(j))

def getGroups(grid):
    groupNum = 0
    groups = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == '.'):
                continue
            print("Check " + pos2key(i,j))
            top = False
            left = False
            if(i > 0): #check left neighbor
                if(grid[i-1][j] == '#'):
                    left = True
            if(j > 0): #check top neighbor
                if(grid[i][j-1] == '#'):
                    top = True

            if top and left:
                topID  = groups[pos2key(i,j-1)]
                leftID = groups[pos2key(i-1,j)]
                for entry in groups.keys():
                   if groups[entry] == leftID:
                       groups[entry] = topID
                groups[pos2key(i,j)] = topID
                print("Melted Group at " + pos2key(i,j) + " with IDs " + str(leftID) + " and " + str(topID) + " to " + str(topID))
            elif top: #set as same group
                groups[pos2key(i,j)] = groups[pos2key(i,j-1)]
                print("Existing Group at " + pos2key(i,j) + " with ID " + str(groups[pos2key(i,j)]))
            elif left: #set as same group
                groups[pos2key(i,j)] = groups[pos2key(i-1,j)]
                print("Existing Group at " + pos2key(i,j) + " with ID " + str(groups[pos2key(i,j)]))
            else: #new group
                groupNum += 1
                groups[pos2key(i,j)] = groupNum
                print("New Group at " + pos2key(i,j) + " with ID " + str(groupNum))
    return groups

groups = getGroups(grid)
print(set(groups.values()))
print(len(set(groups.values())))