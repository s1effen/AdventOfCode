import csv
valid = 0

with open("day4.input") as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        if len(set(row)) == len(row): #no duplicates
            valid +=1
print(valid)