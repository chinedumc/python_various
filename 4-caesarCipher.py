import string
a = string.ascii_lowercase
print(a)
alphabet = [*a]
print(alphabet + alphabet)


message = input("Type your message:\n").lower()
shift_value = int(input("Enter a shift value:\n"))
encode_decode = input("Type 'encode' or 'decode':\n").lower()

if(encode_decode == 'encode'):
  def encrypt(text, shift):
    code=""
    for letter in message:
      idx = alphabet.index(letter)
      code += alphabet[idx + shift]
    print(code)
  encrypt(message, shift_value)

elif(encode_decode == 'decode'):
  def decrypt(text, shift):
    decoded=""
    for letter in message:
      idx = alphabet.index(letter)
      decoded += alphabet[idx - shift]
    print(decoded)
  decrypt(message, shift_value)

else:
  print('Enter encode or decode')