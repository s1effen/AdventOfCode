def getReversedSublist(list):
     reverse = list[cursor:cursor+length]
     if(cursor+length > len(list)):
         reverse += list[0:cursor+length - len(list)]
     reverse.reverse()
     return reverse

def replaceSublist():
    sublist = getReversedSublist(numbers)
    if cursor+length > len(numbers):    # sublist list sublist
        return sublist[len(numbers)-cursor:] + numbers[(cursor+length) % len(numbers):cursor] + sublist[0:len(numbers)-cursor]
    elif cursor+length < len(numbers):  #list sublist list
        return numbers[0:cursor] + sublist + numbers[cursor+length:]
    else:
        return numbers[0:cursor] + sublist #list sublist

with open("input.txt") as file:
    data = list(map(int, file.readline().rstrip("\r\n").split(",")))


numbers = list(range(0, 256))
cursor = 0
skipSize = 0

for length in data:
    numbers = replaceSublist()
    cursor = (cursor + length + skipSize) % len(numbers)
    skipSize += 1

print(numbers[0] * numbers[1])

#part 2
with open("input.txt") as file:
    data = list((map(lambda x:ord(x), file.readline().rstrip("\r\n"))))
data += [17, 31, 73, 47, 23]
print(data)

numbers = list(range(0, 256))
cursor = 0
skipSize = 0

for i in range(0,64):
    for length in data:
        numbers = replaceSublist()
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

print(result)