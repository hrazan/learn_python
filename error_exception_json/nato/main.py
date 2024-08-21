import pandas


nato_phonetic_alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_phonetic_alphabet_data_frame)
nato_phonetic_alphabet_dict = {row.letter:row.code for (index, row) in nato_phonetic_alphabet_data_frame.iterrows()}
# print(nato_phonetic_alphabet_dict)

# while True:
#     input_word = input("input a word: ").upper()
#     # nato_phonetic_alphabet_input_list = [nato_phonetic_alphabet_dict[letter] for letter in input_word]
#     # print(nato_phonetic_alphabet_input_list)
#     try:
#         nato_phonetic_alphabet_input_list = [nato_phonetic_alphabet_dict[letter] for letter in input_word]
#     except KeyError as err:
#         print(f"{err} is not an alphanbet. Please insert just alphabets.")
#     else:
#         print(nato_phonetic_alphabet_input_list)


def generate_phonetic():
    input_word = input("input a word: ").upper()
    # nato_phonetic_alphabet_input_list = [nato_phonetic_alphabet_dict[letter] for letter in input_word]
    # print(nato_phonetic_alphabet_input_list)
    try:
        nato_phonetic_alphabet_input_list = [nato_phonetic_alphabet_dict[letter] for letter in input_word]
    except KeyError as err:
        print(f"{err} is not an alphanbet. Please insert just alphabets.")
        generate_phonetic()
    else:
        if len(nato_phonetic_alphabet_input_list) <= 0:
            print("Please input a word.")
            generate_phonetic()
        else:
            print(nato_phonetic_alphabet_input_list)

generate_phonetic()