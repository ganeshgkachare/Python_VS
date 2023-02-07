"""
Python Modules:-

    In Python, modules refer to the Python file, which contains Python code like Python statements, classes, functions, variables, etc.
    The benefit of modules is, it provides a way to share reusable functions.

Types of modules
    In Python, there are two types of modules:-
        1) Built-in Modules
        2) User-defined Modules

1) Built-in modules:-
    Built-in modules come with default Python installation. 
    Some commonly used Python built-in modules are datetime, os, math, sys, random, etc.

2) User-defined modules:-
    The modules which the user defines or create are called a user-defined module. We can create our own module, 
    which contains classes, functions, variables, etc., as per our requirements.

"""
"""
How to import modules?

Python Import:-
    We do not also have to write Python code from scratch to accomplish certain tasks. Python
    having several inbuilt modules that are already coded to perform some task and we can 
    easily use these modules to accomplish our task without us coding these functionalities from scratch.
"""
"""
To import modules in Python, we use the Python import keyword.
Syntax :-
        import module_name
With the help of the import keyword, both the built-in and user-defined modules are imported.
"""
import math
print(math.sqrt(25))


# For finding factorial we have to write function

def fact (x):
    fact = 1
    for i in range(1,x+1):
        fact*=i
    return fact

print(fact (2))
print(fact (3))
print(fact (4))
print(fact (5))


#Also we can find factorial without function by imorting the module

import math

print(math.factorial(2))
print(math.factorial(3))
print(math.factorial(4))
print(math.factorial(5))



"""
To import particular classes or functions, we can use the from...import statement. 
Syntax of from...import statement :-
        from module_name import function_name
"""
# import only factorial function from math module

from math import factorial

print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))


"""
Renaming the Python module:-

    Import with renaming a module
    If we want to use the module with a different name, we can use from..import…as statement.
    It is also possible to import a particular method and use that method with a different name. It is called aliasing

Syntax of from...import ...as keyword:-
        from module_name import function_name as alias_name
"""

# importing sqrt() and factorial from the module math
import math as mt

# if we simply do "import math", then math.sqrt(25) and math.factorial() are required.
print(mt.sqrt(25))
print(mt.factorial(5))



# if we do "from math import factorial" and "from math import sqrt" , then math.sqrt(25) and math.factorial() are not required.

from math import sqrt
from math import sqrt

print(sqrt(25))
print(factorial(5))



"""
What is PIP?

PIP is a package manager for Python packages, or modules if you like.

What is a Package?
A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.
"""

# A module is basically a bunch of related code saved in a file with the extension .py
# Python packages are basically a directory of a collection of modules.
# a package is a collection of modules, a library is a collection of packages.

"""
Python PIP Packages
Download a Package
Downloading a package is very easy.

Open the command line interface and tell PIP to download the package you want

syntax:-
    pip install package_name
"""
# eg. pip install numpy
