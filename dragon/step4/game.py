#%% README.rst

"""
Dragon game
===========
>>> from game import Dragon  # doctest: +SKIP
>>> from random import seed; seed(0)
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3,11), 'Python 3.11+ required'

Stwórz smoka o nazwie "Wawelski"
Ustaw inicjalną pozycję smoka na x=1, y=2

>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

Ustaw nową pozycję na x=10, y=20

>>> dragon.position_set(x=10, y=20)

Przesuń smoka w lewo o 10 i w dół o 20

>>> dragon.position_change(left=10, down=20)

Przesuń smoka w lewo o 10 i w prawo o 15

>>> dragon.position_change(left=10, right=15)

Przesuń smoka w prawo o 15 i w górę o 5

>>> dragon.position_change(right=15, up=5)

Przesuń smoka w dół o 5

>>> dragon.position_change(down=5)

Smok zadaje obrażenia (5-20)

>>> dmg = dragon.make_damage()

Zadaj smokowi DMG obrażeń

>>> try:
...     dragon.take_damage(10)
...     dragon.take_damage(20)
...     dragon.take_damage(30)
...     dragon.take_damage(40)
...     dragon.take_damage(50)
... except dragon.IsDead:
...     drop = dragon.get_drop()
...     print(f'{dragon.name} is dead')
...     print(f'Gold: {drop.gold}')
Wawelski is dead
Gold: 98
"""
from random import seed, randint
from typing import NamedTuple


class HasPosition:
    POSITION_X_MIN = 0
    POSITION_X_MAX = 1920
    POSITION_Y_MIN = 0
    POSITION_Y_MAX = 1080
    POSITION_Z_MIN = -100
    POSITION_Z_MAX = 100

    position_x: int
    position_y: int
    position_z: int

    def __init__(self, position_x=0, position_y=0, position_z=0):
        self.position_set(x=position_x, y=position_y, z=position_z)

    def position_set(self, *, x, y, z=0):
        self.position_x = max(self.POSITION_X_MIN, min(self.POSITION_X_MAX, x))
        self.position_y = max(self.POSITION_Y_MIN, min(self.POSITION_Y_MAX, y))
        self.position_z = max(self.POSITION_Z_MIN, min(self.POSITION_Z_MAX, z))

    def position_change(self, *, left=0, right=0, up=0, down=0, depth=0, altitude=0):
        new_x = self.position_x + right - left
        new_y = self.position_y + down - up
        new_z = self.position_z + altitude - depth
        self.position_set(x=new_x, y=new_y, z=new_z)

    def position_get(self):
        return self.position_x, self.position_y, self.position_z


class Drop(NamedTuple):
    gold: int


class HasDrop:
    GOLD_MIN = 0
    GOLD_MAX = 1
    gold: int

    def __init__(self):
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)

    def get_drop(self):
        gold, self.gold = self.gold, 0
        return Drop(gold=gold)


class MakesDamage:
    DAMAGE_MIN = 0
    DAMAGE_MAX = 100

    def make_damage(self):
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)


class HasHealth:
    HEALTH_MIN = 1
    HEALTH_MAX = 100
    health: int

    def __init__(self):
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

    class IsDead(Exception):
        pass

    def take_damage(self, damage):
        self.set_health(self.health-damage)

    def is_dead(self):
        return self.health <= 0

    def set_health(self, value):
        self.health = value
        if self.is_dead():
            raise self.IsDead


class Dragon(HasPosition, HasDrop, HasHealth, MakesDamage):
    HEALTH_MIN = 50
    HEALTH_MAX = 120
    DAMAGE_MIN = 5
    DAMAGE_MAX = 20
    GOLD_MIN = 1
    GOLD_MAX = 100

    def __init__(self, name, /, *, position_x=0, position_y=0, position_z=0):
        self.name = name
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.position_set(x=position_x, y=position_y, z=position_z)
