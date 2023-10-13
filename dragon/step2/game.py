"""
Dragon game
===========
Stwórz smoka o nazwie "Wawelski"
Ustaw inicjalną pozycję smoka na x=1, y=2
>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

Ustaw nową pozycję na x=10, y=20
>>> dragon.set_position(x=10, y=20)

Przesuń smoka w lewo o 10 i w dół o 20
>>> dragon.move(left=10, down=20)

Przesuń smoka w lewo o 10 i w prawo o 15
>>> dragon.move(left=10, down=20)

Przesuń smoka w prawo o 15 i w górę o 5
>>> dragon.move(left=10, down=20)

Przesuń smoka w dół o 5
>>> dragon.move(left=10, down=20)
"""
from unittest import TestCase


class Dragon:
    def __init__(self, name, /, *, position_x=0, position_y=0):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y

    def set_position(self, *, x, y):
        self.position_x = x
        self.position_y = y

    def move(self, *, left=0, right=0, up=0, down=0):
        self.position_x += right - left
        self.position_y += down - up
