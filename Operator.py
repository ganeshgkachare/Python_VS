'''
Operators:- 
        Operators are special symbols in Python that carry out arithmetic or logical computation. 
        The value that the operator operates on is called the operand.
    1. Arithmetic
    2. Comparison
    3. Logical
    4. Bitwise Operators
    5. Special operators :- 1) Identity operators
                            2) Membership operators
    6. Assignment operators:- 

1) Arithmetic Operators :-
    Operator	Operation	    Description	
    +	    Addition	    Adds values on either side of the operator.	
    -	    Subtraction	    Subtracts right hand operand from left hand operand.	
    *	    Multiplication	Multiplies values on either side of the operator	
    /	    Division	    Divides left hand operand by right hand operand	
    %	    Modulus	        Divides left hand operand by right hand operand and returns remainder	
    **	    Exponent    	Performs exponential (power) calculation on operators	
    //	    Floor Division	The division of operands where the result is the quotient in which
                            the digits after the decimal point are removed. 
'''

a = 10
b = 2 
print(a + b) # Addition
print(a - b) # Subtraction	
print(a * b) # Multiplication	
print(a / b) #Division

# Modulus 
a = 10
b = 2 
c = 3
print(a%b) # Remainder is 0
print(a%c) # Remainder is 1

# Exponent
a = 2
b = 4
print(a**b)
print(a*a*a*a)
print("floor")

# Floor Division
a = 40
b = 3
print(a//b)

x = 15
y = 4
print('x + y =',x+y)
print('x - y =',x-y)
print('x * y =',x*y)
print('x / y =',x/y)
print('x // y =',x//y)
print('x ** y =',x**y)


"""
2) Comparison operators:-

    Operator	    Description	
    ==	        If the values of two operands are equal, then the condition becomes true.	
    !=	        If values of two operands are not equal, then condition becomes true.
    >	        If the value of left operand is greater than the value of right operand, then condition becomes true.	
    <	        If the value of left operand is less than the value of right operand, then condition becomes true.	
    >=	        If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	
    <=	        If the value of left operand is less than or equal to the value of right operand, then condition becomes true.
"""
a = 55
b = 45
print(a == b) # False
print(a != b) # True
print(a > b) # True
print(a < b) #False
print(a >= b) #True
print(a <= b) #False

x = 20
y = 30
print('Is x greater than y :- ',x>y)
print('Is x less than y :- ',x<y)
print('Is x equal to y :- ',x==y)
print('Is x not equal to y :- ',x!=y)
print('Is x greater than or equal to y :- ',x>=y)
print('Is x less than or equal to y :- ',x<=y)

x = 10
y = 12
print('x > y is',x>y)
print('x < y is',x<y)
print('x == y is',x==y)
print('x != y is',x!=y)
print('x >= y is',x>=y)
print('x <= y is',x<=y)


'''
3) Logical Operator :-

    Operator	             Description	
    and   Logical AND	    If both the operands are true then condition becomes true.	(a and b) is true.
    or    Logical OR	    If any of the two operands are non-zero then condition becomes true. (a or b) is true.
    not   Logical NOT	    Used to reverse the logical state of its operand.

'''

x = True
y = False
print('Logical AND operation :- ',x and y) # True if both values are true
print('Logical OR operation :- ',x or y) # True if either of the values is true
print('NOT operation :- ',not x ) # True if operand is false

# and
# True  and  True  ==> True
# False and  True  ==> False
# True  and  False ==> False
# False and  False ==> False

print(12 < 13 and 7 == 7)   # True
print(12 >= 13 and 7 != 6)  # False
print(12 == 11 and 7 == 8)  # False
print(12 > 11 and 7 == 8)   #False


#or

# True  or  True  ==> True
# False or  True  ==> True
# True  or  False ==> True
# False or  False ==> False

print(12 < 13 or 7 == 7)    # True
print(12 >= 13 or 7 != 6)   # True
print(12 == 11 or 7 == 8)   # False
print(12 > 11 or 7 == 8)    # True

# not 

#True ==> False
#False ==> True 

print(not True)
print(not False)
print(not 8==8)




"""
4) Bitwise Operators
    Bitwise operators are used to compare (binary) numbers:

    Operator	Name	               Description
        & 	    AND	                Sets each bit to 1 if both bits are 1
        |	    OR	                Sets each bit to 1 if one of two bits is 1
        ^	    XOR	                Sets each bit to 1 if only one of two bits is 1
        ~ 	    NOT	                Inverts all the bits
        <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
        >>	Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""

# Bitwise and &
# It performs logical AND operation on the integer value after converting an integer to a binary value and gives 
# the result as a decimal value. It returns True only if both operands are True. Otherwise, it returns False.

a = 7
b = 4
c = 5
print(a & b)
print(a & c)
print(b & c)



# Bitwise or |
# It performs logical OR operation on the integer value after converting integer value to binary value and gives the result
#  a decimal value. It returns False only if both operands are True. Otherwise, it returns True.

a = 7
b = 4
c = 5
print(a | b)
print(a | c)
print(b | c)


# Bitwise xor ^
# It performs Logical XOR ^ operation on the binary value of a integer and gives the result as a decimal value.

a = 7
b = 4
c = 5
print(a ^ c)
print(b ^ c)


# Bitwise 1's complement ~
# It performs 1's complement operation. It invert each bit of binary value and returns the bitwise negation of a value as a result.

a = 7
b = 4
c = 3
print(~a) # -8
print(~b) # -5
print(~c) # -4  


# Bitwise left-shift <<
# The left-shift << operator performs a shifting bit of value by a given number of the place and fills 0’s to new positions.

print(4 << 2)   # 16

print(5 << 3)   # 40


# Bitwise right-shift >>
# The left-shift >> operator performs shifting a bit of value to the right by a given number of places. Here some bits are lost.

print(4 >> 2)   #1

print(5 >> 2)   #1

"""
5) Special operators :- 1) Identity operators
                        2) Membership operators
