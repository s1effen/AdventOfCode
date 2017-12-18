import csv
data = []
with open("input.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter='\t',quoting=csv.QUOTE_NONNUMERIC)
    data = list(map((int),next(reader)))

def cycle(data):
    cycles = 0
    history = []
    while str(data) not in history:
        cycles += 1
        history.append(str(data))
        cursor = data.index(max(data))
        buffer = data[cursor]
        data[cursor] = 0
        for i in range(1,buffer+1,1):
            data[(cursor + i) % len(data)] += 1
    else:
        return (cycles,data)

cycles1,state1 = cycle(data)
print(state1)
print(cycles1)

cycles2,state2 = cycle(state1)
print(state2)
print(cycles2)
