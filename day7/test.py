import unittest

from intcode_computer import Computer


class TestComputer(unittest.TestCase):

    def test_pad_instruction(self):
        self.assertEqual("00101", Computer.pad_instruction("101"), "Should left-pad with two zeros (to length of 5)")

    def test_parse_instruction(self):
        self.computer = Computer([])
        instruction = 1001
        self.assertEqual((1, [0, 1, 0]), self.computer.parse_instruction(instruction),
                         "Should parse instruction to yield opcode and list of parameter modes")

    def test_sum(self):
        self.computer = Computer([1, 2, 3, 4, 5])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.computer.add(parameter_modes=parameter_modes)
        self.assertEqual([1, 2, 3, 4, 7], self.computer.intcode,
                         "Should store sum of pos 2 and 3 (3 + 4 = 7) at pos 4")
        self.assertEqual(4, self.computer.i, "Index should be incremented by 4")

    def test_sum_with_immediate_mode(self):
        self.computer = Computer([1001, 2, 3, 4, 5])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.computer.add(parameter_modes=parameter_modes)
        self.assertEqual([1001, 2, 3, 4, 6], self.computer.intcode,
                         "Should store sum of pos 2 and val 3 (3 + 3 = 6) at pos 4")
        self.assertEqual(4, self.computer.i, "Index should be incremented by 4")

    def test_multiply(self):
        self.computer = Computer([2, 0, 4, 1, 6])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.computer.multiply(parameter_modes=parameter_modes)
        self.assertEqual([2, 12, 4, 1, 6], self.computer.intcode,
                         "Should store product of pos 0 and 4 (2 * 6 = 12) at pos 1")
        self.assertEqual(4, self.computer.i, "Index should be incremented by 4")

    def test_multiply_with_immediate_mode(self):
        self.computer = Computer([1002, 4, 3, 1, 5])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.computer.multiply(parameter_modes=parameter_modes)
        self.assertEqual([1002, 15, 3, 1, 5], self.computer.intcode,
                         "Should store product of pos 4 and val 3 (5 * 4 = 15) at pos 1")
        self.assertEqual(4, self.computer.i, "Index should be incremented by 4")

    def test_write(self):
        self.computer = Computer([3, 2, 5, 1])
        self.computer.write(12)
        self.assertEqual([3, 2, 12, 1], self.computer.intcode,
                         "Should write input (12) to  position 2")
        self.assertEqual(2, self.computer.i, "Index should be incremented by 2")

    def test_read(self):
        self.computer = Computer([4, 2, 5, 1])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.assertEqual(5, self.computer.read(parameter_modes),
                         "Should read value at position 2")
        self.assertEqual(2, self.computer.i, "Index should be incremented by 2")

    def test_read_with_immediate_mode(self):
        self.computer = Computer([104, 2, 5, 1])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.assertEqual(2, self.computer.read(parameter_modes),
                         "Should read out the parameter (at pos 1) in immediate mode")
        self.assertEqual(2, self.computer.i, "Index should be incremented by 2")

    def test_jump_if_true(self):
        self.computer = Computer([5, 3, 4, 1, 50])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.computer.jump_if_true(parameter_modes)
        self.assertEqual(50, self.computer.i, "Index should be set to value from position 4")

        self.computer = Computer([5, 3, 4, 0, 50])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.computer.jump_if_true(parameter_modes)
        self.assertEqual(3, self.computer.i, "Index should be incremented by 3")

    def test_jump_if_true_with_immediate_mode(self):
        self.computer = Computer([1005, 3, 50, 1, 5])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.computer.jump_if_true(parameter_modes)
        self.assertEqual(50, self.computer.i, "Index should be set to 50")

    def test_jump_if_false(self):
        self.computer = Computer([5, 3, 4, 1, 50])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.computer.jump_if_false(parameter_modes)
        self.assertEqual(3, self.computer.i, "Index should be incremented by 3")

        self.computer = Computer([5, 3, 4, 0, 50])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.computer.jump_if_false(parameter_modes)
        self.assertEqual(50, self.computer.i, "Index should be set to value from position 4")

    def test_jump_if_false_with_immediate_mode(self):
        self.computer = Computer([1005, 3, 50, 0, 5])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.computer.jump_if_false(parameter_modes)
        self.assertEqual(50, self.computer.i, "Index should be set to 50")

    def test_less_than(self):
        self.computer = Computer([7, 1, 2, 3])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.computer.less_than(parameter_modes=parameter_modes)
        self.assertEqual([7, 1, 2, 1], self.computer.intcode,
                         "Should store 1 in position given by third param")
        self.assertEqual(4, self.computer.i, "Index should be incremented by 4")

        self.computer = Computer([7, 0, 3, 2])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.computer.less_than(parameter_modes=parameter_modes)
        self.assertEqual([7, 0, 0, 2], self.computer.intcode,
                         "Should store 0 in position given by third param")
        self.assertEqual(4, self.computer.i, "Index should be incremented by 4")

    def test_equals(self):
        self.computer = Computer([108, 2, 3, 2])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.computer.equals(parameter_modes=parameter_modes)
        self.assertEqual([108, 2, 1, 2], self.computer.intcode,
                         "Should store 1 at position given by third param")
        self.assertEqual(4, self.computer.i, "Index should be incremented by 4")

        self.computer = Computer([108, 5, 3, 2])
        opcode, parameter_modes = self.computer.parse_instruction(self.computer.intcode[self.computer.i])
        self.computer.equals(parameter_modes=parameter_modes)
        self.assertEqual([108, 5, 0, 2], self.computer.intcode,
                         "Should store 0 at position given by third param")
        self.assertEqual(4, self.computer.i, "Index should be incremented by 4")

    def test_run(self):
        self.computer = Computer([1, 1, 1, 4, 99, 5, 6, 0, 99])
        self.computer.run()
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], self.computer.intcode,
                         "Should add and then multiply to produce expected output")

        self.computer = Computer([1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,5,27,2,27,10,31,1,31,9,35,1,35,5,39,1,6,39,43,2,9,43,47,1,5,47,51,2,6,51,55,1,5,55,59,2,10,59,63,1,63,6,67,2,67,6,71,2,10,71,75,1,6,75,79,2,79,9,83,1,83,5,87,1,87,9,91,1,91,9,95,1,10,95,99,1,99,13,103,2,6,103,107,1,107,5,111,1,6,111,115,1,9,115,119,1,119,9,123,2,123,10,127,1,6,127,131,2,131,13,135,1,13,135,139,1,9,139,143,1,9,143,147,1,147,13,151,1,151,9,155,1,155,13,159,1,6,159,163,1,13,163,167,1,2,167,171,1,171,13,0,99,2,0,14,0])
        self.computer.run()
        self.assertEqual(3654868, self.computer.intcode[0])


if __name__ == "__main__":
    unittest.main()
