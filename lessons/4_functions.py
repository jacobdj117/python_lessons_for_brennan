# Quick item - appending to an array
some_arry = [1, 2, 3, 4]
some_arry.append(5)

# Lessons 1-3 already used functions:
print("function argument")
return_value = input("function argument")

# Making our own functions with no return
def void_function(an_argument):
    function_var = an_argument * an_argument
    print(function_var)

# Variable defined inside function only exists in the function
print(function_var) # this line should fail

# Use the function the same way as print, which also has no return value (it is a void function)
void_function(4) # this line should print 16

# Making a function with a return
def returning_function(an_argument):
    return an_argument * an_argument

# Use the function in the same way as input, which also returns a value
power_4 = returning_function(4)
print(power_4)

# Use the return of returning_function as the argument for print
print(returning_function(4))

# Not all functions need to receive arguments
def no_arguments():
    function_var = 4
    power = function_var * function_var
    print(power)

print(no_arguments())

# A function can return multiple values.  This is not common in other languages.
def returns_multiple():
    value_1 = 3
    value_2 = 7
    return value_1, value_2

value_a, value_b = returns_multiple()