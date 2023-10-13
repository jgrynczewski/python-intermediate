# Deokrator - funkcja, która uzupełnia inną funkcję
# tutaj dekoratorem jest funckja deco
# dekorujemy funkcję func

def deco(f):

    def wrapper(*args, **kwargs):
        print("Robię coś przed wykonanie funkcji")
        f(*args, **kwargs)
        print("Robię coś po wykonaniu funkcji")

    return wrapper


# ten zapis @deco to cukier składniowy
# pod spodem wykonuje się dokładnie taka linijka kodu:
# func = deco(func)
@deco
def func(a, b):
    print(a+b)
    return a + b


func(1, 2)
