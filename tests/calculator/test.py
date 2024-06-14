from src.calculator.npi_calculator import eval_npi
import unittest


class TestEvalNPI(unittest.TestCase):
    """A test case for evaluating expressions in NPI (Reverse Polish Notation).

    This test case contains multiple test methods to verify the correctness of the `eval_npi` function.
    """

    def test_addition(self):
        self.assertEqual(eval_npi("3 4 +"), 7)

    def test_subtraction(self):
        self.assertEqual(eval_npi("10 4 -"), 6)

    def test_multiplication(self):
        self.assertEqual(eval_npi("3 4 *"), 12)

    def test_division(self):
        self.assertEqual(eval_npi("12 3 ÷"), 4)

    def test_division_2(self):
        self.assertEqual(eval_npi("10 2 ÷"), 5.0)

    def test_complex_expression_1(self):
        self.assertEqual(eval_npi("3 4 + 16 *"), 112)

    def test_complex_expression_2(self):
        self.assertEqual(eval_npi("5 1 2 + 4 * + 3 -"), 14)

    def test_negative_numbers_addition(self):
        self.assertEqual(eval_npi("-5 3 +"), -2)

    def test_negative_numbers_multiplication(self):
        self.assertEqual(eval_npi("-2 4 *"), -8)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            eval_npi("5 0 ÷")

    def test_invalid_input_letter(self):
        with self.assertRaises(ValueError):
            eval_npi("3 a +")

    def test_invalid_input_malformed_expression(self):
        with self.assertRaises(IndexError):
            eval_npi("3 4 + +")


if __name__ == '__main__':
    unittest.main()
