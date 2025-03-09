# For read only, use open and assign the return to a variable.
file_path = input("File path: ")
file = open(file_path, "r")

# To get use the entire file, use .read on the variable returned from open.
print(file.read())

# Remember to close your file when finished
file.close()

# It is often more usefule to go line by line.
# NEW OPERATOR: += will add the value on the right to the variable on the left.
#               variable += 1 is equivalent to variable = variable + 1
file_2 = open(file_path, "r")
line_number = 1
for line in file_2:
    print(line_number, ":", line)
    line_number += 1
file_2.close()

# Files can also be written to.  This will replace the contents of the file
# NEW CONCEPT: Escape characters
#              A character preceded by a backslash is a unique character.  Here, we use \n, which is
#              called a carriage return, and is used to make a new line and move to the beginning of
#              that line.  Note that the file path uses forward slashes to avoid unintentional escape
#              characters.
OUTPUT_FILE_PATH = "C:/Users/Jacob/code/python_lessons_for_brennan/data/5_example_output_file.txt"
file_output = open(OUTPUT_FILE_PATH, "w")
line_number = 1
for i in range(10):
    file_output.write("This is line number " + str(line_number) + "\n")
    line_number += 1
file_output.close()

# Files can also be appended to
file_2 = open(file_path, "a")
new_lines = [
    "This file isn't long enough.\n",
    "So I'm adding to it.\n",
    "I don't really have anything to say though, so here's some text:\n",
    "    text text text text text text text text text text text text text text text text"
]
for new_line in new_lines:
    file_2.write(new_line)