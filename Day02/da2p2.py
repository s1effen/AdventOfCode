import csv
sum = 0
with open("day2.input") as csvfile:
    reader = csv.reader(csvfile, delimiter='\t',quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        for i in range(0,len(row)):
            for j in range(0,len(row)):
                if i != j and (row[i] / row[j]) % 1 == 0:
                    #print(str(row[i])  + " - " + str(row[j]) + " -- " + str(row[i] / row[j]))
                    sum += row[i] / row[j]

print(sum)