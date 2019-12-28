from intcode_computer import Computer


with open("input.txt") as f:
    values = f.read()

values = values.rstrip().split(",")
values = [int(value) for value in values]
values[1] = 12
values[2] = 2

computer = Computer(values)
computer.run()
print(computer.intcode[0])
