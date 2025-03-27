# A pseudo-real-world application.
# Refer to the associared data/6_resource_utilization.txt and answer the following items:
#   1. What is the average system temperature?
#   2. Which CPU has the highest average utilization
#   3. At what time was the GPU the most used?

# Part 0 - open the file
PATH = "C:/Users/Jacob/code/python_lessons_for_brennan/data/6_resource_utilization.txt"
file = open(PATH, "r")

# Part 1
# New techniques:
#   if string contains substring - simply if substring in string
#   Remove whitespace from string
#       Use string.strip
#   Partition string
#       Use a substring split a sting into pieces.
#   Trim last character of string - string = string[:-1]
#       A string is an array of characters, so each character can be accessed in the same way as an array
#       An array can be accessed by tange using the : operator
#       A blank index indicates a default value
#       A negative index counts from the back of the array, starting at 1

TARGET = "Temperature:"
sum = 0
count = 0

for line in file:
    if not TARGET in line: continue
    process_line = line.strip()
    pre, sub, after = process_line.partition(TARGET)
    after = after[:-1]

    sum += int(after)
    count += 1

file.close()
print("Average temp:", sum / count)


# Part 2
# Highest can be defined in multiple ways.
# We just wrote an averaging piece of code, so we can functionize this and call it with each CPU,
# then see which of those is the highest.
#
# New Concept: file seek
#   When reading through a file, Python maintains a "cursor" so that each read continues from the last.
#   On a second read through a file, seek must be used to set this cursor back to the beginning

def average(target):
    sum = 0
    count = 0

    for line in file:
        if not target in line: continue
        process_line = line.strip()
        pre, sub, after = process_line.partition(target)
        after = after[:-1]

        sum += int(after)
        count += 1

    if count == 0: return 0
    return (sum / count)


averages = []

file = open(PATH, "r")
averages.append(average("CPU1:"))
file.seek(0)
averages.append(average("CPU2:"))
file.seek(0)
averages.append(average("CPU3:"))
file.seek(0)
averages.append(average("CPU4:"))
file.close()

highest_average = 0
highest_cpu = 0

cpu = 0
for avg in averages:
    cpu += 1
    if avg <= highest_average: break
    highest_average = avg
    highest_cpu = 1

print("CPU", highest_cpu, "had the highest average temperature, at", highest_average, "C")

# Part 3
# This one should be doable with minimal help

file = open(PATH, "r")

highest_gpu = 0
highest_time = 0

timestamp = 0
for line in file:
    print(line)
    timestamp += 1
    clean_line = line.strip()
    pre, sub, after = clean_line.partition("GPU:")
    gpu = int(after[:-1])

    if gpu > highest_gpu:
        highest_gpu = gpu
        highest_time = timestamp
