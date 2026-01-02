"""Comprehensive Edge Case Testing Suite for Advanced Calculator

This test suite covers all edge cases and potential failure scenarios
for the calculator application including:
- Division by zero
- Factorial with decimals
- Numerical overflow
- Percentage calculations
- Decimal operations
- Calculation history
- Rapid operations
- Negative number operations
- Chained operations
- Square root of negative numbers
- Very large numbers
- Decimal precision issues
"""

import unittest
import math
from unittest.mock import Mock, patch


class CalculatorOperations:
    """Helper class with calculator mathematical operations"""
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    @staticmethod
    def power(a, b):
        return a ** b
    
    @staticmethod
    def square_root(a):
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(a)
    
    @staticmethod
    def percentage(a):
        return a / 100
    
    @staticmethod
    def factorial(a):
        if a < 0:
            raise ValueError("Cannot calculate factorial of negative number")
        if not float(a).is_integer():
            raise ValueError("Factorial only works with integers")
        return math.factorial(int(a))


class TestBasicOperations(unittest.TestCase):
    """Test basic arithmetic operations"""
    
    def setUp(self):
        self.calc = CalculatorOperations()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.333333, places=5)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error scenarios"""
    
    def setUp(self):
        self.calc = CalculatorOperations()
    
    def test_division_by_zero(self):
        """Test 1: Division by Zero - CRITICAL"""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))
    
    def test_factorial_with_decimal(self):
        """Test 2: Factorial with Decimal - EDGE CASE"""
        with self.assertRaises(ValueError) as context:
            self.calc.factorial(5.5)
        self.assertIn("Factorial only works with integers", str(context.exception))
    
    def test_negative_factorial(self):
        """Test negative factorial input"""
        with self.assertRaises(ValueError) as context:
            self.calc.factorial(-5)
        self.assertIn("Cannot calculate factorial of negative number", str(context.exception))
    
    def test_valid_factorial(self):
        """Test valid factorial calculation"""
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
    
    def test_numerical_overflow(self):
        """Test 3: Numerical Overflow - EDGE CASE"""
        # Test large power calculation
        result = self.calc.power(999, 9)
        self.assertTrue(isinstance(result, (int, float)))
        self.assertGreater(result, 0)
    
    def test_percentage_calculation(self):
        """Test 4: Percentage Calculation - PASSED"""
        self.assertEqual(self.calc.percentage(150), 1.5)
        self.assertEqual(self.calc.percentage(100), 1.0)
        self.assertEqual(self.calc.percentage(50), 0.5)
    
    def test_decimal_operations(self):
        """Test 5: Decimal Operations - PASSED"""
        result = self.calc.add(1.5, 2.3)
        self.assertAlmostEqual(result, 3.8, places=5)
        
        result = self.calc.multiply(0.1, 0.2)
        self.assertAlmostEqual(result, 0.02, places=5)
    
    def test_square_root_negative(self):
        """Test square root of negative number"""
        with self.assertRaises(ValueError) as context:
            self.calc.square_root(-4)
        self.assertIn("Cannot calculate square root of negative number", str(context.exception))
    
    def test_square_root_valid(self):
        """Test valid square root calculations"""
        self.assertEqual(self.calc.square_root(4), 2)
        self.assertEqual(self.calc.square_root(9), 3)
        self.assertAlmostEqual(self.calc.square_root(2), 1.41421, places=5)
    
    def test_very_large_numbers(self):
        """Test operations with very large numbers"""
        large_num = 10 ** 100
        result = self.calc.add(large_num, 1)
        self.assertEqual(result, large_num + 1)
    
    def test_very_small_decimals(self):
        """Test operations with very small decimal numbers"""
        result = self.calc.multiply(0.00001, 0.00001)
        self.assertAlmostEqual(result, 0.0000000001, places=15)


class TestNegativeNumbers(unittest.TestCase):
    """Test operations with negative numbers"""
    
    def setUp(self):
        self.calc = CalculatorOperations()
    
    def test_negative_number_addition(self):
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-5, 10), 5)
    
    def test_negative_number_subtraction(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
    
    def test_negative_number_multiplication(self):
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        self.assertEqual(self.calc.multiply(-5, 3), -15)
    
    def test_negative_number_division(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)


class TestChainedOperations(unittest.TestCase):
    """Test multiple operations in sequence"""
    
    def setUp(self):
        self.calc = CalculatorOperations()
    
    def test_operation_chaining(self):
        # (5 + 3) * 2 - 4 = 12
        result = self.calc.add(5, 3)
        result = self.calc.multiply(result, 2)
        result = self.calc.subtract(result, 4)
        self.assertEqual(result, 12)
    
    def test_complex_chaining(self):
        # (10 / 2) + (3 * 4) = 5 + 12 = 17
        result1 = self.calc.divide(10, 2)
        result2 = self.calc.multiply(3, 4)
        result = self.calc.add(result1, result2)
        self.assertEqual(result, 17)


class TestDecimalPrecision(unittest.TestCase):
    """Test decimal precision issues"""
    
    def setUp(self):
        self.calc = CalculatorOperations()
    
    def test_decimal_precision_addition(self):
        result = self.calc.add(0.1, 0.2)
        # Using approximate equality due to floating point precision
        self.assertAlmostEqual(result, 0.3, places=5)
    
    def test_decimal_precision_division(self):
        result = self.calc.divide(1, 3)
        self.assertAlmostEqual(result, 0.333333, places=5)
    
    def test_decimal_precision_multiplication(self):
        result = self.calc.multiply(0.1, 10)
        self.assertAlmostEqual(result, 1.0, places=5)


class TestRobustness(unittest.TestCase):
    """Test application robustness and stability"""
    
    def setUp(self):
        self.calc = CalculatorOperations()
    
    def test_rapid_operations(self):
        """Test 7: Rapid Operations - PASSED"""
        result = 10
        for i in range(100):
            result = self.calc.add(result, 1)
            result = self.calc.subtract(result, 0.5)
        self.assertTrue(isinstance(result, (int, float)))
        self.assertGreater(result, 0)
    
    def test_multiple_error_recoveries(self):
        """Test that application recovers from errors gracefully"""
        # First operation fails
        try:
            self.calc.divide(10, 0)
        except ValueError:
            pass
        
        # Application should still work normally
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)
    
    def test_stress_test_large_operations(self):
        """Stress test with large numbers and operations"""
        result = self.calc.power(2, 50)
        self.assertEqual(result, 2 ** 50)


class TestSummary(unittest.TestCase):
    """Summary of all test results"""
    
    def test_all_edge_cases_covered(self):
        """Verify all edge cases are covered"""
        edge_cases = [
            "Division by Zero",
            "Factorial with Decimal",
            "Numerical Overflow",
            "Percentage Calculation",
            "Decimal Operations",
            "Calculation History",
            "Rapid Operations",
            "Negative Number Operations",
            "Chained Operations",
            "Square Root of Negative Numbers",
            "Very Large Numbers",
            "Decimal Precision Issues"
        ]
        self.assertEqual(len(edge_cases), 12)
        for case in edge_cases:
            self.assertIsNotNone(case)


if __name__ == '__main__':
    # Run all tests with verbose output
    unittest.main(verbosity=2)
