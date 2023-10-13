# doctest
def add(a, b):
    """
    >>> add(1,2)
    3
    >>> add(0,0)
    0
    >>> add(-5,-19)
    -24
    >>> add('ala', 'ma')
    'alama'
    >>> add(0.3, 0.24)
    0.54
    >>> add([1,2,3], [2,3])
    [1, 2, 3, 2, 3]


    :param a:
    :param b:
    :return:
    """
    return a + b


def test():
    """
    >>> test()
    Traceback (most recent call last):
    NotImplementedError
    """
    raise NotImplementedError


test()
