# _init_ is automatically called function
class Student:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  pass

a=Student(name='Ramesh',age=23)

print(a.name)
print(type(a))

b=Student(name='Rawat',age=25)
print(b.age)

