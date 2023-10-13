# wzorce strukturalne (to trochę jak wzorce tekstowe w regex-ach, tylko że tutaj wzorcem jest jakaś struktura w pythonie np. lista)

# Match często wprowadza się jako istrukcję switch w pythonie
x = "hello"

if x == "hello":
    print("It is hello")
elif x == "hi":
    print("It is hi")

# switch x:
#     case "hello":
#         print("It is hello")
#     case "hi":
#         print("It is hi")
#     case x.startswith('he'):
#         print('he he')

match x:
    case "hello":
        print("It is hello")
    case "hi":
        print("It is hi")

# Ale match potrafi znacznie więcej niż instrukcja switch
x = (1, 2)

match x:
    case "hello" | "hi" | 5 | (1, 2, 3):
        print("super")
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Linia pozioma {y}")
    case (x, 0):
        print(f"Linia pionowa {x}")
    case (x, y) if abs(x) == abs(y):
        print(f"Przekątne główna: {x} {y}")
    case (x, y):
        print(f"Punkt: {x} {y}")
    case other:
        print(f"Coś innego {other}")


x = (1, 2, 3, 4)

match x:
    case [_]:
        print("One element")
    case [_, _]:
        print("Two elements")
    case [x, y, z]:
        print(f"Trzy elementy {x} {y} {z}")
    case [x, y, *foo]:
        print(f"Tutaj {foo}")

