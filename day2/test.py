import unittest

from intcode_computer import Computer


class TestSum(unittest.TestCase):

    def test_pad_instruction(self):
        self.assertEqual(Computer.pad_instruction("101"), "00101", "Should left-pad with two zeros (to length of 5)")

    def test_parse_instruction(self):
        self.computer = Computer([])
        instruction = "1001"
        self.assertEqual(self.computer.parse_instruction(instruction), (1, [0, 1, 0]),
                         "Should parse instruction to yield opcode and list of parameter modes")

    def test_sum(self):
        self.computer = Computer([1, 2, 3, 4, 5])
        self.computer.add()
        self.assertEqual(self.computer.intcode, [1, 2, 3, 4, 7],
                         "Should store sum of pos 2 and 3 (3 + 4 = 7) at pos 4")
        self.assertEqual(self.computer.i, 4, "Index should be incremented by 4")

    def test_multiply(self):
        self.computer = Computer([2, 0, 4, 1, 6])
        self.computer.multiply()
        self.assertEqual(self.computer.intcode, [2, 12, 4, 1, 6],
                         "Should store product of pos 0 and 4 (2 * 6 = 12) at pos 1")
        self.assertEqual(self.computer.i, 4, "Index should be incremented by 4")

    def test_run(self):
        self.computer = Computer([1, 1, 1, 4, 99, 5, 6, 0, 99])
        self.computer.run()
        self.assertEqual(self.computer.intcode, [30, 1, 1, 4, 2, 5, 6, 0, 99],
                         "Should add and then multiply to produce expected output")


if __name__ == "__main__":
    unittest.main()
