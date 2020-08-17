import unittest

from sum_of_multiples import sum_of_multiples_below


class TestNaturalMultiplesSum(unittest.TestCase):

    def test_sum_of_multiples_of_3_and_5_below_1000(self):
        self.assertEqual(sum_of_multiples_below(n=10, multipliers=[3, 5]), 23)
    
    def test_sum_of_multiples_of_3_and_5_below_4(self):
        self.assertEqual(sum_of_multiples_below(4, multipliers=[3, 5]), 3)

    def test_raise_value_error_if_not_natural(self):
        with self.assertRaises(ValueError):
            sum_of_multiples_below(n=-1, multipliers=[3, 5])

    def test_raise_value_error_if_any_multiples_not_natural(self):
        with self.assertRaises(ValueError):
            sum_of_multiples_below(n=1, multipliers=[-1, 2])
        

if __name__ == '__main__':
    unittest.main()
