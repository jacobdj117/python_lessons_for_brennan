operation_count = int(input("How many operations to perform: "))

for i in range(operation_count):
    operator = input("operator for operation " + str(i + 1) + ", or q to quit: ")
    if operator == "q": break

    operand_count = 0
    if operator == "+" or operator == "*":
        operand_count = int(input("operands:"))

    if operator == "+":
        total = 0
        for i in range(operand_count):
            total = total + float(input("operand " + str(i + 1) + ": "))
        print("result: ", total)

    elif operator == "-":
        value_1 = float(input("operand 1: "))
        value_2 = float(input("operand 2: "))
        print("result: ", value_1 - value_2)

    elif operator == "*":
        total = 1
        for i in range(operand_count):
            total = total * float(input("operand " + str(i + 1) + ": "))
        print("result", total)

    elif operator == "/":
        value_1 = float(input("operand 1: "))
        value_2 = float(input("operand 2: "))
        print("restult: ", value_1 / value_2)

    else:
        print("ERROR - valid operators are +, -, *, /")