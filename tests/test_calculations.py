# tests/test_calculations.py - Unit tests
# Basic unit tests for calculations.

import unittest
from engine.performance import calculate_thrust  # Assuming it's exposed

class TestCalculations(unittest.TestCase):
    def test_thrust(self):
        total, momentum, pressure = calculate_thrust(50, 600, 200, 120000, 100000, 0.5)
        self.assertEqual(total, 30000.0)
        self.assertEqual(momentum, 20000)
        self.assertEqual(pressure, 10000.0)

if __name__ == '__main__':
    unittest.main()
