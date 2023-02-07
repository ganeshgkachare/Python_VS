'''
String

Strings are one of the fundamental Python data types.
It is text or words or sentence in quotation mark (single or double). 
Strings are used to represent text.

properties:
1. Strings contain individual letters or symbols called characters.
2. Characters in a string appear in a sequence, which means that each character has a numbered position in the string.
'''
# Here we assign Ganesh value to my_name variable
my_name = "Ganesh"
print(my_name)
print(len(my_name))
print(type(my_name))

# Multiline Strings :- You can assign a multiline string to a variable by using three quotes

a = '''
My
Name
Is
Ganesh
'''
print(a)
print(type(a))
print(len(a))


# Looping Through a String
for i in a:
    print(i)


'''
Indexing :-

    Indexing means referring to an element of an iterable by its position within the iterable. Each of a string’s characters corresponds to an index number and each character can be accessed using its index number. We can access characters in a String in Two ways :

    1) Accessing Characters by Positive Index Number
    2) Accessing Characters by Negative Index Number
'''

Institute = "Minskole"
print(len(Institute))
for i in Institute:
    print(i)



'''

1) Accessing Characters by Positive Index Number:
   We pass a Positive index(which we want to access) in square brackets.
 The index number starts from index number 0 (which denotes the first character of a string).


2) Accessing Characters by Negative Index Number: 
    We pass the Negative index(which we want to access) in square brackets. 
    Here the index number starts from index number -1 (which denotes the last character of a string).


    0   1   2   3   4   5   6   7   ====>  Positive Index Number
    M   i   n   s   k   o   l   e   ====>  String
    -8  -7  -6  -5  -4  -3  -2  -1  ====>  Negative Index Number

'''
print("------Indexing---------")

#Positive Index Number

print(Institute[0])     #First element
print(Institute[3])     
print(Institute[7])     
# print(Institute[9])   #IndexError :- string index out of range

# Negative Index Number

print(Institute[-8])     
print(Institute[-5])     
print(Institute[-1])    #Last element


'''
Slicing :-

    Slicing in Python is a feature that enables accessing parts of the sequence. 
    We use slicing when we require a part of the string and not the complete string.
    
Syntax :
        string[start : end : step]

    start : We provide the starting index.
    end : We provide the end index(this is not included in substring).
    step : It is an optional argument that determines the increment between each index for slicing.

'''
string = "This is python class for fullstack developement."
print(string)
print(type(string))
print(len(string))

print("------Indexing---------")
print(string[5])     # i
print(string[9])     # y

print("------Slicing---------")
print(string[8:14])     # python
print(string[15:20])    # class
print(string[:])        # Full string

str2 = "Python"
print(str2)
print(type(str2))
print(len(str2))
print(str2[0:]) 
print(str2[0:6]) 
print(str2[0:6:2]) 
print(str2[1:6:2]) 
print(str2[0:6:3]) 
print(str2[:])      # Full string
print(str2[::-1])   # Reverse string

str2 = "Python"
# str2[0] = "A"  #TypeError :-'str' object does not support item assignment
#String is immutable

#String Concatenation :-
str2 = "Python"
str3 = " Class"
str4 = str2 + str3  
print(str4)
print(str4)

#String Repetation:-
str2 = "Python"
str5 = str2 * 3
print(str5)

print("Hi" + " Good" + " Morning")
# print("Five" + 5)   #TypeError :- can only concatenate str (not "int") to str
print("Five " + '5')

"""
string + string   ===> string
string + int      ===> Error
string + str(int) ===> string

"""
"""
 String Methods :-

 syntax:-
        stringVariableName.method()
"""
String = "Python class"
# isalnum() 
# Returns True if all characters in the string are alphanumeric
str1 = String.isalnum() 

# isalnum()
# Returns True if all characters in the string are alphabet
str1 = String.isalnum() 

# isalpha()
# Returns True if all characters in the string are decimals
str1 = String.isalnum() 

# isdecimal()
# Returns True if all characters in the string are digits
str1 = String.isalnum() 

# isdigit()
# Returns True if all characters in the string are lower case

# islower()
# Returns True if all characters in the string are whitespaces

# isspace()

# isupper() 
# Returns True if all characters in the string are upper case

# lower() 
# Converts a string into lower case

# upper() 
# Converts a string into upper case

# strip() 
# It removes leading and trailing spaces in the string









# upper()

String = "Python class"
b1 = String.upper()
print(b1)

#lower()
a2 = "Nagpur"
b2 = a2.lower()
print(b2)

#isupper()
a3 = "JAIPUR"
b3 = a3.isupper()
print(b3)

#islower()
a4 = "wardha"
b4 = a4.islower()
print(b4)

#capitalize()

a5 = "raipur"
b5 = a5.capitalize()
print(b5)

# startswith()

a6 = "delhi"
b6 = a6.startswith("de")
print(b6)

#endswith()

a7 = "akola"
b7 = a7.endswith("la")
print(b7)

#index()

a8 = "goa"
b8 = a8.index("o")
print(b8)

#count()

a9 = "abhisha"
b9 = a9.count('a')
print(b9)

#replace()
a10 = "I am learning javascript"
b10 = a10.replace('javascript','python')
print(b10)

# strip

a11 = " amol "
print(len(a11))

b11 = a11.strip()
print(b11)
print(len(b11))

# split()
#   Splits the string at the specified separator, and returns a list

print("chinmaydeshpande010@gmail.com".split('@'))
print("chinmaydeshpande010@gmail.com".split('a'))
print("chinmaydeshpande010@gmail.com".split('d'))


email="ganeshgkachare@gmail.com"
print(email.split("@"))

"""
Method	        Description
capitalize()	Converts the first character to upper case
count()	        Returns the number of times a specified value occurs in a string
endswith()  	Returns true if the string ends with the specified value
find()	        Searches the string for a specified value and returns the position of where it was found
format()    	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Converts the elements of an iterable into a string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
replace()	    Returns a string where a specified value is replaced with a specified value
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
upper()	        Converts a string into upper case

"""