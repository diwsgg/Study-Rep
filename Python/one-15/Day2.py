#What i wanted to know the lenght of an int, can i use...

# print(len(123456))

#If I wanted to print just a letter from a word, we can use [number], example:

print("Hello"[0]) #This will print 'H'

#If we use negatives indixes, we will have the result backwards
print("Hello"[-1]) #This will print 'o'

# Lets see how the nummbers can work on python
#String
print("123"+"345") #Not a math operation, just to strings merging
#Integer
print("Sum:", 123+456) #Math operation, this time '+'
#Large integers
print(123_456_789) #Just for the code, to help us to read that, to the console will be 123456789
#FLoat
print(3.1416) #Its ok
#Boolean
print(False, True) #Only true and boolean


# How we can fix the error from len(123456),
# As we can only use it with Strings we have to convert that number into a string

print(len("123456"))

#PRINT the type of variables 
print(type("123456"))
print(type(123456))
print(type(123.456))
print(type(True))

#Type conversation, knows as type casting 

# What if I want a "string" convert to a number, so we use

print(int("123")+int("456")) #This will add the numbers (123+456=579) not merging them like strings

#But not all can be convert, for example "ABC" TO A NUMBER?

# print(int("ABC")+int("456")) ----> this will give us an error: "ValueError: invalid literal for int() with base 10: 'ABC'"

'''
But we can use differrent converts like:
int()
float()
str()
bool()
'''

# print("Numbers of letter in your name: " + len(input("Enter your name: "))) ---> 
# this will give us an error for the len function, since it returns an INT, we can not concatenate str+int, so how do we fix this

#We use:
print("Numbers of letter in your name: " + str(len(input("Enter your name: "))))

#Or to visualize this step by step
name_Of_User = input("Enter your name 2: ")
lenght_user = len(name_Of_User)
string_name = str(lenght_user)
print("Numbers of letter in your name: " +string_name)

# -------------------------------------------------------------------

'''
OPERATIONS
'''
# 1.- +
123+456

# 2.- -
123-123

# 3.- *
3*2

# 4.- /
6/2 #--> FLOAT, will implicity convert the number, so if we wanted as integer we use

# 4.1- '//'
6//2 #--> integer, but this will quit all the float numbers

# 5.- ** (Exponential)

2**3 #--> this will give us 8 (base 2, exponential 3)

# Also we can use the function round(), to round to the next or previous number, this will convert the float number into an integer one
#Example
round(1.853) # this will gave us 2
round(1.453) # this will gave us 1

#But if we add a number to the round function we will see the result

round (1.85652563542, 2) # The two after the comma, will say, only save the two decimals, like "1.85"


'''
Number Manipulation
'''
#The help us to do operations with the same variable, like this

score = 0

#If I wanted to add 1 to that value each time for .... reason i can do

score = score + 1
#For an efficient way we use 
score += 1
#And we can use others as:
score -= 1
score *= 1
score /= 1
score **= 1


