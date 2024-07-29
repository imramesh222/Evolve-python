# x=100
# for i in range (1,x+1):
#   if (i%10==0):
#     print(i,end='\n')
#   else:
#     print(i,end=' ')
  

# for i in range(1,100,10):
#   for j in range(i,i+10):
#     print(j,end=' ')
#     j+=10
#   print()

# x=int(input("Enter any number"))
# fact=1
# for i in range (1,x+1):
#  fact *=i
# print(fact,end=' ')

# x=int(input("Enter any number : "))
# for i in range(1,x):
#   if(x%i==0):
#     print("Not prime")
#     break
#   else:
#     print("prime")
#     break
#   print()

num=int(input("Enter any number : "))
flag=False

if num==1:
  print("Prime")
elif(num>1):
  for i in range(2,num):
    flag=True
    break
  if flag:
    print(num, "is not a prime number")
  else:
    print(num,"is a prime number")