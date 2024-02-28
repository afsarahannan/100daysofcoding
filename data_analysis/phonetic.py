student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


{"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

user_response = input("Enter a name to convert to NATO code. \n")
NATO_convertor = [phonetic_dict[letter] for letter in user_response.upper()]
print(NATO_convertor)