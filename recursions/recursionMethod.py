
'''
def recursionMethod(parameters):
    if exit from condition satisfied:
      return some value
    else: 
      recursionMethod(modified parameters)
'''

# deeper dive into how recursion works
# '''
def firstMethod():
    secondMethod()
    print("I am the first method")

def secondMethod():
    thirdMethod()
    print("I am the second method")

def thirdMethod():
    fourthMethod()
    print("I am the third method")

def fourthMethod():
    print("I am the fourth method")
# '''

# '''
def recursiveMethod(n):
    if n<1:
        print("n is less than 1")
    else:
      recursiveMethod(n-1)
      print(n)
# '''