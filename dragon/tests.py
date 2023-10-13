import unittest

from step1 import Dragon


class DragonInitTest(unittest.TestCase):
    def test_init_dragon_failed(self):
        self.assertRaises(TypeError, Dragon)

    def test_init_dragon_name(self):
        dragon = Dragon("Wawelski")
        self.assertEqual(dragon.name, 'Wawelski')
