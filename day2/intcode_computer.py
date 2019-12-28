

class Computer:

    def __init__(self, intcode):
        self.intcode = intcode
        self.i = 0

    def run(self):
        while True:
            instruction = self.intcode[self.i]
            opcode, parameter_modes = self.parse_instruction(str(instruction))
            if opcode == 99:
                break
            elif opcode == 1:
                self.add()
            elif opcode == 2:
                self.multiply()

    def parse_instruction(self, instruction):
        instruction = self.pad_instruction(instruction)
        parameter_modes, opcode = list(instruction[:3]), int(instruction[3:])
        parameter_modes.reverse()
        parameter_modes = [int(mode) for mode in parameter_modes]
        return opcode, parameter_modes

    @staticmethod
    def pad_instruction(instruction):
        while len(instruction) < 5:
            instruction = "0" + instruction
        return instruction

    def add(self):
        parameters = self.intcode[self.i + 1: self.i + 4]
        self.intcode[parameters[2]] = self.intcode[parameters[0]] + self.intcode[parameters[1]]
        self.i += 4

    def multiply(self):
        parameters = self.intcode[self.i + 1: self.i + 4]
        self.intcode[parameters[2]] = self.intcode[parameters[0]] * self.intcode[parameters[1]]
        self.i += 4
