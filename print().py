"""
print():-

    The print() function prints the specified message to the screen, or other standard output device.

 
Syntax
    print(object(s), sep=separator, end=end)

By default, the value of "end" parameter is '\n', i.e. the new line character.

    Parameter	    Description
    object(s)	    Any object, and as many as you like. Will be converted to string before printed
    sep='separator'	Optional. Specify how to separate the objects, if there is more than one. Default is ' '
    end='end'	    Optional. Specify what to print at the end. Default is '\n' (line feed)

"""

# Print more than one object:
# eg.1
print("Hello", "how are you?")

# eg.2
a=2
b="Two"
print(a,b)

"""separator"""
# eg.3
print(a,b,sep="=")

# eg.4
print("Student", "Teacher", sep="--->")

# eg.5
# print "1,2,3,4,5,6" in one line using for loop :-
for i in range(1,7):
    print(i,end=",")



# print() Return Value
# It doesn't return any value; returns None.
a= print("Hi")
a
print("-----------------")
print(a)
print("Python is fun.")




a = 5
# Two objects are passed
print("a =", a)

b = a
# Three objects are passed
print('a =', a, '= b')





"""
print vs return
"""
# Printing means displaying a value in the console. To print a value in Python, you call the print() function.
#  After printing a value, you can no longer use it.
# Returning is used to return a value from a function and exit the function. To return a value from a function, 
# use the return keyword. You can use the returned value later by storing it in a variable.

def greet(name):
    print("Hello", name)
          
greet("Rahul")
greeting = greet("Rahul")
print(greeting)



def greet(name):
    return "Hello " + name
          
greeting = greet("Rahul")
print(greeting)



# Printing means showing a value in the console.
# Returning means giving back a value from a function.