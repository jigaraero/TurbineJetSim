import unittest
from engine.performance import thrust

class TestPerformance(unittest.TestCase):
    def test_thrust(self):
        self.assertAlmostEqual(thrust(10, 300), 3000)

if __name__ == "__main__":
    unittest.main()
