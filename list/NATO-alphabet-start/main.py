student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
nato_phonetic_alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_phonetic_alphabet_data_frame)

#Loop through rows of a data frame
for (index, row) in nato_phonetic_alphabet_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    print(row.letter)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
nato_phonetic_alphabet_dict = {row.letter:row.code for (index, row) in nato_phonetic_alphabet_data_frame.iterrows()}
print(nato_phonetic_alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("input a word: ").upper()
nato_phonetic_alphabet_input_list = [nato_phonetic_alphabet_dict[letter] for letter in input_word]

print(nato_phonetic_alphabet_input_list)