# Rozpakowywanie kolekcji

# Literał krotki (wcale nie nawias definiuje krotkę)
t = 1, 2, 3  # pakujemy 3 wartości do jednej zmiennej
x = 1,

# wyjątkiem jest pusta krotka
y = ()  # tuple()

# pakujemy
s = "hello"
set1 = {1, 2, 3}
d = {'a': 1, 'b': 2, 'c': 3}

# rozpakowujemy (jeden obiekt (złożony z trzech wartości) do trzech zmiennych)
a, b, c = [1, 2, 3]

# rozpakowujemy
e, f, g = t
print(g)

# rozpakowujemy
x, y, z = "abc"  # noqa
print(y)

# Use case - zamiana zmiennych
a = 5  # noqa
b = 10  # noqa

a, b = b, a
print(a)
print(b)
