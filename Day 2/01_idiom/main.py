# Idiomy

# Wstęp z generatorami
# Tutaj, z każdą iteracją funkcja range podaje nam po jednym elemencie (po tym jak go wylicz). Nie obciążamy pamięci
# mimo to, że przewidujemy wyprintować 9 999 999 elemetów (jeden po drugim). Tylko procesor się namęczy.
# for item in range(9_999_999):
#     print(item)

# Tego nie uruchamiamy bo zje nam bardzo dużo pamięci (rzutowanie na listę, oznacza zapisanie całej zawartości listy
# w pamięci ram, a ta lista będzie miała 100 000 elementów)
# for item in list(range(1000000)):
#     print(item)

# Idiomy
# wszystkie te funkcje zachowują się właśnie trochę tak jak funkcja range

my_names = ["John", "Bob", "Alex"]

# enumerate
a = enumerate(my_names)
print(a)  # generator
print(*a)  # rozpakowanie = wysycenie generatora

# iteracja = wysycenie generatora
for idx, name in enumerate(my_names):
    print(f"{idx} - {name}")

#  rzutowanie na listę/tuple/słownik/set = wysycenie generatora
a = dict(enumerate(my_names))
print(a)

names = ["Anna", "John", "Bob"]
ages = [20, 40, 30]

# zip (jak zamek błyskawiczny)
res = zip(names, ages)
print(zip)
print(*res)

# a jak posortować równocześnie obie listy?
# lambda - funkcja anonimowa - moglibyśmy tutaj wstawić zwykłą funkcję, ale po co nadawać jej nazwę skoro używamy
# jej tylko w jednym miejscu.
data = sorted(zip(names, ages), key=lambda x: x[0])
print(data)

names, ages = zip(*data)
print(names)
print(ages)

# any
x = [True, False, True, False, False]
print(any(x))

# all
numbers = [1, 12, 14, 13, 1234, 5235, 3]
result = [item % 2 == 0 for item in numbers]
print(any(result))
print(all(result))

# paradygmat funkcyjny
# map (stosuje przekazaną funkcję (tutaj square) na każdym elemencie przekazanego typu iterowalnego (tutaj numbers).
# Zwraca typ iterowalny, który będzie podawał po kolei nowe elementy (czyli wynik działania funkcji square na starych
# elementach))
def square(param):
    return param**2

result = map(square, numbers)
print(*result)

# ale ta funkcja square jest użyta tylko w jednym miejscu, więc zróbmy to za pomocą funkcji anonimowej
result = map(lambda x: x**2, numbers)
print(*result)

# filter (stosuje funkcję boolean (czyli taką, która zwraca True lub False) na każdym elemencie przekazanego
# typu iterowalnego i zwraca typ iterowalny, który wybierał będzie tylko te elementy, dla których funkcja wygenerowała
# True
def is_even(item) -> bool:
    return item % 2 == 0

result = filter(is_even, numbers)
print(*result)

result = filter(lambda x: x % 2 == 0, numbers)
print(*result)

result = filter(is_even, map(square, numbers))
print(*result)

# reduce
import functools

result = functools.reduce(lambda x, y: x+y, numbers)
print(result)

def max_(x, y):
    return x if x > y else y

result = functools.reduce(lambda x, y: x if x>y else y, numbers)
print(result)
