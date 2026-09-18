import turtle
import pandas as pd
from pathlib import Path

#This will return the dir that we open on visual studio on py files
# folder_path = Path.cwd()
# print(folder_path)

#it is recommend to use in py __file__.parent
folder_path = Path(__file__).parent
#we have to only the sub dirs if necessary
image_path = folder_path / "images"/ "blank_states_img.gif"
coor_path = folder_path / "csvdata"/ "50_states.csv"

data = pd.read_csv(coor_path)

screen = turtle.Screen()
screen.title("US States Game")
image = str(image_path)
screen.addshape(image)
turtle.shape(image)

# answer_state = screen.textinput("Guess the state", "Whats another state's name")

# # What I wanted to do is compare if answer_state is on data[state]
# # if it is then print the name of that country on the coordenates of it
# # if is not it will return nothing
# state = data[data.state == answer_state]
# print(state)

# #With this we have access to the x and y coordenates
# #But this is not a string neither an int its a DataFrame
# print(state.x)
# print(state.y)


#Create the US NAMES PROJECT
#We will create a nother turtle for write the names without moving the map
t = turtle.Turtle()
t.hideturtle()
t.penup()

#A counter for the loop
counter_States = 0

#how we will print the names 
def printNamesContries(x,y,name):
    t.goto(x,y)
    t.write(name, align="center", font=("Courier", 10, "bold"))

#a list to fill the states that user guess
guessStates = []

#We will repeat until counter is 50
while counter_States<51:
    #The only error with title if user put cancel then it will stop for an error
    answer_state = screen.textinput(f"{counter_States}/50 States Correct", "Whats another state's name").title()
    if answer_state == 'Exit':
        break
    #Register the answer
    state = data[data.state == answer_state]
    #is state is null we do not count that
    #As state is a dataframe we use .empty to check if we have some result
    if not state.empty:
        #get the x and y coordenates
        # iloc[0] will help us to grab the value and not the index (0, will grab the first value position)
        xcoord = state.x.iloc[0]
        ycoord = state.y.iloc[0] 
        name = state.state.iloc[0]
        #Now we can print that
        printNamesContries(xcoord,ycoord,name)

        guessStates.append(name)
        #add that to the counter
        counter_States+=1

#after the loop 
#~ this means not so
#we are asking for the ones that are in guessStates we wanted the rest
states_to_learn = data[~data.state.isin(guessStates)]

states_to_learn_path = folder_path / "csvdata" / "states_to_learn.csv"

# if we wanted only the states without the coordenates
states_to_learn = states_to_learn[["state"]]

states_to_learn.to_csv(states_to_learn_path)