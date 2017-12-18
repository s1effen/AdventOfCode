import csv
sum = 0
with open("day2.input") as csvfile:
    reader = csv.reader(csvfile, delimiter='\t',quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        sum += max(row) - min(row)
print(sum)