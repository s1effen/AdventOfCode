lanes = {}
with open("inputEx.txt") as file:
    reader = file.readlines()
    for line in reader:
        lanes[int(line.split(":")[0])] = [int(line.split(":")[1].rstrip("\n")),0,1]

numLanes = max(list(lanes.keys()))

def cycle():
    for key, value in lanes.items():
        if(value[1] == value[0] -1):
            value[2] = -1
        elif(value[1] == 0):
            value[2] = 1
        value[1] += value[2]

def calcPacket(initPos):
    severity = 0
    while initPos <= numLanes:
        if(initPos in lanes.keys() and lanes[initPos][1] == 0): #caught
            severity += initPos * lanes[initPos][0]
            #print("Picosecond " + str(initPos) + " | add severity of " + str(initPos) + " * " + str(lanes[initPos][0]) + " = " + str(initPos * lanes[initPos][0]) + " -> " + str(severity))
        initPos += 1
        cycle()
    return severity

#print(calcPacket(0))

#part 2

def cycle2(state, caller):
    #print("---- " + caller + "----")
    #print("Pre loop " + str(state))
    for key, value in state.items():
        if(value[1] == value[0] -1):
            value[2] = -1
        elif(value[1] == 0):
            value[2] = 1
        value[1] += value[2]
    #print("Post loop " + str(state))
    return state

def calcPacket2(stateInput):
    pos = 0
    while pos <= numLanes:
        #print(stateInput)
        if(pos in stateInput.keys() and stateInput[pos][1] == 0): #caught
            print("Caught in Lane " + str(pos))
            return True
        pos += 1
        stateInput = cycle2(stateInput,"check")
    return False

def resetLanes():
    for value in lanes.values():
        value[1] = 0
        value[2] = 1

resetLanes()
caught = True
startstate = lanes
delay = 0

startstate = cycle2(startstate,"incStart")
startstate = cycle2(startstate,"incStart")
print("############################")
#while caught:

while delay < 12:
    #print("delay " + str(delay))
    #print("new startstate: " + str(startstate))
    print(startstate)
    caught = calcPacket2(startstate)
    print(startstate)
    startstate = cycle2(startstate,"incStart")
    print(startstate)
    print("###########")
    delay += 1