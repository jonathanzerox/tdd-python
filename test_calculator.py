import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def SetUp():
        print("Setting things up")

    def TearDown():
        print("Releasing allocated resources back")

    def test_addition(self):
        calc = Calculator()
        self.assertEqual(4, calc.add(2, 2))

    def test_multiplication(self):
        calc = Calculator()
        self.assertEqual(8, calc.mul(4, 2))

if __name__ == '__main__':
    unittest.main()
