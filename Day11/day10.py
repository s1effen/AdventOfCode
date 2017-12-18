from operator import ne

n_s = 0
ne_sw = 0
nw_se = 0
sums = []
avg = []

steps = {'n':0,'s':0,'ne':0,'se':0,'nw':0,'sw':0}

def printSituation():
    print("-----")
    if(steps['n'] > steps['s']):
        print("N: " + str(steps['n'] - steps['s']))
    else:
        print("S: " + str(steps['s'] - steps['n']))
    if(steps['ne'] > steps['sw']):
        print("NE: " + str(steps['ne'] - steps['sw']))
    else:
        print("SW: " + str(steps['sw'] - steps['ne']))
    if(steps['nw'] > steps['se']):
        print("NW: " + str(steps['nw'] - steps['se']))
    else:
        print("SE: " + str(steps['se'] - steps['nw']))
    print("-----")

with open("input.txt") as file:
    data = list(file.readline().rstrip("\r\n").split(","))

for direction in data:
    steps[direction] += 1
    if direction == 'n':
        n_s += 1
    elif direction == 's':
        n_s -= 1

    if direction == 'ne':
        ne_sw += 1
    elif direction == 'sw':
        ne_sw -= 1

    if direction == 'nw':
        nw_se += 1
    elif direction == 'se':
        nw_se -= 1

    sums.append(n_s + ne_sw + nw_se)
    avg.append()
    if((n_s + ne_sw + nw_se) == 644 or (n_s + ne_sw + nw_se) == -644):
        printSituation()

print("-----")
print(steps)



axisNS = steps['n'] - steps['s']
axisNESW = steps['ne'] - steps['sw']
axisNWSE = steps['ne'] - steps['sw']

print(sums)
print(max(sums))

