def get_fib_array(element_count):
    if element_count == 1: return [1]
    if element_count == 2: return [1, 1]

    fib_array = [1, 1]
    for i in range(element_count - 2):
        new_value = fib_array[-1] + fib_array[-2]
        fib_array.append(new_value)

    return fib_array

def sum(fib_array):
    total = 0
    for i in fib_array:
        total = total + i
    print("The sum is ", total)

element_count = int(input("How far into the fibonachi series are we going? "))
fib_array = get_fib_array(element_count)
sum(fib_array)