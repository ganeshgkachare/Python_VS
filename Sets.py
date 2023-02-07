
'''
SETS

    Set is an unordered collection of data types that is iterable, mutable and has 
    no duplicate elements.

Creating a Set
    Sets can be created by using the built-in set() function with an iterable object   
    or a sequence by placing the sequence inside curly braces, separated by a ‘comma’.

Note: A set cannot have mutable elements like a list or dictionary, as it is mutable. 

    Common uses include membership testing, removing duplicates from a sequence, and computing 
    mathematical operations such as intersection, union, difference, and symmetric difference. 

'''


# set is an unordered collection of unique elements
# # Sets Creation
s = {"a","b","c","d"}
print(type(s))

s = {1, 2, 3, 4} # Set 
s1 = [1,2,3,4] # List 
s2 = (1,2,3,4) # Tuple
s3 = {1:"1", 2:"2", 3:"3", 4:"4"} # Dict
print(s3[1])
print(type(s))

s = {False, "Hola mundo", (1, 2), True, 3.14, None}
print(type(s))

# s = {[1, 2]} # TypeError unhashable type: 'list'
a = {1:"asd", 2:"fgh"}
b = (1,2,3,4,5,6)
c = {b}

# s = {{1:"1",2:"2"}}

s = {}
print(type(s))

s = set()
print(s)
print(type(s))

s1 = set([1, 2, 3, 4]) 
s2 = set(range(10))
print(s1)
print(s2)

s = list({1, 2, 3, 4})
print(s[0])

s = set([1, 2, 2, 3, 4])
print(s)

repeat = {1,1,1,1,1,1,1,1,1,1,1,1}
print(repeat)

long_list = range(10)
print(long_list)

long_list = list(long_list)
print(long_list)

long_list = long_list + [10,10,10,10,10,10,10]
print(long_list)


no_noise_data = set(long_list)
print(no_noise_data)
print(type(no_noise_data))

no_noise_data_list = list(no_noise_data)
print(no_noise_data_list)
print(type(no_noise_data_list))


list_a = [0,1,1,1,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6,6,6,6,True,True,True,True,False,False,False,"Hello","Hello","Hello"]
set_c = set(list_a)
print(set_c)

str = "this is a example"
set(str)


# using set() to create a set
a = set()
print(a)
print(type(a)) # <class 'set'>


# unique collection
list_buy = [1,12,15,14,12,48,48,48,48]
s = set(list_buy)
print(s)

list_new = [12,14,1.44,3.14,"NUm1", True, (True,False),[33,66,99]]

# v = set(list_new)
# print(list_new) # unhashable type: 'list'



list_new = [(True,False),(True,False),(True,False), False, True,12,22]
v = set(list_new)
print(v)


# set is an unordered collection of unique elements
name = "NAMAN"
print(set(name))


s = {11,22,33,44,55}
print(s)


# print(s[0]) #'set' object is not subscriptable
# print(s[2])

# we can not call elements of  a set by calling the index position

# but we can use loop for calling
for i in s:
    print(i)



# #eg. 

# s_even = {True, False, False ,25 , 'order' , [55,55,55]} #unhashable type: 'list

#           0   1       2       3       4 # this is not supported in SET
s_even = {True, False, False ,25 , 'order' } #unhashable type: 'list
print(type(s_even))

#           0  1  2
list_num = [3,33,333]
print(list_num[2]) #indexing  = order define = LIST is an ordered collection

# print(s_even[3]) # not subscriptable

print(s_even)

set_one = {'R', 'R', 'R', 'R', 'R', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'R', 'R', 'R', 'R', 'R', 'R', 'A', 'A', 'A'}

print(len(set_one))
print(set_one)


# typecasting 

print(list(set_one))


#accessing elements using a for loop


for i in set_one:
    print(i)

# tricky questions

z1 = (33)
z2 = ('33')
z3 = ("Mumbai")

print(type(z1))
print(type(z2))
print(type(z3))

print("***********")
s1 = {12,23,45,87}
s2 = {1}
s3 = {"Minskole"}
s4 = {} #<class 'dict'>


print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))


# methods
# operations on set 
# mathematical 

s = {44,55,66,55,66,'weak','order',False,True}
print(s)

# add 
s.add(77) # will add 77 in the set collection
print(s)

s.add(9999)
print(s)

s.add(True) # we can not add duplicate values
print(s)


# remove
s.remove(False)
print(s)



# sorted # retuen type is LIST
# print(sorted(s)) # instances of 'str' and 'int

s2 = {11,88,44,55,77,33,55,55}
print(sorted(s2))


#clear
s.clear()
print(s)
print(type(s))

x = set() #explicitly definig a set 
print(x)

y  = {}
print(y)
print(type(y))


# del

# del(s)
# print(s)

s3 = {11,22,33}
print(list(s3)) #constructor

a = ["A", 44 ,False, True]
a.clear()
print(a)

b = {11,22,44,77}
b.clear()
print(b)


# constructor for creating/defining a set

p = set([True,False,22,22])
print(p)


r = set((True,False,22,22))
print(r)

z = set() # empty set
print(z)


d = list()  #empty list
print(d)

e = {2,3,4,5,6,7,8}
o = {6,7,8,9,10,11}


print("--------------intersection---------------")
print(e.intersection(o))
print(e&o)
print("--------------union---------------")
print(e.union(o))
print(e|o)
print("--------------diff---------------")
print(e.difference(o))
print(e-o)
print("--------------sy.diff---------------")
print(e.symmetric_difference(o))
print(e^o)
print("-----------------------------")
print(e.issubset(o))






## Operations between sets

set_a = {1,2,3}
set_b = {4,5,6}

print(len(set_a))


set_a.add(4) #Adding an element
print(set_a)

set_c = {1,2,3}
set_c.update(set_a)
set_c.update({5})
print(set_c)


set_a.discard(1) # Remove an element
print(set_a)


# set_a.remove(1)
# print(set_a)

print(1 not in set_a)

print(3 in set_a)



set_a.clear()
print(set_a)


set_a.update({6,7,8,9})
print(set_a)

print(set_b.pop())
print(set_b)

set_b = {"hola",7,6,5,4,3, True, False}
print(set_b.pop())
print(set_b.pop())
print(set_b)

print(set_b.pop())
print(set_b)


set_c = {1,2,3,4,5,6,7,8,9}
print(set_c)


# A∪B
set_d = {1,2,3}
set_e = {4,5,6}
print(set_d | set_e) # Union

print(set_d.union(set_e)) # Union

# A∩B
set_d = {1,2,3,4,5}
set_e = {4,5,6,7,8}
print(set_d.intersection(set_e)) # Intersection

print(set_d & set_e )# Intersection


# A - B
print(set_d - set_e) # Difference

print(set_e - set_d)

print(set_d.difference(set_e)) # Difference


# AΔB
print(set_d ^ set_e) # Symmetric Difference

print(set_e.symmetric_difference(set_d)) # Symmetric Difference

# Subset: if each element of b is in a 
a = {1,2,3,4,5,6,8}
b = {2,3,4,8}
print(b.issubset(a))

print(a.issubset(a))

# Superset: if each element in a is in b
print(a.issuperset(b))

print(a.issuperset(a))








