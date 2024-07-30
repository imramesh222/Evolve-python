import random
import random

rock="rock"
paper="paper"
scissors="scissor"

user_choice=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors\n"))
if user_choice == 0:
    user_choice = rock
    print(f"You chose {user_choice}")
elif user_choice == 1:
    user_choice = paper
    print(f"You chose {user_choice}")
elif user_choice == 2:
    user_choice = scissors
    print(f"You chose {user_choice}")
else:
    print("You typed incorrectly.\nTry again later")
    exit()

computer_choice=random.randint(0,2)

if computer_choice == 0:
    computer_choice = rock
    print(f"Computer chooses {computer_choice}")
elif computer_choice == 1:
    computer_choice = paper
    print(f"Computer chooses {computer_choice}")
else:
    computer_choice = scissors
    print(f"Computer chooses {computer_choice}")


if user_choice == rock and computer_choice == scissors:
    print("You win!")
elif user_choice == paper and computer_choice == rock:
    print("You win!")
elif user_choice == scissors and computer_choice == paper:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a tie!")
else:
    print("Computer wins!")





















# player_choice=''

# while player_choice=='rock' or player_choice=='sciccor' or player_choice=='papper':
#   player_choice=input("Enter your choice")
#   computer_choice=random(options)

#   if(player_choice=='rock' and computer_choice=='papper'):
#     if(player_choice=='papper' and computer_choice=='scissor'):
#       if(player_choice=='scissor' and computer_choice=='rock'):
#         print("You loose")
#   elif(player_choice=='papper' and computer_choice=='rock'):
#     print("You win")
#   elif(player_choice=='rock' and computer_choice=='scissor'):
#     print("You win")
#   elif(player_choice=='scissor' and computer_choice=='papper'):
#     print("You win")
#   elif(player_choice=='scissor' and computer_choice=='scissor'):
#     if(player_choice=='papper' and computer_choice=='papper'):
#       if(player_choice=='rock' and computer_choice=='rock'):
#         print("Match drawn")






