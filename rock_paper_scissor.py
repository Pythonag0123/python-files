import random

rock = '''
    _____
--'   ___)
     (___)
     (___)
     (___)
  ---(__)'''

scissors = '''
    _____
---'  ___)__
        ____)
     _______)
     (____)
---._(___)'''

paper = '''
    _____
---'  ___)__  
       _____)
     ________)
     _______)
---.______)     
      '''

total_choices = [rock, paper, scissors]

player_choice = input("Enter your choice:").lower().strip()
print(player_choice)
bot_choice = random.choice(total_choices)
print(bot_choice)

if player_choice == "rock" and bot_choice == paper:
    print("you lose")
elif player_choice == "paper" and bot_choice == scissors:
    print("you lose")
elif player_choice == "scissors" and bot_choice == rock:
    print("you lose")
elif player_choice == bot_choice:
    print("it's a draw")
else:
    print("you won")
