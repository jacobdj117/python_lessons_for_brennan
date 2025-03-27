import random

PATH = "C:/Users/Jacob/code/python_lessons_for_brennan/data/6_resource_utilization.txt"
file = open(PATH, "w")

for i in range(10000):
    file.write("Readings at time " + str(i) + "seconds:\n")
    file.write("    Temperature: " + str(random.randint(75, 95)) + "C\n")
    file.write("    CPU1:        " + str(random.randint(68, 95)) + "%\n")
    file.write("    CPU2:        " + str(random.randint(5, 30)) + "%\n")
    file.write("    CPU3:        " + str(random.randint(69, 97)) + "%\n")
    file.write("    CPU4:        " + str(random.randint(2, 18)) + "%\n")
    file.write("    GPU:         " + str(random.randint(70, 100)) + "%\n\n")