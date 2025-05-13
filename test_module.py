import unittest
from mean_var_std import calculate

class TestCalculate(unittest.TestCase):

    def test_valid_input_1(self):
        self.assertEqual(
            calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]),
            {
                'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
                'variance': [[6.0, 6.0, 6.0], [0.6666666666666666] * 3, 6.666666666666667],
                'standard deviation': [[2.449489742783178] * 3, [0.816496580927726] * 3, 2.581988897471611],
                'max': [[6, 7, 8], [2, 5, 8], 8],
                'min': [[0, 1, 2], [0, 3, 6], 0],
                'sum': [[9, 12, 15], [3, 12, 21], 36]
            }
        )

    def test_valid_input_2(self):
        result = calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])
        self.assertAlmostEqual(result['mean'][-1], 3.888888888888889)
        self.assertEqual(result['max'][-1], 8)
        self.assertEqual(result['min'][-1], 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate([1, 2, 3])

if __name__ == "__main__":
    unittest.main()
