# concatenation, indexing, slicing

message = "The price of the stock is:"
price = "$1100"

print(message + " " + price)

# to reassign
message1 = "The updated price of the stock is:"
price1 = "$1100"

new_message = message1 + " " + price1
print(new_message)


# id function, the results via print will be the memory location for the memory2 objects
message2 = "The price of the stock is:"
print(id(message2)) #since python runs from top to bottom,, this will execute for the first message2
price2 = "$1500"

message2 = message2 + " " + price2
print(id(message2)) #this will only get the id of the last message2 which was assigned


# indexing
'''
name = I N T E R S T E L  L A  R
       0 1 2 3 4 5 6 7 8  9 10 11
                      -4 -3 -2 -1

we can access the index using the square brackets e.g.

name[3] = E
name[0] = I
name[11] = R

***if you don't know the length of your string, you can use - negatives to access characters, e.g.
name[-1] = R
name[=5] = E
'''

name = 'INTERSTELLAR'
name[0]


