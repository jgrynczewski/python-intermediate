"""
* Assignment: JSON String DumpFlat
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Dump `DATA` to JSON format
    2. Run doctests - all must succeed

Polish:
    1. Zrzuć `DATA` do formatu JSON
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'
    >>> assert len(result) > 0, \
    'Variable `result` should not be empty'

    >>> print(result)
    [5.1, 3.5, 1.4, 0.2, "setosa"]
"""

import json


DATA = (5.1, 3.5, 1.4, 0.2, 'setosa')

# dump DATA to JSON format
# type: str
result = ...

# Solution
