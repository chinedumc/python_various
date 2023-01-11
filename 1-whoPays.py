import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(names)
index_who_pays= random.randint(0, (len(names)-1))
print(index_who_pays)
name_who_pays = names[index_who_pays]
print(name_who_pays)