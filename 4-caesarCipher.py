import string
a = string.ascii_lowercase
print(a)
alpha = [*a]
alphabet=alpha + alpha
print(alphabet)


# if(encode_decode == 'encode'):
#   def encrypt(text, shift):
#     code=""
#     for letter in message:
#       idx = alphabet.index(letter)
#       code += alphabet[idx + shift]
#     print(code)
#   encrypt(message, shift_value)

# elif(encode_decode == 'decode'):
#   def decrypt(text, shift):
#     decoded=""
#     for letter in message:
#       idx = alphabet.index(letter)
#       decoded += alphabet[idx - shift]
#     print(decoded)
#   decrypt(message, shift_value)

# else:
#   print('Enter encode or decode')

end_game = False


def encrypt_decrypt(text, shift, encode_decode):
  if encode_decode == 'encode':
    shift *= 1
  elif encode_decode == 'decode':
    shift *= -1
  else:
    print('Enter encode or decode')
  coded_decoded = ''
  for letter in message:
    idx = alphabet.index(letter)
    coded_decoded += alphabet[idx + shift]
  print(coded_decoded)

while not end_game:

  message = input("Type your message:\n").lower()
  shift_value = int(input("Enter a shift value:\n"))
  encode_decode = input("Type 'encode' or 'decode':\n").lower()

  shift_value = shift_value % 26

  encrypt_decrypt(text=message, shift=shift_value, encode_decode=encode_decode)

  new_round = input("Type 'yes' if you want to decode/encode again. Or type 'no' to quit\n").lower()

  if new_round == 'no':
    end_game = True
    print('You have exited the game')