l = [1, 2, 3, 4, 5, 6]

a, b = l[0], l[1:]

# operator * po lewej stronie wyrażenia przypisania
a, b, c, *d, e, f = "ala ma kota"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

a, *b, c = {34, 2, 1, 's'}
print(a)
print(b)
print(c)

# Operator przypisania po prawej stronie wyrażenia przypisania
l1 = (1, 2, 3)
l2 = (4, 5, 6)

l = [*l1, *l2]
print(l)

d1 = {'a':1, 'b':2}
d2 = {'c':10, 'd':12}

d = [*d1, *d2]
print(d)

d = {**d1, **d2}
print(d)

s1 = 'abc'
s2 = 'cde'
s = {*s1, *s2}
print(s)

a, b, c = [10, 20, 30]

def func(a, b, c):
    print(a)
    print(b)
    print(c)

func(10, 20, 30)

l = [10, 20, 30]
func(*l)

a, b, *c = 10, 20, 'a', 'b'

def func(a, b, *args):
    print(a)
    print(b)
    print(args)


func(10, 20, 30, 'a', 'b')


def sum_(*args):
    result = 0
    for item in args:
        result += item
    return result

result = sum_(1, 2, 3, 4, 5, 6, 7, 8)
print(result)

def func(*args, d, e, f=10, **kwargs):
    print(a)
    print(b)
    # print(args)
    print(d)


func(10, d=19, e=2)

def func(a, /):
    print(a)
