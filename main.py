alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
  new_word_list = []

  for letter in text:
    index = alphabet.index(letter)
    new_word_list.append(alphabet[index+shift])
  new_word = ''.join(new_word_list)
  print(new_word)
    
encrypt(text, shift)
  
