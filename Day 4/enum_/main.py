from enum import Enum

# old-fashion ways
# RED = 1
# GREEN = 2
# BLUE = 3

# COLORS = {
#     "RED": 1,
#     "GREEN": 2,
#     "BLUE": 3
# }

# class Color:
#     RED = "#FF0000"
#     GREEN = '#00FF00'
#     BLUE = '#0000FF'
#
#     @classmethod
#     def get_favourite(cls):
#         return cls.RED


# Tworzenie Enum
class Color(Enum):
    RED = "#FF0000"
    GREEN = '#00FF00'
    BLUE = '#0000FF'

    @classmethod
    def get_favourite(cls):
        return cls.RED


print(type(Color.RED))
print(Color.RED.name)
print(Color.RED.value)

# Posługiwanie się Enum
# 1. porównania
choosen_color = Color.GREEN

...
if choosen_color is not Color.BLUE:
    print("Zły kolor")

# 2. Iteracje
for color in Color:
    print(color)

# 3. Rozbudowywanie
print(Color.get_favourite())

# IntEnum
from enum import IntEnum


class Status(IntEnum):
    ACTIVE = 1
    DISABLE = 2


from enum import StrEnum


class Ordinal(StrEnum):
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'E'


print(Ordinal.NORTH.lower())


# autonumerator
from enum import auto
class Car(Enum):
    BMW = auto()
    MERCEDES = auto()
    OPEL = auto()

from enum import unique


@unique
class Quality(Enum):
    GOOD = 1
    BAD = 2


class Key(Enum):
    ESC = 27
    ARROW_LEFT = 37
    DELETE = 27

