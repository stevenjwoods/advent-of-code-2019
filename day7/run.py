import itertools

from intcode_computer import Computer

with open("input.txt") as f:
    values = f.read()

values = values.rstrip().split(",")
values = [int(x) for x in values]

signal = 0
output = 0
biggest_output = 0

# combinations = itertools.permutations([0, 1, 2, 3, 4], 5)  # For part 1
# combinations = itertools.permutations([5, 6, 7, 8, 9], 5)  # For part 2

for combination in combinations:
    combination = list(combination)
    computers = [Computer(values) for x in range(5)]

    i = 0
    for combination_value in combination:
        computers[i].phase = combination_value
        i += 1

    if combination[0] < 5:
        for computer in computers:
            computer.input_signal = signal
            signal = computer.run()
            if signal:
                output = signal
    else:
        i = 0
        x = 0
        while signal is not None:
            computers[i].input_signal = signal
            signal = computers[i].run()
            if signal:
                output = signal
            if i == len(computers) - 1:
                i = 0
            else:
                i += 1
            x += 1

    if output > biggest_output:
        biggest_output = output
    signal = 0

print(biggest_output)
