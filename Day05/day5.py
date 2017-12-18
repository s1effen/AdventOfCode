with open("input.txt") as file:
    instructions = file.readlines()

instructions = list(map(int, instructions))
pointer = 0
steps = 0
while(pointer >= 0 and pointer < len(instructions)):
    steps +=1
    pointerToIncrement = pointer
    pointer = pointer + instructions[pointer]
    instructions[pointerToIncrement] += 1

print(steps)

