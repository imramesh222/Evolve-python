# num = int(input("Enter a number: "))

# if num == 0:
#     print("Zero")
# elif num % 2 == 0:
#     print(f'{num} is Even')
# else:
#     print("Odd")

price = float(input("Enter a number: "))
sp=price
dis=0
if(price>500):
  sp-=(20*price)/100
  dis=price-sp
elif(price>200 and price<500):
  sp-=(10*price)/100
  dis=price-sp
else:
  sp=price
  dis=0

print(f'sp is {sp}')
print(f'discount is {dis}')
