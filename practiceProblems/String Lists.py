from audioop import reverse


input = input("Give me word to check for palindrome? ")
reverseInput = list(input)
reverseInput.reverse()
string = ""
string = string.join(reverseInput)
print(string)
if(input == string):
  print("Its a palindrome")
else:
  print("Its not a palindrome")
