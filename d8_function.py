# predefined functions

import math
import random

# print(math.ceil(20.456))
# print(math.floor(30.999))
# print(math.sqrt(22))
# print(math.pow(2,5))
# from random import shuffle,random,choice,randint

# list=[1,2,3,4,5,6,7]
# print(list)
# shuffle(list)
# print(list)

# print(random())
# print(math.floor(100000+random()*899999))


# print(random.randint(1,10))

# function is a block of codes that perform specific task
# function can be reused in program
# function name must be ended by paranthesis()
# while naming function we can not  use python keywords or variable name,we should avoid space,special characters expect underscore_
# function name must be started with alphebets or underscore followed by numbers,alphabets,underscere

# syntax
# def functionName()
    # ...task...
# functionName()

# defining function
def showName():
  myname='Karan'
  print(f"My name is {myname}")
# calling the function
showName()

# function with arguments
def showName(name):
  print(name)

showName('Rahul')

# function with return type

def showName(ramukaka):
  return ramukaka
result=showName('lucky')
print(result)

# add two numbers using function with arguments
def addNumbers(n1,n2):
  return n1+n2
sum=addNumbers(2,3)#arguments
print(sum)