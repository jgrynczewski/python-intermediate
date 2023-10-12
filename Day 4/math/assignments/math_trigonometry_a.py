"""
* Assignment: Math Trigonometry Deg2Rad
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Read input (angle in degrees) from user
    2. User will type `int` or `float`
    3. Print all trigonometric functions (sin, cos, tg, ctg)
    4. If there is no value for this angle, raise an exception
    5. Round results to two decimal places
    6. Run doctests - all must succeed

Polish:
    1. Program wczytuje od użytkownika wielkość kąta w stopniach
    2. Użytkownik zawsze podaje `int` albo `float`
    3. Wyświetl wartość funkcji trygonometrycznych (sin, cos, tg, ctg)
    4. Jeżeli funkcja trygonometryczna nie istnieje dla danego kąta podnieś
       stosowny wyjątek
    5. Wyniki zaokrąglij do dwóch miejsc po przecinku
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result_sin
    0.02
    >>> result_cos
    1.0
    >>> result_tg
    0.02
    >>> result_ctg
    57.29
    >>> result_pi
    3.14
"""

import math
from unittest.mock import MagicMock


PRECISION = 2

# Simulate user input (for test automation)
input = MagicMock(side_effect=['1'])
degrees = input('What is the angle [deg]?: ')


result_sin = ...
result_cos = ...
result_tg = ...
result_ctg = ...
result_pi = ...


# Solution
