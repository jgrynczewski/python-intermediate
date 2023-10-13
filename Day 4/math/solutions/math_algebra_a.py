"""
* Assignment: Math Algebra Distance2D
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Given are two points `A: tuple[int, int]` and `B: tuple[int, int]`
    2. Coordinates are in cartesian system
    3. Points `A` and `B` are in two dimensional space
    4. Calculate distance between points using Euclidean algorithm
    5. Run doctests - all must succeed

Polish:
    1. Dane są dwa punkty `A: tuple[int, int]` i `B: tuple[int, int]`
    2. Koordynaty są w systemie kartezjańskim
    3. Punkty `A` i `B` są w dwuwymiarowej przestrzeni
    4. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> A = (1, 0)
    >>> B = (0, 1)
    >>> result(A, B)
    1.4142135623730951

    >>> result((0,0), (1,0))
    1.0

    >>> result((0,0), (1,1))
    1.4142135623730951

    >>> result((0,1), (1,1))
    1.0

    >>> result((0,10), (1,1))
    9.055385138137417
"""

from math import sqrt


# type: point = tuple[int,...]
# type: Callable[[point, point], float]
def result(A, B):
    ...


# Solution
def result(A, B):
    x1 = A[0]
    y1 = A[1]
    x2 = B[0]
    y2 = B[1]

    dx = (x2-x1)
    dy = (y2-y1)

    return sqrt(dx**2 + dy**2)
