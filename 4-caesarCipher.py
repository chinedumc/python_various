import string
a = string.ascii_lowercase
print(a)
alphabet = [*a]
print(alphabet + alphabet)


message = input("Type your message:\n").lower()
shift_value = int(input("Enter a shift value:\n"))
encode_decode = input("Type 'encode' or 'decode':\n").lower()

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

def encrypt_decrypt(text, shift, encode_decode):
  if encode_decode == 'encode':
    shift = shift*1
  elif encode_decode == 'decode':
    shift *= -1
  else:
    print('Enter encode or decode')
  coded_decoded = ''
  for letter in message:
    idx = alphabet.index(letter)
    coded_decoded += alphabet[idx + shift]
  print(coded_decoded)
encrypt_decrypt(message, shift_value, encode_decode)