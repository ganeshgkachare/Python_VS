"""
In Python, Using the input() function, we take input from a user, and using the
print() function, we display output on the screen. Using the input() function,
users can give any information to the application in the strings or numbers format.

"""

#Input() function

# The Python input() function is used to accept user inputs. This allows us to write dynamic codes in Python.

# input (): This function first takes the input from the user and converts it into a string. 

# Example:

User_input = input('Enter a number')
print('User entered:',User_input)
print(type(User_input))

#You can change input datatype by casting
#eg.1
User_input = int(input('Enter a number'))
print('User entered:',User_input)
print(type(User_input))

#eg.2
quantity = int(input('Enter a Quantity: '))
price = int(input('Enter size: '))
cost = quantity * price

print('Your item cost is: ',cost)



#Output() function
# In Python, we normally use the print() function to out a result onto the screen.

print("Hi")

num1 = 80
num2 = 90
add = num1 + num2
print(add)

str = "Python"
print(str)


##input(),output()
a = int(input("value1 "))
b = int(input("value2 "))
c = a + b
print(c)

