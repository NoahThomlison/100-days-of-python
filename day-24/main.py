with open("./input/Names/invited_names.txt") as nameFiles:
  names = nameFiles.read()

with open("./input/Letters/starting_letter.text") as letter:
  letterTemplate = letter.read()

print(names)
print(letterTemplate)

