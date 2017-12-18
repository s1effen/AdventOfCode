import time

commands = []
programs = []
numProgs = 16

with open("input.txt") as file:
    reader = file.readlines()
    for line in reader:
        commands = line.split(",")

for i in range(numProgs):
    programs.append(chr(i + ord('a')))

def swap(programs,posA,posB):
    #print("swap " + programs[posA] + "(" + str(posA) + ") and " + programs[posB] + "(" + str(posB) + ")")
    ret = list(programs)
    temp = ret[posA]
    ret[posA] = ret[posB]
    ret[posB] = temp
    return ret

def perform(programs,commands,loops,disableS,disableX,disableP):
    history = [programs]
    for i in range(loops):
        if(i % 1000 == 0):
            print("{:,}".format(i))
        for command in commands:
            #print(programs)
            if(command[0] == 's'): #spin
                if disableS: continue
                length = int(command[1:])
                #print("Spin last " + str(length) + " programs: " + str(programs[-length:]))
                splitpos = numProgs - length
                programs = programs[splitpos:16] + programs[0:splitpos] #TEUER
            elif(command[0] == 'x'): #exchange
                if disableX: continue
                pos = command[1:].split('/')
                programs = swap(programs,int(pos[0]),int(pos[1]))
            elif(command[0] == 'p'): #partner
                if disableP: continue
                progs = command[1:].split('/')
                programs = swap(programs,programs.index(progs[0]),programs.index(progs[1]))
                #print(programs)
                #print("---------------------------------------------------------------------------------")
        #if programs in history:
        #    print("Cycle in loop " + str(i) + " same as " + str(history.index(programs)) + ": " + printProgramRet(programs))
        #else:
        #    history.append(programs)
    return programs

def printProgram(programs):
    result = ""
    for c in programs:
        result += c
    print(result)

#part1
programsPart1 = perform(programs,commands,1,False,False,False)
printProgram(programsPart1)

#part2
print("\n----- Part2")

print("proof that shortcut exists:")
printProgram(programs)
programsA = perform(programs,commands,1,False,False,True)
printProgram(programsA)
programsB = perform(programsA,commands,1,True,True,False)
printProgram(programsB)

print("\n-- get shortcuts:")
print("\n\nop s and x: ")
#get shortcut for operation s and x:
printProgram(programs)
programsC = perform(programs,commands,1,False,False,True)
printProgram(programsC)
code = "programs=["
for c in programsC:
    code += "programs[" + str(programs.index(c)) + "],"
print(code[:-1] + "]")
programsD = [programs[5],programs[13],programs[0],programs[12],programs[7],programs[4],programs[2],programs[15],programs[8],programs[10],programs[3],programs[1],programs[6],programs[11],programs[9],programs[14]]
printProgram(programsD)

print("\n\nop p: ")
#get shortcut for operation p:
printProgram(programs)
programsE = perform(programs,commands,1,True,True,False)
printProgram(programsE)

code = "swapFast(programs,["
for i in range(numProgs):
    charA = programs[i]
    charB = programsE[i]
    code += "['" + charA + "','" + charB + "'],"
code = code[:-1] + "])"
print(code)

def swapFast(programs,swaplist):
    ret = [None] * numProgs
    for pair in swaplist:
        pos = programs.index(pair[0])
        ret[pos] = pair[1]
    return ret

programsF = swapFast(programs,[['a','i'],['b','d'],['c','o'],['d','k'],['e','f'],['f','c'],['g','n'],['h','b'],['i','m'],['j','p'],['k','g'],['l','l'],['m','j'],['n','e'],['o','h'],['p','a']])
printProgram(programsF)

print("---------------------------------")
print("last proof: ")

def printProgramRet(programs):
    result = ""
    for c in programs:
        result += c
    return  result

def performFast(programs,loops):
    history = [programs]
    for i in range(1,loops+1):
        if(i % 100000 == 0):
            print("{:,}".format(i))
        programs = [programs[5],programs[13],programs[0],programs[12],programs[7],programs[4],programs[2],programs[15],programs[8],programs[10],programs[3],programs[1],programs[6],programs[11],programs[9],programs[14]]
        programs = swapFast(programs,[['a','i'],['b','d'],['c','o'],['d','k'],['e','f'],['f','c'],['g','n'],['h','b'],['i','m'],['j','p'],['k','g'],['l','l'],['m','j'],['n','e'],['o','h'],['p','a']])
        #if programs in history:
        #    print("Cycle in loop " + str(i) + " same as " + str(history.index(programs)) + ": " + printProgramRet(programs))
        #else:
        #    history.append(programs)
    return programs

programsG = perform(programs,commands,10,False,False,False)
printProgram(programsG)
programsH = performFast(programs,10)
printProgram(programsH)
print("---------------------------------")
print("execution: ")

a = time.time()
programspart2 = perform(programs,commands,1000,False,False,False)
b = time.time()
programsPart2Fast = performFast(programs,1000)
c = time.time()

print(str(b - a) + " -> " + str(c - b))
print(str((b - a)*1000000) + " -> " + str((c - b)*1000000))