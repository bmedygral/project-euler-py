import unittest

from fibonacci import get_fibonacci_number, sum_of_even_valued_fibonacci_numbers

class TestFibonacci(unittest.TestCase):

    def test_first_three_fibonacci_numbers(self):
        self.assertEqual(get_fibonacci_number(n=1), 1)
        self.assertEqual(get_fibonacci_number(n=2), 2)
        self.assertEqual(get_fibonacci_number(n=3), 3)
    
    def test_sixth_fibbonacci_number(self):
        self.assertEqual(get_fibonacci_number(n=6), 13)
    
    def test_sum_of_even_valued_fibonacci_numbers(self):
        self.assertEqual(sum_of_even_valued_fibonacci_numbers(upper_limit=4), 2)
        self.assertEqual(sum_of_even_valued_fibonacci_numbers(upper_limit=10), 10)
    
    def test_raise_error_if_n_is_lower_than_1(self):
        with self.assertRaises(ValueError):
            get_fibonacci_number(n=0)
    
if __name__ == '__main__':
    unittest.main()
