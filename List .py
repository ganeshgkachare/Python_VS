
"""
List
    The list is a sequence data type which is used to store the collection of data.
    List is mutable.
"""

l = [1,2,2]
print(type(l))
print(len(l))

a = [1,2,3,4,"5","6","7","Hello","World",True,False,"Houndred"] 
print(a)
print(len(a))
print(a[2])
print(a[3])

a[3] = "Four"
print(a[3])

print(a[-1])
print(a.reverse())

# iterate over the list items 

a = [1,2,3,4,"5","6","7","Hello","World",True,False,"Houndred"] 
for i in range(len(a)):
    print(a[i])

for i in a:
    print(i)

for index in range(len(a)):
    if index == len(a)-1:
        print(a[index])


for i in range(0,10):
    print(i)
    


# for l in a:
    # print(l,a[l])
    # print(a[l])


a= [1, 2, 3, 4, '5', '6', '7', 'Hello', 'World', True, False, 'Houndred']

print(a[-len(a)])


# ### Slicing

print(a[:]) # All Elements

print(a[5:]) # From 3 to foward

print(a[4:])

print(a[5:8] )# Between 5 and 8 (5,8)

print(a[:3] )# from start to 3 

print(a[::]) #start_index:Ending_index:Jump(how many index we want to skip)

#a[starting_index:ending_index:jump]

print(a[:-3] )# from start to 3 element from last 

print(a)
print(a[::2])
print(a[::-2])

print(a[::-1]) # Reverse

# ### Concatenate
b = [1,2,3,4]
c = [4,6,7,8]
n = b + c
print(set(n))


b = [1,2,3,4]
n = b + [5,6,7,8] 
print(n)


# ### Data Manipulation

a = [1,2,3,4,"5","6","7","Hello","World",True,False,"Houndred"]
print(a)

print(a[4])
print(type(a[4]))
print(type(a[5]))

a[4] = 5
print(a)
print(type(a[4]))


complex_list = [1,"1",[1],["1"],[[1],["hello"]]]
print(complex_list[4][0])
print(complex_list[4])
print(complex_list[4][1][0][0])
print(complex_list[4][1][0][1])
print(complex_list[-3])
print(complex_list[-4])


a = [1,2,3,4,"5","6","7","Hello","World",True,False,"Houndred"]

a.append("This is a another String") # Add an element
print(a)


a.remove("This is a another String") # remove element
print(a)


print(a.pop(5)) # remove element
print(a)


a[5:6] = [6,7]
print(a)


# ### Matrix or List of lists

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
M = [a,b,c]
print(M)

print(M[1][0]) # b[0]

print(M[2][0:]) # c



# The insert() method inserts an item at the specified index:
b = [8, 9, 12]
b.insert(2, 40)
print(b)

# To add an item to the end of the list, use the append() method:
b = [8, 9, 12]
b.append(40)
print(b)


b = [8, 9, 12]
b.append([23,24,25])
print(b)

# To append elements from another list to the current list, use the extend() method.
b = [8, 9, 12]
b.extend([23,24,25])
print(b)

# The remove() method removes the specified item.
b = [8, 9, 12, 23,18, 24, 25]
b.remove(18)
print(b)

# The pop() method removes the specified index.
b = [8, 9, 12, 23,18, 24, 25]
print(b.pop(2))
print(b)

# If you do not specify the index, the pop() method removes the last item.
b = [8, 9, 12, 23,18, 24, 25]
print(b.pop())
print(b)
print("---")
# The del keyword also removes the specified index:
b = [8, 9, 12, 23,18, 24, 25]
del b[3]
print(b)

# The del keyword can also delete the list completely.
b = [8, 9, 12, 23,18, 24, 25]
del b
# print(b)


# The clear() method empties the list.
b = [8, 9, 12, 23,18, 24, 25]
b.clear()
print(b)


# ort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

# Example
# Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:

# Example
# Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# There are ways to make a copy, one way is to use the built-in List method copy().

# Example
# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.

# One of the easiest ways are by using the + operator.

# Example
# Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)