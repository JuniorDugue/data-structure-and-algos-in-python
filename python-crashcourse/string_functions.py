
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

'''
'''

# Split()


# Join()

'''
'''





