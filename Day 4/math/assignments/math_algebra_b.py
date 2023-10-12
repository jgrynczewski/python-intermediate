"""
* Assignment: Math Algebra DistanceND
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Given are two points `A: Sequence[int]` and `B: Sequence[int]`
    2. Coordinates are in cartesian system
    3. Points `A` and `B` are in `N`-dimensional space
    4. Points `A` and `B` must be in the same space
    5. Calculate distance between points using Euclidean algorithm
    6. Run doctests - all must succeed

Polish:
    1. Dane są dwa punkty `A: Sequence[int]` i `B: Sequence[int]`
    2. Koordynaty są w systemie kartezjańskim
    3. Punkty `A` i `B` są w `N`-wymiarowej przestrzeni
    4. Punkty `A` i `B` muszą być w tej samej przestrzeni
    5. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `for n1, n2 in zip(A, B)`

Tests:
    >>> result((0,0,0), (0,0,0))
    0.0

    >>> result((0,0,0), (1,1,1))
    1.7320508075688772

    >>> result((0,1,0,1), (1,1,0,0))
    1.4142135623730951

    >>> result((0,0,1,0,1), (1,1,0,0,1))
    1.7320508075688772

    >>> result((0,0,1,0,1), (1,1))
    Traceback (most recent call last):
    ValueError: Points must be in the same dimensions
"""

from math import sqrt


# type: point = tuple[int,...]
# type: Callable[[point, point], float]
def result(A, B):
    ...


# Solution
