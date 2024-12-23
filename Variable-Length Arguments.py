print("Example 1")
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3 , 4, 5, six=6, seven=7)

print("\nExample 2")
#
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3 , 4)

print("\nExample 3")
# Everything after the * must be keyword arguments
def foo(a, b, *, c, d):
    print(a, b, c, d)

foo(1, 2, c=3 , d=4)

print("\nExample 4")
#
def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)

foo(1, 2, 3, last=100)

print("\nExample 5")
# The arguments must have the same amount as the parameters
def foo(a, b, c):
    print(a, b, c)

my_list = (0, 1, 2)
foo(*my_list)

print("\nExample 6")
# The arguments must have the same amount as the parameters, as well as, have the keys match the parameters
def foo(a, b, c):
    print(a, b, c)

my_dict = {'a':1, 'b':2, 'c':3}
foo(**my_dict)