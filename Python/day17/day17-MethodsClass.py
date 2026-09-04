class User:
    #Constructor (__init__, thats the diference, everytime its created will pass here first)
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0
    #For every new method, need the self parameter as the first parameter
    #That will works 
    # for knows the object that called it 
    #In this case user is the obj itself
    def follow(self, user):
        #User is another obj
        user.followers +=1
        #Self is for the one that is calling the function
        self.following +=1

#HOw do we create an attribute for ours class
user_1 = User("01","DELL")
user_2 = User("02","LENGEND")

#Use the method to change the followers
user_1.follow(user_2)

#How does this works?
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

print("-"*50)
user_1.follow(user_1)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# As we can see we can call the method with an object and also we need other one
# We can call the function for itself or to modify others

# It is important to notice that we are going to modify the value of following, every time we call the method
# even if we pass other obj, since the method is program to do that