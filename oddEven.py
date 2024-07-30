list=[1,2,3,4,5,6,7,8,9]
oddlist=[]
evenList=[]
for i in list:
  if i%2==0:
    evenList.append(i)
  else:
    oddlist.append(i)
print(oddlist)
print(evenList)
    