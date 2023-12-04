import unittest
from ipoteka import MortgageCalculator as myCalculator

class TestMortgageCalculator(unittest.TestCase):
    def test_fixed_rate_calculation(self):
        calculator = myCalculator(100000, 5, 30, fixed_rate=True, additional_payments=0)
        self.assertAlmostEqual(calculator.calculate_monthly_payment(), 536.82, delta=0.01)

    def test_variable_rate_calculation(self):
        calculator = myCalculator(100000, 5, 30, fixed_rate=False, additional_payments=0)
        self.assertAlmostEqual(calculator.calculate_monthly_payment(), 536.82, delta=0.01)

    def test_additional_payments(self):
        calculator = myCalculator(100000, 5, 30, fixed_rate=True, additional_payments=100)
        self.assertAlmostEqual(calculator.calculate_monthly_payment(), 636.82, delta=0.01)

    def test_negative_principal(self):
        with self.assertRaises(ValueError):
            calculator = myCalculator(-100000, 5, 30, fixed_rate=True, additional_payments=0)

    def test_negative_annual_rate(self):
        with self.assertRaises(ValueError):
            calculator = myCalculator(100000, -5, 30, fixed_rate=True, additional_payments=0)

    def test_negative_years(self):
        with self.assertRaises(ValueError):
            calculator = myCalculator(100000, 5, -30, fixed_rate=True, additional_payments=0)

    def test_invalid_rate_type(self):
        with self.assertRaises(TypeError):
            calculator = myCalculator(100000, "5%", 30, fixed_rate=True, additional_payments=0)

    def test_empty_additional_payments(self):
        with self.assertRaises(TypeError):
            calculator = myCalculator(100000, 5, 30, fixed_rate=True, additional_payments="")
            
if __name__ == '__main__':
    unittest.main()
