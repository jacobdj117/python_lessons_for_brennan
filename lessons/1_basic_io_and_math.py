
# 1. Use print() to place text (called a string) on the terminal that started the script
# 2. In a terminal, usee 'python lesson1.py' to run the script
# 3. Define two variables that are assigned to integers.
# 4. Define a third variable that is assigned the sum of the two integers.
# 5. Use print() again, this time with a comma, to print another string and the third sum holding variable
# 7. Go the opposite direction - use input to assign a user value to a string
# 8. Print the string that the user provided
# 9. Get two more variables from the user
# 10. Convert the two new variables form strings to integers
# 11. Use print to print the sum of the two new variables - note that the calculation may be performed in the print line

# Print and variables
print("starting to learn Python!")
x = 5
y = 7
z = x + y
print("the sum of x and y is", z)

# Get variables from the user
some_string = input("enter some text: ")
print(some_string)

# Get integer input
x = input("enter an integer value for x: ")
y = input("enter an integer value for y: ")
x = int(x)
y = int(y)

# Print the sum using an inline operation this time
print("the sum of the new x and the new y is", x + y)
