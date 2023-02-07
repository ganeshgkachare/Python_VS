# upper()

String = "Python class"
str_u = String.upper()
print(str_u)

#lower()
a2 = "Nagpur"
b2 = String.lower()
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