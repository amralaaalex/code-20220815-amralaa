import unittest
from bmiCalculator import bmiCalculator


class TestB(unittest.TestCase):

    def test_calculate_bmi(self):
        calc = bmiCalculator([])
        self.assertEqual(calc.calculate_bmi(75,175), 24.49)

    def test_catgeorize_bmi(self):
        calc = bmiCalculator([])
        self.assertEqual(calc.catgeorize_bmi(18.4), 'Underweight')
        self.assertEqual(calc.catgeorize_bmi(24.9), 'Normal weight')
        self.assertEqual(calc.catgeorize_bmi(34.9), 'Moderately obese')
        self.assertEqual(calc.catgeorize_bmi(39.9), 'Severely obese')

    def test_main(self):
        rows = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
            { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
            { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
            { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
        calculator = bmiCalculator(rows)
        calculator.update_rows_with_bmi()
        self.assertEqual(calculator.overweight_counter, 4)

if __name__ == '__main__':
    unittest.main()
