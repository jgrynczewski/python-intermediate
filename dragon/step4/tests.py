from random import seed
from unittest import TestCase

from game import (
    Dragon,
    MakesDamage,
    HasPosition,
    HasDrop,
    HasHealth
)


class PositionTest(TestCase):
    def setUp(self) -> None:
        self.current = HasPosition(position_x=10, position_y=20, position_z=30)

    def test_position_get(self):
        x, y, z = self.current.position_get()
        self.assertEqual(x, 10)
        self.assertEqual(y, 20)
        self.assertEqual(z, 30)

    def test_position_set_default(self):
        with self.assertRaises(TypeError):
            self.current.position_set()  # noqa
        with self.assertRaises(TypeError):
            self.current.position_set(x=1)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_set(y=1)  # noqa

    def test_position_set_positional(self):
        with self.assertRaises(TypeError):
            self.current.position_set(1, 2, 3)  # noqa

    def test_position_set_keyword(self):
        self.current.position_set(x=1, y=2, z=3)
        self.assertEqual(self.current.position_x, 1)
        self.assertEqual(self.current.position_y, 2)
        self.assertEqual(self.current.position_z, 3)

    def test_position_move_positional(self):
        with self.assertRaises(TypeError):
            self.current.position_change(1)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2, 3)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2, 3, 4)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2, 3, 4, 5)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2, 3, 4, 5, 6)  # noqa

    def test_position_border_right(self):
        self.current.position_change(right=10_000)
        self.assertEqual(self.current.position_x, 1920)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 30)

    def test_position_border_left(self):
        self.current.position_change(left=10_000)
        self.assertEqual(self.current.position_x, 0)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 30)

    def test_position_border_up(self):
        self.current.position_change(up=10_000)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 0)
        self.assertEqual(self.current.position_z, 30)

    def test_position_border_down(self):
        self.current.position_change(down=10_000)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 1080)
        self.assertEqual(self.current.position_z, 30)

    def test_position_border_depth(self):
        self.current.position_change(depth=10_000)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, -100)

    def test_position_border_altitude(self):
        self.current.position_change(altitude=10_000)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 100)

    def test_position_move_keyword_right(self):
        self.current.position_change(right=1)
        self.assertEqual(self.current.position_x, 11)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 30)

    def test_position_move_keyword_left(self):
        self.current.position_change(left=1)
        self.assertEqual(self.current.position_x, 9)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 30)

    def test_position_move_keyword_up(self):
        self.current.position_change(up=1)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 19)
        self.assertEqual(self.current.position_z, 30)

    def test_position_move_keyword_down(self):
        self.current.position_change(down=1)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 21)
        self.assertEqual(self.current.position_z, 30)

    def test_position_move_keyword_depth(self):
        self.current.position_change(depth=1)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 29)

    def test_position_move_keyword_altitude(self):
        self.current.position_change(altitude=1)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 31)

    def test_position_move_keyword_axis_x(self):
        self.current.position_change(left=1, right=2)
        self.assertEqual(self.current.position_x, 11)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 30)

    def test_position_move_keyword_axis_y(self):
        self.current.position_change(up=1, down=2)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 21)
        self.assertEqual(self.current.position_z, 30)

    def test_position_move_keyword_axis_z(self):
        self.current.position_change(depth=1, altitude=2)
        self.assertEqual(self.current.position_x, 10)
        self.assertEqual(self.current.position_y, 20)
        self.assertEqual(self.current.position_z, 31)

    def test_position_move_keyword_axis_xyz(self):
        self.current.position_change(left=1, right=2, up=3, down=4, depth=5, altitude=6)
        self.assertEqual(self.current.position_x, 11)
        self.assertEqual(self.current.position_y, 21)
        self.assertEqual(self.current.position_z, 31)


class HasDropTest(TestCase):
    def setUp(self) -> None:
        seed(0)
        self.drop = HasDrop()

    def test_drop_get(self):
        drop = self.drop.get_drop()
        self.assertEqual(drop.gold, 1)

    def test_drop_gold_default(self):
        self.assertEqual(self.drop.gold, 1)

    def test_drop_gold_range(self):
        self.assertEqual(self.drop.GOLD_MIN, 0)
        self.assertEqual(self.drop.GOLD_MAX, 1)


class MakesDamageTest(TestCase):
    def setUp(self) -> None:
        self.character = MakesDamage()

    def test_damage_make(self):
        seed(0)
        dmg = self.character.make_damage()
        self.assertIsInstance(dmg, int)
        self.assertEqual(dmg, 49)

    def test_damage_range(self):
        self.assertEqual(self.character.DAMAGE_MIN, 0)
        self.assertEqual(self.character.DAMAGE_MAX, 100)


class HasHealthTest(TestCase):
    def setUp(self) -> None:
        seed(0)
        self.obj = HasHealth()

    def test_health_default(self):
        self.assertEqual(self.obj.health, 50)

    def test_health_range(self):
        self.assertEqual(self.obj.HEALTH_MIN, 1)
        self.assertEqual(self.obj.HEALTH_MAX, 100)

    def test_health_isdead_when_health_zero(self):
        with self.assertRaises(self.obj.IsDead):
            self.obj.set_health(0)
        self.assertTrue(self.obj.is_dead())

    def test_health_isdead_when_health_negative(self):
        with self.assertRaises(self.obj.IsDead):
            self.obj.set_health(-1)
        self.assertTrue(self.obj.is_dead())

    def test_health_take_damage(self):
        self.obj.set_health(2)
        self.obj.take_damage(1)
        self.assertEqual(self.obj.health, 1)


class DragonInitTest(TestCase):
    def test_init_name_default(self):
        with self.assertRaises(TypeError):
            Dragon()  # noqa

    def test_init_name_positional(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon.name, 'Wawelski')

    def test_init_name_keyword(self):
        with self.assertRaises(TypeError):
            Dragon(name='Wawelski')  # noqa

    def test_init_position_default(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon.position_x, 0)
        self.assertEqual(dragon.position_y, 0)

    def test_init_position_positional(self):
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 1, 2, 3)  # noqa

    def test_init_position_keyword(self):
        dragon = Dragon('Wawelski', position_x=1, position_y=2, position_z=3)
        self.assertEqual(dragon.position_x, 1)
        self.assertEqual(dragon.position_y, 2)
        self.assertEqual(dragon.position_z, 3)
