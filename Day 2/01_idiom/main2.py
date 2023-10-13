# Generator (funkcja zawierająca yield)

def func_reverse(l):
    idx = len(l) - 1
    while idx >= 0:
        yield l[idx]
        idx -= 1


a = [1, 2, 3]
res = func_reverse(a)

from inspect import isgeneratorfunction, isgenerator

print(isgeneratorfunction(func_reverse))
print(isgenerator(func_reverse))

print(isgeneratorfunction(func_reverse(a)))
print(isgenerator(func_reverse(a)))
