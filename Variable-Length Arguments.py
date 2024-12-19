def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3 , 4, 5, six=6, seven=7)

#
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3 , 4)

#
def foo(a, b, *, c, d):
    print(a, b, c, d)

foo(1, 2, c=3 , d=4)

#
def fool(*args, last):
    for arg in args:
        print(arg)
    print(last)

foo(1, 2, 3, last=100)