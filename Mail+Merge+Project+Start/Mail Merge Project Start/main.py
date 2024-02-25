#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt

#read the names from the invited_list
with open("./Input/Names/invited_names.txt", mode = "r") as file:
    name = file.read()
    names = name.splitlines()

#read the template from the starting_letter and then replace the [name] placeholder with the names from the names list
with open("./Input/Letters/starting_letter.txt", mode = "r") as letter_file:
    letter_content = letter_file.read()
    print(letter_content)
    for name in names:
        new_letter = letter_content.replace("[name]", name)
        #save the individual letters to yhe ready to send folder
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode = "w") as letter:
            letter.write(new_letter)

