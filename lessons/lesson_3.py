# 1. Arrays are for storing several values to a single variable
numbers = [1, 1, 2, 3, 5, 8, 13]

# 2. Get a specific value from the array by using each element's index (indicees start at 0)
print(numbers[0])
print(numbers[5])

# 3. New concept - loops.  Just repeat the code in the scope a bunch
total = 0
for number in numbers:
    print("Adding", number, "to total")
    total = total + number
print("Total:", total)

# 4. Modify the loop to run a predetermined number of times
# 4.5 - new concepts: str() to conver to the string type, and using + to concatenate strings
total = 0
for i in range(5):
    total = total + int(input("enter value " + str(i) + ": "))
print("total:", total)

# 5. break exits a loop early
total = 0
for i in range(5):
    value = int(input("Enter any positive value:"))
    if value < 0:
        print("I said positive!!")
        break
    total = total + value
print("total:", total)

# 6. continue skipps an iteration
total = 0
for i in range(5):
    value = int(input("Enter a value.  Preference is not 3, absolute is must be positive: "))

    if value < 0:
        print("Must be positive")
        break

    if value == 3:
        print("shouldn't be 3 - skipping")
        continue

    print("Adding", str(value))
    total = total + value

print(total)

# 7. Same as 6, but with less printing for a nicer look
print("Enter numbers.  They should not be three and MUST be positive.")
total = 0

for i in range(5):
    value = int(input(" - "))

    if value < 0:  break
    if value == 3: continue

    total = total + value

print(total)