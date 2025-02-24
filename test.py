import unittest
from Calc import add, subtract, multiply, divide
from main import parse_and_calculate


class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        with self.assertRaises(ValueError):
            divide(10.0, 0)

    def test_parse_and_calculate_division_by_zero(self):


        with unittest.mock.patch('builtins.print') as mock_print:
            parse_and_calculate("10 / (4-4)")
            mock_print.assert_called_with("Нельзя делить на ноль!")


if __name__ == '__main__':
    unittest.main()
