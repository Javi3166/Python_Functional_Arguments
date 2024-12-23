print("Example 1")
# Simple multiplication
result = 2 * 5
print(result)

print("\nExample 2")
# Raise something to a power
result = 2 ** 3
print(result)

print("\nExample 3")
# Repeat something to initialize a list, tuple, etc.
my_list = [0, 1] * 10
my_tuple = (0, ) * 10
my_string = "AB" * 10

print(my_list)
print(my_tuple)
print(my_string)

print("Example 4")
print("\nFor use in arguments and keyword arguments in functions. See relevant module.\n")

print("\nExample 5")
# For unpacking a container. They will always result in a list.
numbers = [1, 2, 3, 4, 5, 6]

print("\nSub-example 1")
*beginning, last = numbers
print(beginning)
print(last)

print("\nSub-example 2")
beginning, *last = numbers
print(beginning)
print(last)

numbers = (1, 2, 3, 4, 5, 6)
print("\nSub-example 3")
beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)

print("\nExample 6")
# Can be used to combine tuple, list, and set into a list
my_tuple = (1, 2)
my_set = {3, 4}
my_list = [5, 6]

new_list = [*my_tuple, *my_set, *my_list]
print(new_list)

print("\nExample 7")
# Can be used to combine dictionaries
dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'd': 4}

my_dict = {**dict_1, **dict_2}
print(my_dict)