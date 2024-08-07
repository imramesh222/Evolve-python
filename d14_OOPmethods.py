import math

class Circle:
  pi=math.pi
  def __init__(self,radius=2):
    self.rad=radius
    self.area=self.pi*radius*radius
    
  
  def setRadius(self,newRadius):
    self.newrad=newRadius
    self.newarea=self.pi*newRadius*newRadius

  def setCircum(self,thirdRadius=2):
    self.thirdRad=thirdRadius
    self.circumference=2*self.pi*thirdRadius


c1=Circle()
print(c1.area)

c1.setRadius(2)
print(c1.newrad)
print(c1.newarea)

c2=Circle()
c2.setRadius(2)
print(c2.newarea)

c3=Circle()
c3.setCircum()
print(c3.circumference)

