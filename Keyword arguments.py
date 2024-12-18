# With keywords, it is possible to explicitly which arguments will go to which parameter.

def foo(a, b, c):
    print(a, b, c)

foo(a=1, b=2, c=3)


# It is possible to have some be positional and some keywords, however there can be no positional after the keyword

def foo(a, b, c):
    print(a, b, c)

foo(1, b=2, c=3)

# It is not possible to use a keyword to assign an argument to a parameter that is already implicitly assigned with positional

def foo(a, b, c):
    print(a, b, c)

foo(1, b=2, a=3)

# It is possible to set a default value to the parameters, however a non-default can not be after a declared default

def foo(a, b=4, c=1):
    print(a, b, c)

foo(1, b=2, c=3)

# It is possible to have more parameters than arguments provided if there is a default provided

def foo(a, b, c, d=4):
    print(a, b, c, d)

foo(1, b=2, c=3)

