import math


def circle_area(r: int|float) -> float:
    """
    Returns area of the circle

    :param r: radius
    :return: circle area
    """

    if r < 0:
        raise ValueError("Radius cannot be smaller than 0")

    return math.pi * r**2
