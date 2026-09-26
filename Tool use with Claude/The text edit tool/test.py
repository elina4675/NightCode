import unittest
import math
from main import calculate_pi


class TestPiCalculation(unittest.TestCase):
    """Test cases for the calculate_pi function"""
    
    def test_pi_5_digits(self):
        """Test pi calculation to 5 decimal places"""
        result = calculate_pi(5)
        expected = 3.14159
        self.assertEqual(result, expected, 
                        f"Expected {expected}, but got {result}")
    
    def test_pi_accuracy(self):
        """Test that calculated pi is close to math.pi"""
        result = calculate_pi(5)
        # Check that the result is within acceptable range
        self.assertAlmostEqual(result, math.pi, places=5,
                              msg=f"Calculated pi {result} not accurate enough")
    
    def test_pi_3_digits(self):
        """Test pi calculation to 3 decimal places"""
        result = calculate_pi(3)
        expected = 3.142
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
    
    def test_pi_2_digits(self):
        """Test pi calculation to 2 decimal places"""
        result = calculate_pi(2)
        expected = 3.14
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
    
    def test_pi_default_parameter(self):
        """Test that default parameter gives 5 digits"""
        result = calculate_pi()
        expected = 3.14159
        self.assertEqual(result, expected,
                        f"Expected {expected} with default parameter, but got {result}")
    
    def test_pi_first_digit(self):
        """Test that the integer part of pi is correct"""
        result = calculate_pi(5)
        self.assertEqual(int(result), 3,
                        "The integer part of pi should be 3")
    
    def test_pi_return_type(self):
        """Test that the function returns a float"""
        result = calculate_pi(5)
        self.assertIsInstance(result, float,
                            f"Expected float, but got {type(result)}")


def run_tests():
    """Run all tests and print results"""
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPiCalculation)
    
    # Run the tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*70)
    
    # Print actual calculated value
    print(f"\nCalculated Pi (5 digits): {calculate_pi(5)}")
    print(f"Actual Pi (math.pi):      {round(math.pi, 5)}")
    print(f"Difference:               {abs(calculate_pi(5) - round(math.pi, 5))}")


if __name__ == "__main__":
    run_tests()
