import sys


def compute(values):
    i = 0
    while values[i] != 99:
        if values[i] is 1:
            values[values[i + 3]] = values[values[i + 1]] + values[values[i + 2]]
            i += 4
        elif values[i] is 2:
            values[values[i + 3]] = values[values[i + 1]] * values[values[i + 2]]
            i += 4
        else:
            print(f"Unexpected operand: {values[i]} at position {i}")
            sys.exit()


with open("input1.txt") as f:
    values = f.read()

values = values.rstrip().split(",")
values = [int(value) for value in values]
values[1] = 12
values[2] = 2

compute(values)

print(values[0])
