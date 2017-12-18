register = {}
commands = []
maxVal = 0

with open("input.txt") as file:
    rawLine = file.read().splitlines()
    for raw in rawLine:
        commands.append(raw.split(" "))
        register[raw.split(" ")[0]] = 0

def executeCommand(command):
    operator = command[1]
    value = int(command[2])
    if operator == 'inc':
        register[command[0]] += value
    elif operator == 'dec':
        register[command[0]] -= value


for command in commands:
    checkItem = command[4]
    condition = command[5]
    checkValue = int(command[6])
    if condition == '>':
        if(register[checkItem] > checkValue):
            executeCommand(command)
    elif condition == '<':
        if(register[checkItem] < checkValue):
            executeCommand(command)
    elif condition == '>=':
        if(register[checkItem] >= checkValue):
            executeCommand(command)
    elif condition == '<=':
        if(register[checkItem] <= checkValue):
            executeCommand(command)
    elif condition == '==':
        if(register[checkItem] == checkValue):
            executeCommand(command)
    elif condition == '!=':
        if(register[checkItem] != checkValue):
            executeCommand(command)

    thisMax = max(list(register.values()))
    if maxVal < thisMax:
        maxVal = thisMax

print(max(list(register.values())))
print(maxVal)
