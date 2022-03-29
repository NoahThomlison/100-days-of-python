import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
natoAlphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
natoAlphabetDict = {row["letter"]: row["code"] for (index, row) in natoAlphabet.iterrows()}
print(natoAlphabetDict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generateNato():
  word = input("Enter a word: ").upper()
  try:
    wordNato = [natoAlphabetDict[letter] for letter in word]
  except KeyError:
    print("Sorry, only letters in the alphabet please.")
    generateNato()
  else:  
    print (wordNato)
  
generateNato()