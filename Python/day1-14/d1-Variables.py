#For print any line we could use the command:
print("Hello world \nHello world")

#concatenate strings with:
print("Hello"+" Angela")

print("Hello"+ " " + "Angela")

#How to read data and save it 
name = input("What is yor pet's name: ")

print("Wow "+ name + ", such a cute name")

print("Hello "+ input("What is your name: "))
#This will print first the input, and the it will concatenate it with the print
'''
Example:
What is your name: 'user type'
Hello 'whatever user type'
'''

print("Hello "+ input("What is your name: ")+ "!")

# WITH ctrl + / we can make the line a comment or change it 


#VARIABLES
'''
To save
STRINGS/NUMBERS, python will detect this 

arrays/ and that kinds of things we will see it later

'''
#Knowing the lenght of the variables and printing them
len("world") # --> This will have the lenght of world that is 5, but it will not do anything, maybe we can assign it to a variable or print it directly
print(len("hello world"))
#We can use it also with input, and will print the lenght of waht user types
print(len(input("What is your favorite color: ")))

#This will print the lenght first (not what user type) and the user can type whatever to print it on console, this is not the best way to use it
print(input(len("What is your favorite color: ")))

#Can be divided like this, and can be more understandable
favAnimal = input("What is your favorite animal: ")
lenght = len(favAnimal)
print(lenght)

# HOW TO CONCATENATE VARS that are ints/numbers with strings?
# var1, var2, var3 = 1, 4, 5 
# print(var1+" 2."+var2+" 3."+var3) --> this is not right, so w=hoiw we fix this


#We are going to create a generator a for a brand name
print("WELCOME TO THR BRAND NAME GENERATOR.")
name_city = input("What's the name of the you grew up in? \n")
pet_name = input("What's your pet's name? \n")
print("Your band name could be "+name_city+" "+pet_name)