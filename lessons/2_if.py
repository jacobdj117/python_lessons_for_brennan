# 1. Constants.  They don't exist in Python, but can be signaled by coding conventions
TARGET = 10

# 2. Get the value as an int on one line - placing operations inside call arguments
value = int(input("Enter a number: "))

# 3. if introduction with equality.
if value == TARGET:
    print("It's the right value")

# 4. elif/else indroductions with inequalities
if value < TARGET:
    print("too low")
elif value > TARGET:
    print("too high")
else:
    print("It's the right value")

# 5. ranges - introduce gte/lte and and operator
RANGE_MIN = 5
RANGE_MAX = 15
value = int(input("Enter an number"))

if value >= RANGE_MIN and value <= RANGE_MAX:
    print("in the range")
else:
    print("out of range")

# 6. Invert the range to introduce or operator
if value <= RANGE_MIN or value >= RANGE_MAX:
    print("out of range")
else:
    print("in the range")

# 7. Using text
TARGET_TEXT = "hello"
text = input("enter some text")

if text == TARGET_TEXT:
    print("it's the same")
else:
    print("not the same.  Wanted: ", TARGET_TEXT)

# 8. Invert the logic
if not text == TARGET_TEXT:
    print("not the same.  Wanted: ", TARGET_TEXT)
else:
    print("it's the same")

# 9. Booleans
same = text == TARGET_TEXT
if same:
    print("it's the same")
else:
    print("not the same.  Wanted: ", TARGET_TEXT)

same = False
if same:
    print("it's the same")
else:
    print("not the same.  Wanted: ", TARGET_TEXT)

same = True
if same:
    print("it's the same")
else:
    print("not the same.  Wanted: ", TARGET_TEXT)