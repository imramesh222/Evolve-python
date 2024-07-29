pin=1234
amount=1000
# language=['english','neplai','exist']
# accountType=['saving','current']
# task=['withdraw','checkbalance']
print("Welcome To Evolve Bank of Nepal.")
lang=input("Choose Language : ")

if(lang=='english'):
  Your_pin=int(input("Enter your pin : "))
  if(Your_pin==pin):
    Your_task=input("Do you want to withdraw or check balance : ")
    if(Your_task=='checkbalance'):
      print(f'Your balance is Rs {amount}')
    elif(Your_task=='withdraw'):
      savingORcurrent=input("Choose your account type saving or current : ")
      if(savingORcurrent=='saving' or savingORcurrent=='current'):
        withdrawamount=int(input("Enter how much money do you want to withdraw : "))
        if(withdrawamount<=amount):
          amount-=withdrawamount
          print(f'Rs {withdrawamount} Withdrawl successfull .\nYour remaining amount is : Rs {amount}')
        else:
          print("Amount not availabe in your account")
      else:
        print("Invalid choice")
    else:
      print('Incorrect choice')
  else:
    print("Incorrect pin")

elif(lang=='nepali'):
  Your_pin=int(input("Enter your pin : "))
  if(Your_pin==pin):
    Your_task=input("Do you want to withdraw or check balance : ")
    if(Your_task=='checkbalance'):
      print(f'Your balance is Rs {amount}')
    elif(Your_task=='withdraw'):
      savingORcurrent=input("Choose your account type saving or current : ")
      if(savingORcurrent=='saving' or savingORcurrent=='current'):
        withdrawamount=int(input("Enter how much money do you want to withdraw : "))
        if(withdrawamount<=amount):
          amount-=withdrawamount
          print(f'Rs {withdrawamount} Withdrawl successfull .\nYour remaining amount is : Rs {amount}')
        else:
          print("Amount not availabe in your account")
      else:
        print("Invalid choice")
    else:
      print('Incorrect choice')
  else:
    print("Incorrect pin")
else:
  print('Terminated try again')



