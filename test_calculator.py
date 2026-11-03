import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    
    def test_add_2(self):
        self.assertEqual(self.calc.add(5, 5), 10)

    def test_subtract_1(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_subtract_2(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_multiply_1(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_2(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_divide_1(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_2(self):
        self.assertEqual(self.calc.divide(9, 3), 3)

    def test_modulo_1(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(12, 4), 0)


if __name__ == '__main__':
    unittest.main()

