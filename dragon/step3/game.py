"""
Dragon game
===========
>>> from random import seed; seed(0)
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3,11), 'Python 3.11+ required'

Stwórz smoka o nazwie "Wawelski"
Ustaw inicjalną pozycję smoka na x=1, y=2

>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

Ustaw nową pozycję na x=10, y=20

>>> dragon.set_position(x=10, y=20)

Przesuń smoka w lewo o 10 i w dół o 20

>>> dragon.move(left=10, down=20)

Przesuń smoka w lewo o 10 i w prawo o 15

>>> dragon.move(left=10, right=15)

Przesuń smoka w prawo o 15 i w górę o 5

>>> dragon.move(right=15, up=5)

Przesuń smoka w dół o 5

>>> dragon.move(down=5)

Smok zadaje obrażenia (5-20)

>>> dmg = dragon.make_damage()

Zadaj smokowi DMG obrażeń

>>> dragon.take_damage(10)

>>> dragon.take_damage(20)

>>> dragon.take_damage(30)

>>> dragon.take_damage(40)
Wawelski is dead
Gold: 98
Position: x=20, y=40

>>> dragon.take_damage(50)
Wawelski is dead
Gold: 98
Position: x=20, y=40
"""

from random import randint
from random import seed


class Dragon:
    HEALTH_MIN = 50
    HEALTH_MAX = 120
    DAMAGE_MIN = 5
    DAMAGE_MAX = 20
    GOLD_MIN = 1
    GOLD_MAX = 100

    def __init__(self, name, /, *, position_x=0, position_y=0):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)

    def set_position(self, *, x, y):
        self.position_x = x
        self.position_y = y

    def move(self, *, left=0, right=0, up=0, down=0):
        self.position_x += right - left
        self.position_y += down - up

    def make_damage(self):
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    def take_damage(self, damage):
        self.set_health(self.health-damage)

    def is_dead(self):
        return self.health <= 0

    def set_health(self, value):
        self.health = value
        if self.is_dead():
            self.make_dead()

    def make_dead(self):
        print(f'{self.name} is dead')
        print(f'Gold: {self.gold}')
        print(f'Position: x={self.position_x}, y={self.position_y}')
