import copy
import sys


def compute(values):
    i = 0
    while values[i] != 99:
        if values[i] == 1:
            values[values[i + 3]] = values[values[i + 1]] + values[values[i + 2]]
            i += 4
        elif values[i] == 2:
            values[values[i + 3]] = values[values[i + 1]] * values[values[i + 2]]
            i += 4
        else:
            print(f"Unexpected operand: {values[i]} at position {i}")
            sys.exit()


with open("input.txt") as f:
    values = f.read()

values = values.rstrip().split(",")
values = [int(value) for value in values]

for noun in range(100):
    for verb in range(100):
        values[1] = noun
        values[2] = verb
        memory = copy.deepcopy(values)
        compute(memory)
        if memory[0] == 19690720:
            print(noun, verb)
            print(100 * noun + verb)
