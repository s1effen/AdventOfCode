import csv
from itertools import permutations

invalid = 0
lines = 0
with open("day4.input") as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        lines += 1
        for word in row:
            perms = [''.join(p) for p in permutations(word)]
            rowTemp = list(row)
            rowTemp.remove(word)
            for perm in perms:
                if perm in rowTemp:
                    #print(perm + " exists in row " + str(lines) + " as perm of " + word)
                    invalid +=1
                    break
            else: # Continue if the inner loop wasn't broken.
                continue
            # Inner loop was broken, break the outer.
            break

print(invalid)
print(lines - invalid)