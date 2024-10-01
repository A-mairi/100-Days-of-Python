import pandas

new_data = pandas.read_csv('nato_phonetic_alphabet.csv')
#TODO 1. Create a dictionary:
new_dictionary = {row.letter: row.code for (index, row) in new_data.iterrows()}
# print(new_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter a word: ').upper()
output_list = [new_dictionary[letter] for letter in word]
print(output_list)
