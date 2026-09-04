
#How we can create a class
class UserExample1:
    ...
    # #Or 'pass' is the same
    # # This is used when we know that we will create something but we are not developing that yet 
        

#For the classes we have the constructor, that is __init__
#this will be executed everytime a new object is created
class UserExample2:
    def __init__(self):
        #Creating starting values for attributes
        print("New user being created")
  
#WE can pass as many attributes need the object
class UserExample3:
    def __init__(self, user_id, user_name):
        #Creating starting values for attributes
        self.id = user_id
        self.username = user_name
        

#What if we do not want to pass the values of the attributes for initialize?
class UserExample4:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0

#QUESTION HOW DO I DO FOR A NEW OBJ HAVE THE COUNT OF HOW MANY HAVE BEEN CREATED AND THEN JUST CONTINUE THE COUNT??


#Executions
print("-"*50)
user_1 = UserExample2()
#HOw do we create an attribute for ours class
user_1.id = "001"
user_1.username = "name1"

print(user_1.username)

user_2 = UserExample2()
user_2.id = "002"
user_2.username = "name2"
print(user_2.username)

print("-"*50)
#So if we are expecting the attributes how we do this?
user_11 = UserExample3("01","DELL")
user_22 = UserExample3("02","LENGEND")

#now we can print the attributes for the new "USERS" like the name
print(user_11.username, user_22.username)


print("-"*50)

#Create a new objt without sending all the attributes that have for initialize 
user_111 = UserExample4("01","lloll")
user_222 = UserExample4("02","fire")

print(user_111.followers, user_222.username)

'''
how can i enter the data of that list

question_data2 = [
     {"text": "A slug's blood is green.", "answer": "True"},
]

 SO this is the position 0, inside the positition 0 is 
{"text": "A slug's blood is green.", "answer": "True"}

To access a dictionary we use index["text"]

print(question_data[0]["text"])
print(question_data[0]["answer"])
'''

