# import string
from string import ascii_lowercase

'''
https://docs.python.org/3/library/functions.html

len(), type(), id(), capitalize(), upper(), lower(), strip(), find(), split(), join()
import string

'''

greeting = "hello"
user="jr"
message="happy FRIDAY"
age=20

print(greeting, user, message, age)

# Len() will print out the amount of characters including whitespaces
print(len(greeting)) # will print the total amount of characters in the string
print(len(message)) # also counts white spaces

# Type() will tell you the type of object (in python everything is an object)
print(type(age)) # prints int
print(type(user)) # prints str

# Id() will tell us the memory location of our object
print(id(age))
print(id(user))
print(id(greeting))

'''
'''


# Capitalize()
print(greeting.capitalize(), message.capitalize()) # prints "Hello", "Happy friday"

#you can have python display all of the built string objects by `print(dir(varname))` e.g. `print(dir(user))`
# print(dir(age))

# Upper() uppercases your strings
print(user.upper())
print(message.upper())

# Lower() lowercases your strings
print(user.lower())
print(message.lower())

# Strip() removes whitespaces from characters before and after a string

message1="       happy FRIDAY       "

print(message1) # prints "       happy FRIDAY       "
print(message1.strip()) # prints happy FRIDAY

#  method chaining, is you can chain methods onto one another e.g.
print(message1.strip().lower()) # prints happy friday

# Find()
message2="guess what day it is!? it's happy FRIDAY"
print(message2.find('it')) # will print 15 because it found 'it' on index 15

'''
'''

# Split() # will separate every word into it's own string separated by commas also viewed as a list data structure
print(message2.split()) # ['guess', 'what', 'day', 'it', 'is!?', "it's", 'happy', 'FRIDAY']

message3="guess-what-day-it-is!?-it's-happy-FRIDAY-!"
print(message3.split("-")) # will print ['guess', 'what', 'day', 'it', 'is!?', "it's", 'happy', 'FRIDAY', '!']

'''
'''

# Join() # will put lists into one string, specify what will be the glue, our example it's space e.g. (" ") then .join followed by the iterable or variable name e.g. print(" ".join(message4))
message4 = ['guess','what','day','it','is!?',"it's",'happy','FRIDAY','!','!'] # will print out guess what day it is!? it's happy FRIDAY ! !
message5 = ['python','ruby','javascript']
print(" ".join(message4)) # guess what day it is!? it's happy FRIDAY ! !
print(" ".join(message5)) # python ruby javascript

#you can join with dashes e.g.
print("-".join(message4)) # will print guess-what-day-it-is!?-it's-happy-FRIDAY-!-!

'''
'''

# import string
print(string.ascii_lowercase)

# import strings imports  all of the constants, so if you just wanted the ascii_lowercase, you would replace `import strings` with `from string import ascii_lowercase` and you don't have to reference the string. in `print(string.ascii_lowercase)`` it would just be `print(ascii_lowercase)`

