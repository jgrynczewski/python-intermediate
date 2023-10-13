"""
* Assignment: Math Algebra Matmul
* Complexity: hard
* Lines of code: 13 lines
* Time: 21 min

English:
    1. Multiply matrices using nested `for` loops
    2. Do not use any library, such as: `numpy`, `pandas`, itp
    3. Run doctests - all must succeed

Polish:
    1. Pomnóż macierze wykorzystując zagnieżdżone pętle `for`
    2. Nie wykorzystuj żadnej biblioteki, tj.: `numpy`, `pandas`, itp
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Zero matrix
    * Three nested `for` loops

Tests:
    >>> A = [[1, 0],
    ...      [0, 1]]
    >>>
    >>> B = [[4, 1],
    ...      [2, 2]]
    >>>
    >>> result(A, B)
    [[4, 1], [2, 2]]

    >>> A = [[1,0,1,0],
    ...      [0,1,1,0],
    ...      [3,2,1,0],
    ...      [4,1,2,0]]
    >>>
    >>> B = [[4,1],
    ...      [2,2],
    ...      [5,1],
    ...      [2,3]]
    >>>
    >>> result(A, B)
    [[9, 2], [7, 3], [21, 8], [28, 8]]
"""

# type: matrix = list[list[int]]
# type: Callable[[matrix, matrix], matrix]
def result(A, B):
    ...


# Solution
def result(A, B):
    result = []
    A_rows = range(len(A))
    B_rows = range(len(B))
    B_columns = range(len(B[0]))

    for i in A_rows:
        row = []

        for j in B_columns:
            total = 0

            for k in B_rows:
                total += A[i][k] * B[k][j]

            row.append(total)
        result.append(row)

    return result
