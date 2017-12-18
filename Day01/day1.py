sum = 0

#read file as string
with open("day1Example.input") as file:
    nums = file.read()

#iterate over digit pairs:
for i in range(0, len(nums) -1):
    if int(nums[i]) == int(nums[i+1]):
        sum += int(nums[i])

#last digit == first?
if int(nums[len(nums) -1]) == int(nums[0]):
    sum += int(nums[len(nums) -1])
print(sum)