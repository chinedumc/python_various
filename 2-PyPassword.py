import string 
import random
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
letters = alphabet_lower + alphabet_upper
# print(letter)

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input('How many symbols would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))

pswd_letters = random.sample(letters,nr_letters)
pswd_symbols = random.sample(symbols,nr_symbols)
pswd_numbers = random.sample(numbers,nr_numbers)

pswd_list = pswd_letters+pswd_numbers+pswd_symbols
random.shuffle(pswd_list)
print(*pswd_list, sep='')
print(f"Your password is: {pswd_list}")


# for x in range(len(pswd_list)):
#   print (pswd_list[x])