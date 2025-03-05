value_1 = int(input("value 1: "))
operator = input("operator: ")
value_2 = int(input("value 2: "))

print()

if operator == "+":
    print("result: ", value_1 + value_2)
elif operator == "-":
    print("result: ", value_1 - value_2)
elif operator == "*":
    print("result: ", value_1 * value_2)
elif operator == "/":
    print("restul: ", value_1 / value_2)
else:
    print("ERROR - valid operators are +, -, *, /")

print()