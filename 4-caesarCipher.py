import string
a = string.ascii_lowercase
print(a)
alphabet = [*a]
print(alphabet)
print(alphabet)

encode_decode = input("Type 'encode' or 'decode':\n")
message = input("Type your message:\n").lower()
shift_value = int(input("Enter a shift value:\n"))


def encrypt(text, shift):
  code=""
  for letter in message:
    for letter in alphabet:
      code += alphabet[shift+1]
  print(code)
encrypt('hello', 5)