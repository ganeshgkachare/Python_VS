'''
Data-Types:- 1) Numbers (integers, float, complex)
             2) String 
             3) lists
             4) Tuple
             5) set
             6) Dictionary

Datatypes are classified into two things
    1) Immutable and
    2) Mutable
Immutable data value: A data value which cannot be modified.
mutable data value : A data value which can be modified.

Lists and dictionaries are mutable. strings and tuples are Immutable.

To verify the type of any object in Python, use the type() function:
'''
# eg.
a = 5
print(a)
print(type(a))

b = "5"
print(b)
print(type(b))


'''
Numbers (integers, float, complex)

    Number data types store numeric values.
    Number data types store numeric values.
           1) int
           2) float
           3) complex
'''
# 1) int
#     Integer is a whole number, positive or negative or zero, without decimals.

a = 222
print(a)
print(type(a))

b = 0
print(b)
print(type(b))

a = -222
print(a)
print(type(b))



# 2) float
#    Float is a number, positive or negative or zero, containing one or more decimals.

a = 222.222
print(a)
print(type(a))

b = 0.0
print(b)
print(type(b))

a = -1.2
print(a)
print(type(b))


# 3) complex
#   Complex numbers are written with a "j" as the imaginary part.

a = 5 + 3j
print(a)
print(type(a))

b = 8j
print(b)
print(type(b))

a = -1.2j + 8
print(a)
print(type(b))


# del a
# print(a) # NameError name 'a' is not defined


'''
Python Casting (type conversion)

'''
# value assign
a = 6
b = a
print(b,type(b))


#Python Casting:- We can change int into float, float into int

a = 10
print(a,type(a))

b = float(a)
print(b,type(b)) 


a = 12.0
print(a,type(a))

b = int(a)
print(b,type(b)) 

