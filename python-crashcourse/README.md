# Notes

You can run an interactive python shell in your terminal by typing in the command `python`, `ctrl+D` allows you to quit

---

## Slicing

![](assets/slicing.jpg)

`name = "INTERSTELLAR"`

```
name = I N T E R S T E L  L A  R
       0 1 2 3 4 5 6 7 8  9 10 11
                      -4 -3 -2 -1
```
`print(name[0:5])` would print `INTER`

we have to include 5 because by default the first index will not be included

if we wanted STELLAR instead, S starts at 5, so we'll start with 5 as the start value

`print(name[5:])` would print out `STELLAR`

name[5:] 
+1 towards the end of the string doesn't exist, so we can leave the stop slot empty


![](assets/slicing1.jpg)

![](assets/slicing2.jpg)

step size is one by default

![](assets/slicing3.jpg)

---

## String Functions 
[Link to read more]('https://docs.python.org/3/library/functions.html')

- len()

will also count white spaces, e.g.

greeting = "hello"
user="jr"
message="happy friday"
age=20

`print(len(greeting)) //prints 5`
`print(len(message)) //prints 12`

- type()

type will tell you the type

`print(type(age)) //prints int`
`print(type(user)) //prints str`

- id()


~
- capitalize()
you have to include dots when using capitalize, e.g.

greeting = "hello"
user="jr"
message="happy friday"
age=20

`print(greeting.capitalize(), message.capitalize()) //prints "Hello", "Happy friday"`


- upper()
will capitalize your entire string

greeting = "hello"
user="jr"
message="happy FRIDAY"

`print(user.upper())`
prints JR
`print(message.upper())`
prints HAPPY FRIDAY

- lower()
will lowercase your entire string

greeting = "hello"
user="jr"
message="happy FRIDAY"

`print(user.lower())`
prints jr
`print(message.lower())`
prints happy friday


- strip()
removes whitespaces from characters before and after a string, e.g.
```
message1="       happy FRIDAY       "
```

`print(message1) # prints "       happy FRIDAY       "`
`print(message1.strip()) # prints happy FRIDAY`

![](assets/strip.jpg)

- find()


~

- split()


- join()

** You can tell a function vs method by functions being written first like the above as examples

** methods are tied to the objects themselves

** you can have python display all of the built string objects by `print(dir(varname))` e.g. `print(dir(user))`
![](assets/stringfunctions.jpg)

** method chaining, is you can chain methods onto one another e.g.

```
message1="       happy FRIDAY       "
```

`print(message1.strip().lower()) # prints happy friday`
~

- import string