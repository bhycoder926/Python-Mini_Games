rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random 
user_choice = int(input("What do you choose? Type 0 for Rock , 1 for Paper , 2 for Scissors.\n"))
symbols = [rock,paper,scissors]
computer_choice = random.randint(0,2)
if user_choice > 2 or user_choice < 0 :
    print("You entered an invalid number.")
else :
    print(f"You chose : \n {symbols[user_choice]}")
    print(f"Computer chose : \n {symbols[computer_choice]}")
    if user_choice == computer_choice :
        print("It's a Draw.")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You Win!")
    else :
        print("You Lose!")