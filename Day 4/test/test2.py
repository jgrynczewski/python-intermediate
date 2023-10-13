import unittest

from main2 import add


class TestAdd(unittest.TestCase):

    def test_add_integers(self):
        result = add(3, 4)

        #assert result == 7
        self.assertEqual(result, 7)
        self.assertEqual(add(0, 0), 0)

    def test_add_floats(self):

        result = add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3)


if __name__ == "__main__":
    unittest.main()
