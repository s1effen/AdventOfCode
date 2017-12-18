commands = []
with open("input.txt") as file:
    reader = file.readlines()
    for line in reader:
        commands.append(line.rstrip("\n").split(" "))

print(commands)
registers = {}
lastSound = 0

for command in commands:
    if not command[1].isdigit():
        registers[command[1]] = 0

print(registers)

def getVal(input):
    try:
        value = int(input)
    except ValueError:
        value = registers[input]
    return value

i = 0
while i  < len(commands):
    command = commands[i]
    print("------- command " + str(i))
    print(command)
    if command[0] == "snd": #snd X plays a sound with a frequency equal to the value of X.
        print("set last sound to " + str(getVal(command[1])))
        lastSound = getVal(command[1])
    elif command[0] == "set": #set X Y sets register X to the value of Y.
        registers[command[1]] = getVal(command[2])
    elif command[0] == "add": #add X Y increases register X by the value of Y.
        registers[command[1]] += getVal(command[2])
    elif command[0] == "mul": #mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
        registers[command[1]] = getVal(command[1]) * getVal(command[2])
    elif command[0] == "mod": #mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
        registers[command[1]] = getVal(command[1]) % getVal(command[2])
        print("\t---> " + str(registers[command[1]]))
    elif command[0] == "rcv" and getVal(command[1]) != 0: #rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
        registers[command[1]] = lastSound
        print("recover op: " + str(lastSound))
        break
    elif command[0] == "jgz" and getVal(command[1]) > 0: #jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
        if(getVal(command[2]) > 0):
            i = i + getVal(command[2])
        else:
            i = i + getVal(command[2]) -1
        print("jump to command " + str(i+1) + ": " + str(commands[i+1]))
    print(registers)
    i += 1