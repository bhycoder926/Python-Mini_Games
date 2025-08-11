import random
computer_choice = random.randint(1,10)
while True:
    user_choice = int(input("Enter a number between 1 and 10 : \n"))
    if(user_choice < 1 or  user_choice > 10):
        print("Invalid number , please enter a number between the given range.")
    elif user_choice == computer_choice:
        print("Congrats! ,  You were right.")
    elif user_choice < computer_choice :
        print("Too Low!")
    else:
        print("Too High!")