alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar (text, shift, direction):
  shiftedMessage = ""
  resetAmount = 26
  if(direction == "encode"):
    shift *= 1
    resetAmount *= -1
  if(direction == "decode"):
    shift *= -1
    resetAmount *= 1

  for letter in text:
    if alphabet.index(letter)+shift < len(alphabet):
      shiftedLetter = alphabet[alphabet.index(letter)+shift]
      shiftedMessage += shiftedLetter
    else:
      shiftedLetter = alphabet[alphabet.index(letter)+shift+resetAmount]
      shiftedMessage += shiftedLetter
  return(shiftedMessage)

encodedMessage = (caesar(text, shift, direction))
dencodedMessage = (caesar(encodedMessage, shift, direction))
print(encodedMessage)
print(dencodedMessage)
