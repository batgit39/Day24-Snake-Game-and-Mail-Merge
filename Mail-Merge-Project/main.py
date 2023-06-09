#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

data = []
with open("./Input/Names/invited_names.txt") as file:
    data = file.readlines()

x = 0
for i in data:
    data[x] = i.replace("\n", "")
    x += 1

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()  

for i in data:
    with open(f"./Output/ReadyToSend/{i}.txt", mode = "w") as file:
        file.write(letter.replace("[name]",i))
