class Person:
  def __init__(self):
    print("Welcome")
  
  def fname(self,firstName=''):
    print(f"Welcome to Evolve Mr.{firstName}.")
  
  def fullname(self,firstName='',lastName=''):
    print(f"Welcome {firstName} {lastName}")


p1=Person()
p1.fname('Ramesh')
p1.fullname('Ramesh','Rawat')

# define method overriding


