currentPos = 0
insertVal = 0
loops = 2017
forward = 345
buffer = [0]

for i in range(1,loops+1):
    if(i % 1000 == 0):
        print("{:,}".format(i))
    currentPos = ((currentPos + forward) % len(buffer))
    buffer = buffer[0:currentPos+1] + [i] + buffer[currentPos+1:]
    currentPos += 1
    #print(buffer)

print(buffer[currentPos -5:currentPos+5])

loops = 50000000
currentPos = 0
insertVal = 0
forward = 345
bufferlen = 1
value = 0
for i in range(1,loops+1):
    if(i % 1000000 == 0):
        print("{:,}".format(i))
    currentPos = ((currentPos + forward) % bufferlen)
    if currentPos == 0:
        value = i
    bufferlen += 1
    currentPos += 1
print(buffer)
print(value)