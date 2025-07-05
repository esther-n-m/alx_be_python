
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a new calculator instance for each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_sign(self):
        self.assertEqual(self.calc.add(-5, 10), 5)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 7), 7)

    # --- Subtraction Tests ---
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtraction_negative_result(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(0, 7), -7)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    # --- Multiplication Tests ---
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, -2), 8)

    def test_multiplication_mixed_sign(self):
        self.assertEqual(self.calc.multiply(-3, 6), -18)

    # --- Division Tests ---
    def test_division_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_negative_result(self):
        self.assertEqual(self.calc.divide(9, -3), -3)

    def test_division_with_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))

    def test_division_floating_point(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

if __name__ == '__main__':
    unittest.main()
