bracketsOpen = 0
numGroups = 0
numGarbage = 0
valueGroups = 0
garbage = False
skip = False
group = ""

with open("input.txt") as file:
    rawLine = file.read().splitlines()
    for character in str(rawLine[0]):
        if skip:
            skip = False
            continue

        if not garbage:
            if character == "{":
                bracketsOpen +=1
            elif character == "}":
                valueGroups += bracketsOpen
                bracketsOpen -=1
                numGroups += 1
            elif character == "<": #begin garbage
                garbage = True
                continue
            group += character

            if character == ",": #newGroup
                group = ""
        else:
            if character == ">": #end garbage
                    garbage = False
            elif character == "!":
                skip = True
            else:
                numGarbage += 1


print("brackets open: " + str(bracketsOpen))
print("value: " + str(valueGroups))
print("num: " + str(numGroups))

print("garbage: " + str(numGarbage))