sum = 0

#read file as string
with open("day1.input") as file:
    nums = file.read()

half = int(len(nums)/2)

#iterate over digit pairs:
for i in range(0, half):
    if int(nums[i]) == int(nums[i + half]):
        sum += int(nums[i])

#last digit == first?
for i in range(half, len(nums)  - 1):
    if int(nums[i]) == int(nums[i - half]):
        sum += int(nums[i])
print(sum)