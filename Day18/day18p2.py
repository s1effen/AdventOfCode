commands = []
with open("input.txt") as file:
    reader = file.readlines()
    for line in reader:
        commands.append(line.rstrip("\n").split(" "))

registers0 = {}
registers1 = {}
lastSound = 0

for command in commands:
    if not command[1].isdigit():
        registers0[command[1]] = 0
        registers1[command[1]] = 0
        if(command[1] == 'p'):
            registers1[command[1]] = 1

print("Init 0: " + str(registers0))
print("Init 1: " + str(registers1))

def getVal(input,registers):
    try:
        value = int(input)
    except ValueError:
        value = registers[input]
    return value

queue0 = []
queue1 = []

def execution(command,programID):
    if(programID == 0):
        sndQueue = queue1
        rcvQueue = queue0
        registers = registers0
    else:
        sndQueue = queue0
        rcvQueue = queue1
        registers = registers1

    if command[0] == "snd": #snd X sends the value of X to the other program. These values wait in a queue until that program is ready to receive them. Each program has its own message queue, so a program can never receive a message it sent.
            sndQueue.append(getVal(command[1],registers))
    elif command[0] == "set": #set X Y sets register X to the value of Y.
        registers[command[1]] = getVal(command[2],registers)
    elif command[0] == "add": #add X Y increases register X by the value of Y.
        registers[command[1]] += getVal(command[2],registers)
    elif command[0] == "mul": #mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
        registers[command[1]] = getVal(command[1],registers) * getVal(command[2],registers)
    elif command[0] == "mod": #mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
        registers[command[1]] = getVal(command[1],registers) % getVal(command[2],registers)
    elif command[0] == "rcv": #rcv X receives the next value and stores it in register X. If no values are in the queue, the program waits for a value to be sent to it. Programs do not continue to the next instruction until they have received a value. Values are received in the order they are sent.
        if len(rcvQueue) > 0:
            registers[command[1]] = rcvQueue.pop(0)
        else:
            return 0 #wait in this command
    elif command[0] == "jgz" and getVal(command[1],registers) > 0: #jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero.
        # (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
        if(getVal(command[2],registers) > 0):
            return getVal(command[2],registers)
        else:
            return getVal(command[2],registers)
    return 1

cycle0 = 0
cycle1 = 0
snd1 = 0

while True:
    command0 = commands[cycle0]
    jump0 = execution(command0,0)
    cycle0Old = cycle0
    cycle0 += jump0

    command1 = commands[cycle1]
    jump1 = execution(command1,1)
    cycle1Old = cycle1
    cycle1 += jump1

    if command1[0] == "snd":
        snd1 += 1

    if jump0 == 0 and jump1 == 0: #deadlock
        print("##### Deadlock!")
        print("Program 1 send " + str(snd1) + " times")
        break
    if False:
        print("------- Execution cycle ")
        print("\t------- Program 0 ")
        print("\t\t Cycle " + str(cycle0Old))
        print("\t\t" + str(command0))
        print("\t\t" + str(registers0))
        print("\t\t next command is (" + str(cycle0) + "): " + str(commands[cycle0]))
        print("\t\t Queue is " + str(queue0))
        print("\t------- Program 1 ")
        print("\t\t Cycle " + str(cycle1Old))
        print("\t\t" + str(command1))
        print("\t\t" + str(registers1))
        print("\t\t next command is (" + str(cycle1) + "): " + str(commands[cycle1]))
        print("\t\t Queue is " + str(queue1))
        print("----------------------- ")
        #input("Press Enter to continue...")