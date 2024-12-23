print("Example 1")
#
def foo():
    number = 3

number = 0
foo()
print(number)

print("\nExample 2")
# In order to modify global variable, needs Global variable_name
def foo():
    global number
    number = 3

number = 0
foo()
print(number)