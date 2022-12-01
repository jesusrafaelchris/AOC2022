## Part 1
summation = []

with open('/Users/christiangrinling/Desktop/AdventOfCode.txt') as f:
    tempSum = 0
    for line in f:
        if line != "\n":
            tempSum += int(line)
        else:
            summation.append(tempSum)
            tempSum = 0

print("Max sum is " + str(max(summation)))

## Part 2
total_sum = 0
copy_of_summation = summation
sorted_copy = sorted(copy_of_summation, reverse = True)

for i in range(0,3):
    total_sum += sorted_copy[i]

print("Total sum of top 3 is " + str(total_sum))