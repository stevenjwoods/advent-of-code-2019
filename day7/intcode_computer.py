import copy


class Computer:

    def __init__(self, intcode):
        self.intcode = copy.deepcopy(intcode)
        self.i = 0
        self.phase = None
        self.input_signal = 0
        self.input_count = 0

    def run(self):
        while True:
            instruction = self.intcode[self.i]
            opcode, parameter_modes = self.parse_instruction(str(instruction))
            if opcode == 99:
                break
            elif opcode == 1:
                self.add(parameter_modes)
            elif opcode == 2:
                self.multiply(parameter_modes)
            elif opcode == 3:
                self.write(self.get_input())
            elif opcode == 4:
                return self.read(parameter_modes)
            elif opcode == 5:
                self.jump_if_true(parameter_modes)
            elif opcode == 6:
                self.jump_if_false(parameter_modes)
            elif opcode == 7:
                self.less_than(parameter_modes)
            elif opcode == 8:
                self.equals(parameter_modes)

    def parse_instruction(self, instruction):
        instruction = self.pad_instruction(str(instruction))
        parameter_modes, opcode = list(instruction[:3]), int(instruction[3:])
        parameter_modes.reverse()
        parameter_modes = [int(mode) for mode in parameter_modes]
        return opcode, parameter_modes

    @staticmethod
    def pad_instruction(instruction):
        while len(instruction) < 5:
            instruction = "0" + instruction
        return instruction

    def get_parameter_values(self, parameter_modes, parameters):
        for i in range(len(parameters)):
            if parameter_modes[i] == 0:
                parameters[i] = self.intcode[parameters[i]]

    def add(self, parameter_modes):
        parameters = self.intcode[self.i + 1: self.i + 4]
        self.get_parameter_values(parameter_modes, parameters)
        self.intcode[self.intcode[self.i + 3]] = parameters[0] + parameters[1]
        self.i += 4

    def multiply(self, parameter_modes):
        parameters = self.intcode[self.i + 1: self.i + 4]
        self.get_parameter_values(parameter_modes, parameters)
        self.intcode[self.intcode[self.i + 3]] = parameters[0] * parameters[1]
        self.i += 4

    def write(self, value):
        self.intcode[self.intcode[self.i + 1]] = value
        self.i += 2

    def get_input(self):
        self.input_count += 1
        if self.input_count == 1:
            return self.phase
        else:
            return self.input_signal

    def read(self, parameter_modes):
        parameters = [self.intcode[self.i + 1]]
        self.get_parameter_values(parameter_modes, parameters)
        self.i += 2
        return parameters[0]

    def jump_if_true(self, parameter_modes):
        parameters = self.intcode[self.i + 1: self.i + 3]
        self.get_parameter_values(parameter_modes, parameters)
        if parameters[0]:
            self.i = parameters[1]
        else:
            self.i += 3

    def jump_if_false(self, parameter_modes):
        parameters = self.intcode[self.i + 1: self.i + 3]
        self.get_parameter_values(parameter_modes, parameters)
        if parameters[0]:
            self.i += 3
        else:
            self.i = parameters[1]

    def less_than(self, parameter_modes):
        parameters = self.intcode[self.i + 1: self.i + 4]
        self.get_parameter_values(parameter_modes, parameters)
        if parameters[0] < parameters[1]:
            self.intcode[self.intcode[self.i + 3]] = 1
        else:
            self.intcode[self.intcode[self.i + 3]] = 0
        self.i += 4

    def equals(self, parameter_modes):
        parameters = self.intcode[self.i + 1: self.i + 4]
        self.get_parameter_values(parameter_modes, parameters)
        if parameters[0] == parameters[1]:
            self.intcode[self.intcode[self.i + 3]] = 1
        else:
            self.intcode[self.intcode[self.i + 3]] = 0
        self.i += 4