"""
"""
1) Identity operators

    Operator	Description	
      is 	    Returns true if both variables are the same object	
     is not  	Returns true if both variables are not the same object
"""
# eg
x = 10
y = 11 
z = 10

print(id(x))
print(id(y))
print(id(z))

print(x is y) 
print(x is z) 


# eg
x = 555
y = 555 
z = 300

print(id(x))
print(id(y))
print(id(z))

print(x is y) 
print(x is z) 

"""
2) Membership Operator

    Operator	   Description	
      in	        Evaluates to true if it finds a variable in the specified sequence and false otherwise.
      not in	    Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.
"""

a = 'h'
b = 'hello'
c = 'world'
print(a in b)
print(a in c)
print(a not in c)



'''
6) Assignment operators:-

        Operator	    Description	                                                            
    =	                Assigns values from right side operands to left side operand	
    +=  Add AND	        It adds right operand to the left operand and assign the result to left operand	
    -=  Subtract AND	It subtracts right operand from the left operand and assign the result to left operand	
    *=  Multiply AND	It multiplies right operand with the left operand and assign the result to left operand	
    /=  Divide AND	    It divides left operand with the right operand and assign the result to left operand	
    %=  Modulus AND	    It takes modulus using two operands and assign the result to left operand	c %= a is equivalent to 
    **=  Exponent AND	Performs exponential (power) calculation on operators and assign value to the left operand	
    //=  Floor Division	It performs floor division on operators and assign value to the left operand
'''	
# eg.
z=5
z+=2
print(z)
z-=3
print(z)
z*=2
print(z)
z**=2
print(z)
z/=2
print(z)
z//=2
print(z)
z%=2
print(z)


# eg.
a = 2
b = 2
c = 10
print(a)
a = 3
print(a)
a +=1
print(a)
b -= 1
print(b)
b *= 2
print(b)
b /= 2
print(b)
c %= 2
print(c)
c +=2
c **=2
print(c)
c //=2
print(c)



