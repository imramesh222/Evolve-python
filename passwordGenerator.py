import random
import string



# def generatePassword(length):
#   upper=string.ascii_uppercase
#   lower=string.ascii_lowercase
#   digits=string.digits
#   sp_characters=string.punctuation
#   password=[
#     random.choice(upper),
#     random.choice(lower),
#     random.choice(digits),
#     random.choice(sp_characters)
#   ]
#   allChar=upper+lower+digits+sp_characters
#   password+=random.choices(allChar, k=length-4)
#   return "".join(password)
# pwd=generatePassword(10)
# print(pwd)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)