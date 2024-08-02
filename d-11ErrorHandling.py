# Error Handling
# types:
# try:  test the block of codes
# expect:   handle the error
# else:   if error not found else is done
# finally:    it executes wheather there is error or not

# Types of Error
# KeyError
# TabError
# NameError
# IndexError
# etc.....


# Example

# try:
#   print('x')
# except NameError:
#   print('something went wrong')
# else:
#   print('No error found')
# finally:
#   print('finally')


# arguments
# *args and **kwargs
# 
# def numbers(*args):
#   print(args)
#   print(type(args))
#   for i in args:
#     print(i)
#   print(type(i))
# numbers(1,2,3,4,5)


# def add(*args):
#     return sum(args)
# res=add(1,2)
# print(res)


def adds(*args):
  sum=0
  for i in args:
    sum+=i
  print(sum)     
adds(1,2)


# **kwargs  (keyword arguments)

# def showFunction(**kwargs):
#   # if 'fruits' in kwargs:
#   #   print(f"My favourite fruits is {kwargs['fruits']}")
#   # print(type(kwargs))
#   for key,value in kwargs.items():
#     print(f"{key} : {value}")
#     print(type(f"{key} : {value}"))
# showFunction(fruits="apple",vegitable="patato")

