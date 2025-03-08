def params():
    operator = input("operator for operation " + str(i + 1) + ", or q to quit: ")
    if operator == "q": exit()

    operand_count = 0
    if operator == "+" or operator == "*":
        operand_count = int(input("operands:"))

    return operator, operand_count

def add(operand_count):
    total = 0
    for i in range(operand_count):
        total = total + float(input("operand " + str(i + 1) + ": "))
    print("result", total)

def subtract():
    value_1 = float(input("operand 1: "))
    value_2 = float(input("operand 2: "))
    print("result: ", value_1 - value_2)

def multiply(operand_count):
    total = 1
    for i in range(operand_count):
        total = total * float(input("operand " + str(i + 1) + ": "))
    print("result", total)

def divide():
    value_1 = float(input("operand 1: "))
    value_2 = float(input("operand 2: "))
    print("restult: ", value_1 / value_2)



operation_count = int(input("How many operations to perform: "))
for i in range(operation_count):
    operator, operand_count = params()

    if operator == "+":   add(operand_count)
    elif operator == "-": subtract()
    elif operator == "*": multiply(operand_count)
    elif operator == "/": divide()
    else: print("ERROR - valid operators are +, -, *, /")