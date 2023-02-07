"""
Docstrings in Python
    The full meaning of docstring is documentation string.
    It's specified in source code that is used, like a comment, to document a specific segment of code.

"""
# Declaring Docstrings: The docstrings are declared using '''triple single quotes''' or """triple double quotes""" just below the class,
#                       method or function declaration. All functions should have a docstring.


def add(a,b):
    """Function to add two numbers"""
    add = a+b
    return add

# Accessing Docstrings: The docstrings can be accessed using the __doc__ method of the object or using the help functio

#we can access the doctsrting as follows

add.__doc__
print(add.__doc__)

