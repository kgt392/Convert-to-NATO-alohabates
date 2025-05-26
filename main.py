import pandas
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
data =nato.to_dict()
phenotic_dict ={row.letter: row.code for (index,row) in nato.iterrows()}
# print(phenotic_dict)
word = input("Enter a word: ").upper()
output_list = [phenotic_dict[letter] for letter in word]
print(output_list)
