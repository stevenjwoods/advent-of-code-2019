import copy

from intcode_computer import Computer


with open("input.txt") as f:
    values = f.read()

values = values.rstrip().split(",")
values = [int(value) for value in values]

for noun in range(100):
    for verb in range(100):
        values[1] = noun
        values[2] = verb
        computer = Computer(copy.deepcopy(values))
        computer.run()
        if computer.intcode[0] == 19690720:
            print(noun, verb)
            print(100 * noun + verb)
