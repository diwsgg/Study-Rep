#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#We define the paths
from pathlib import Path
folder_path = Path(__file__).parent

#names
names_path = folder_path / "Input"/ "Names" / "invited_names.txt"
#start letter
starting_path = folder_path / "Input"/ "Letters" / "starting_letter.txt"
#Output dir
output_path = folder_path / "Output"/ "ReadyToSend"

#Get the files
with open(names_path,"r") as names:
    file_names = [lines.strip() for lines in names.readlines()]

with open(starting_path,"r") as starting:
    file_letter = starting.read()

for word in file_names:
    newletter = file_letter
    newletter = newletter.replace("[name]",word)
    #path
    newOut = str(output_path)+'/'+word+'_letter.txt'
    with open(newOut,'w') as fileout:
        fileout.write(newletter)
    
print("Letters on ReadyToSend")