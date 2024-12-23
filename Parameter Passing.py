# Immutable objects can't be changed in a function, unless they are in a mutable object
# Mutable objects can be changed in a function

print("Example 1")
def foo(a_list):
    a_list.append(4)

my_list = [1, 2, 3]
foo(my_list)
print(my_list)

print("\nExample 2")
def foo(a_list):
    a_list[0] = -100

my_list = [1, 2, 3]
foo(my_list)
print(my_list)

print("\nExample 3")
def foo(a_list):
    a_list = [200, 300, 400]

my_list = [1, 2, 3]
foo(my_list)
print(my_list)

print("\nExample 4")
def foo(a_list):
    a_list += [200, 300, 400]

my_list = [1, 2, 3]
foo(my_list)
print(my_list)

print("\nExample 5")
def foo(a_list):
    a_list = a_list + [200, 300, 400]

my_list = [1, 2, 3]
foo(my_list)
print(my_list)