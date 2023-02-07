## Adding Comment :
# - Comments can be used to explain Python code.
#- To add single line comment we can use  ' # ' 

# This is single line commeent.

# - To add multiple line comment we can use Triple (single(') or double(")) quotes.
# 1) 
'''
Multiple
line
comment
'''
# 2) 
"""
Multiple
line
comment
"""
   


## Print function :
# Python was designed for readability, and has some similarities to the English language with influence from mathematics.
print("Hello World!")
print("Welcome")



''' Variable assignment : 

    Variable is used to store value and we use '=' i.e. assignment operator to assign value to it. 
'''
a = 5
print(a)
print(type(a))
b = "Python"
print(b)
print(type(b))




'''
 We have to take care of following things while writing identifiers
    1. It can be of any length . 
    2. It can be combination of lower cases (a-z) , upper cases (A-Z) and digits (0-9).
    3. It can't be start with digit.
    4. It can't be include special symbols like { !, @, #, $ , % }, etc
    5. We can use '_' i.e underscore in identifire for attaching two strings or one string and one number.
    6. We can't give space between letters, words or between letter and digit.
    7. We can't use python keywords as a python identifier

Python keywords :

    Keywords are the reserved words in Python.
    We cannot use a keyword as a variable name, function name or any other identifier. They are used to define the
    syntax and structure of the Python language.
    In Python, keywords are case sensitive.
    All the keywords except True, False and None are in lowercase and they must be written as they are.

    eg. in , and , or , if , else , elif , def , while , break , True , False , etc .**

Python identifiers
        An identifier is a name given to entities like class, functions, variables, etc. It helps to differentiate one entity
        from another.
Examples 
    We can write identifier of any length like 
    - myname
    - mynameis
'''

myname = "Chinmay"
print(myname)

mynameis = "Chinmay D"
print(mynameis)

# Identifiers using underscore  
# - my_name 
# - my_city

my_name = "Ganesh"
print(my_name)

my_city = "pune"
print(my_city)

# We can combine letters and words while writing identifiers
# - Mybirth22
Mybirth22 ="22 Aug"
print(Mybirth22)


# We can't start our identifier by digit
# - 1stvariable 
# - 19thnumber

# We can't include any special symbol at any position while writing identifier 
# - name@
# - hello!
# - time@2pm
# - $rupees
# - #brand 

# We can't write identifier using space between characcters 
# - my name 
# - my number 
# - my village 



# Assigning multiple values to multiple variables :-
a, b, c = 20, 3.14, "ABC"
print(a)
print(b)
print(c)
print(a+20)
print(type(a))
print(type(b))
print(type(c))


#Assign the same value to multiple variables at once :-
x = y = z = 100
print (x)
print (y)
print (z)
print(x,y,z)

# echo "# Python_VS" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/ganeshgkachare/Python_VS.git
# git push -u origin main

# git remote add origin https://github.com/ganeshgkachare/Python_VS.git
# git branch -M main
# git push -u origin main
git remote add origin https://github.com/ganeshgkachare/Python.git