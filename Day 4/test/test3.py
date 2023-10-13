import math
import unittest

from main3 import circle_area

class TestCircleArea(unittest.TestCase):
    """Test suit for the circle_area function."""

    def setUpClass(cls) -> None:
        """Executes at the very beggining"""
        ...
    def tearDownClass(cls) -> None:
        """Executes at the very end"""
        ...

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def test_area(self):
        """Test area for radius > 0"""
        print("test_area")
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(math.pi), math.pi**3)


    def test_negative_radius(self):
        """Test if ValueException is raised when radius has negative value"""

        print("test_negative_radius")
        self.assertRaises(ValueError, circle_area, -1)


if __name__ == "__main__":
    unittest.main()
