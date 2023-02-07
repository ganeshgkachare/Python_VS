"""
Range():-
    The range() function returns a sequence of numbers, starting from 0 by default,
    and increments by 1 (by default), and stops before a specified number.
Syntax
    range(start, stop, step)

    Parameter	Description
    start	    Optional. An integer number specifying at which position to start. Default is 0
    stop	    Required. An integer number specifying at which position to stop (not included).
    step	    Optional. An integer number specifying the incrementation. Default is 1

"""
#eg.1
a = range(10)
print(a)

for i in a:
    print (i)

#eg.2
b = list(range (6))
print(b)

#eg.3 Create a sequence of numbers from 3 to 5, and print each item in the sequence:
x = range(3, 6)
for n in x:
  print(n)

# eg.4
x = range(1, 6)
print(x)



"# Casting"
# eg.5
a = list(range(1, 6))
print(a)
print(type(a))

# eg.6
b= tuple(range(1, 10))
print(b)
print(type(b))


"#Step"
# eg.7
a = list(range(0,50,5))
print(a)
print(type(a))

# eg.8
a = list(range(0,41,4))
print(a)
print(type(a))

# eg.9
a = tuple(range(0,100,5))
print(a)
print(type(a))

# eg.10
a = list(range(0,140,50))
print(a)
print(type(a))

