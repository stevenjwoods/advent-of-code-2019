from intcode_computer import Computer


with open("input.txt") as f:
    values = f.read()

values = values.rstrip().split(",")
values = [int(value) for value in values]
computer = Computer(values)
computer.run()
