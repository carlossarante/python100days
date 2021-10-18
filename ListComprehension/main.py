import pandas

student_data = pandas.read_csv('./nato_phonetic_alphabet.csv')
student_dict = student_data.to_dict()

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()

#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter:row.code for (index, row) in student_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def convert_input(input_text):
    return [nato_dict[letter.upper()] for letter in input_text]

text = input("Please give me a word to give you a list: ")
print(convert_input(text))

