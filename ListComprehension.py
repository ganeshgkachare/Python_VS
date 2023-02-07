"""
List Comprehension
    List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
"""

# Looping Using List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
[print(x) for x in fruits]


# eg.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
    if "a" in x:
        new_list.append(x)
print(new_list)

# Using list comprehension :

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [x for x in fruits if "a" in x]
print(new_list)


"""
Syntax
    new_list = [expression for item in iterable if condition == True]
    The return value is a new list, leaving the old list unchanged.
"""

# Only accept items that are not "apple":
new_list = [x for x in fruits if x != "apple"]
print(new_list)


# Iterable
new_list = [x for x in fruits]
print(new_list)


# Using range() function to create an iterable:
new_list = [x for x in range(10)]
print(new_list)


# Accept only numbers lower than 5:
new_list = [x for x in range(10) if x < 5]
print(new_list)


# Set the values in the new list to upper case:
new_list = [x.upper() for x in fruits]
print(new_list)





# List contains square of all odd numbers from range 1 to 10
odd_square = []
for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x**2)
 
print(odd_square)

odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)