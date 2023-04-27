# Installing python 3X installs something called a python Launcher which avoids using the PATH
# it finds it for you so no need to add python to the path. c:\windows\py.exe
# You can use VSCode to write python.  Install python for windows extension and its linter
# You can run code by right clicking and select run Python file in terminal.  To allow this, you have to set
# python interpreter.  ctrl+shift+p, then type python:select interpreter, select the interpreter location from dropdown
# To debug, open debug window and select python: current file.  To the left of the name is a green arrow.  Press it to run

# Modules
# Say you have a file named fibo.py with 2 functions, fib and fib2.  You can import them saying
# import fibo
# then use them like fibo.fib()
# also you can import them like this
# from fibo import fib, fib 2
# then use them like fib()
# you can also import all methods like this
# from fibo import *

import re


def MyFunc():
    print("basic function")
    return 2


mf = MyFunc
mf()  # also returns 2

MyFunc()
a = 1
b = 2
c = a+b

# multiple assignment
a, b = 1, 2  # a=0, b=1
c, d = a, a+b
print(str(c) + " " + str(d))

e = 42
if e < 42:
    e = 4
elif e == 43:
    e = 5
else:
    pass


# strings
# concat strings
print('he' 'llo')
print("he" "llo2")

concat1 = "by"
concat2 = "ee"
print(concat1 + "yy")
print(concat1 + concat2)

# substring
substringVar = "fluent"
print("substring: " + substringVar[0:2])  # f1
print("substring: " + substringVar[:2])  # f1
print("substring: " + substringVar[2:4])  # ue
print("substring: " + substringVar[2:])  # uent
print("substring: " + substringVar[-3:-1])  # en
print("substring: " + substringVar[-3:])  # ent

# lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# strings are immutable but list are not so we can change them at a certain position

letters[2:5] = ['C', 'D', 'E']  # ['a', 'b', 'C', 'D', 'E', 'f', 'g']
letters[2:5] = []  # ['a', 'b', 'f', 'g']
letters[:] = []  # clears the list
len(letters)  # shows count

# add
letters.append('w')
letters.insert(2, 'x')
letters.remove('w')
letters.pop()  # removes last item
letters.pop(1)  # removes 2nd item
del letters[0]
letters.clear()  # empties list but it remains
del letters


# List comprehension
# create a new list based on the values of an existing list.
# Syntax: newlist = [expression for item in iterable if condition == True]

newLetters = []
for x in letters:
    if "a" in x:
        newLetters.append(x)
print(newLetters)

# list comprehension version
newLettersLC = [x for x in letters if "a" in x]
newLettersLC2 = [x for x in letters if x != "b"]
newLettersLC3 = [x for x in letters]  # without condition

# loop
for x in letters:
    print(x)

# range() returns a sequence of numbers, starting from 0
for i in range(len(letters)):
    print(letters[i])

# if you want to modify a list while iterating, make copy using slice and iterate the copy
listCopy = ['cat', 'window', 'defenestrate']
for item in listCopy[:]:
    if (len(item) > 6):
        listCopy.insert(0, item)

print(listCopy)  # ['defenestrate', 'cat', 'window', 'defenestrate']

# Dictionary
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(list(tel.keys()))

for k, v in tel.items():
    print(k, v)

# Reading and writing Files

fh = open('data.csv', 'r')


# regex
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


class MyClass:
    """
    My Test Class
    """

    # This gets shared by all instances.  Instead, put inside __init__(self)
    sampleArr = ["initialValue"]

    def addToClassLevelArr(self, item):
        self.sampleArr.append(item)

    def __init__(self):
        """
        All member variables in python are public.  
        Convention for private is to prefix with double underscore
        """
        # sampleArr = ["initialValue"]
        self.data = []
        self.var1 = 1
        self.__privateVar = 2

    def func(self):
        """ 
        Comment Line 1
        Comment Line 2
        """
        print("Test::func")

    def Loops(self):
        i = 0
        while (i < 3):
            self.data.append(i)
            i += 1

        print(self.data)

        localData = ["a", "b", "c", "d"]
        for item in localData:
            print(item)
            if item == "c":
                break  # breaks out of loop
                # continue   #skips rest of statement in this loop block and goes to next iteration
            print("bottom of loop")


# issue to watch out for.  Class level array shared with all instances
sampleArr1 = MyClass()
sampleArr2 = MyClass()
sampleArr1.addToClassLevelArr("new Item")
print(sampleArr1.sampleArr)  # ['initialValue', 'new Item']
print(sampleArr2.sampleArr)  # ['initialValue', 'new Item']

x = MyClass()
x.func()
print(x.var1)
x.Loops()
