# Slicing Notation

'''
name = I N T E R S T E L  L A  R
       0 1 2 3 4 5 6 7 8  9 10 11
                      -4 -3 -2 -1

if we wanted INTER, how would we go about it?

name[0:5]

we have to include 5 because by default the first index will not be included

if we wanted STELLAR instead, S starts at 5, so we'll start with 5 as the start value

name[5:]
+1 towards the end of the string doesn't exist, so we can leave the stop slot empty


'''

name = "INTERSTELLAR"
print(name[0:5])
print(name[5:])
print(name[:5]) #start slot can be left open



# you can provide a 3rd argument which will be for the step size [ : : ]



social_media = "twitter"
'''

T W I T T E R
0 1 2 3 4 5 6

'''

print(social_media[0:4]) # stop plus 1
print(social_media[4:]) # to print out ter
print(social_media[1:4]) # to print out wit
print(social_media[:7]) # will print out twitter since there's six indexes
print(social_media[:]) # if you leave the start and stop empty, it'll give you the whole string
print(social_media[::2]) #3rd argument is called step size
print(social_media[::1]) # step size is 1 by default
print(social_media[::-1]) # would work in reverse, starting with the last element


thought_of_the_day = "If programmers write programs, who writes programmers?"
print(thought_of_the_day[21:29])