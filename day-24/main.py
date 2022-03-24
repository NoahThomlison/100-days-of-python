from fileinput import filename

with open("./input/Names/invited_names.txt") as nameFiles:
  names = (nameFiles.read())
  namesArray = names.split('\n')
with open("./input/Letters/starting_letter.text") as letter:
  letterTemplate = letter.read()

for name in namesArray:
  print (name)
  fileName = f"letter_for_{name}"
  with open(f"./output/readyToSend/{fileName}.txt", "w") as file:
    letter = letterTemplate.replace("[name]", f"{name}")
    file.write(letter)
