print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("🌊🌴  Welcome to Treasure Island.")
print("💪  Your task is to find the Treasure in this Island.")

choice_1 = input('🛣️  You\'re at a crossroad , type "left" or "right" to choose a path you want to continue : \n').lower()

if choice_1 == "right":
    choice_2 = input("You've reached the bank of the river , type \"swim\" to swim across the river or \"wait\" for some magic:\n").lower()
    
    if choice_2 == "wait":
        choice_3 = input('You are almost at the end of the game,now type "door1" or "door2" or "door3" to choose any one door among the three:\n').lower()
        if choice_3 == "door2":
            print("🎉  Congratulations , You have found the Treasure ,You won the game 👏🎊.")
        elif choice_3 == "door3":
            print("🦁  You are in the lion's den , You are finished 🤣 ,Good luck for your next life.")
        elif choice_3 == "door1":
            print("🏜️   You're in the middle of the Thar desert,try to walk south to save yourself 😑")
        else:
            print("🚪  You chose a door that does not exist.Sorry! 😢")
    else:
        print("🐊  You were attacked by a Crocodile while crossing the river. 😭")
else:
    print("🕳️  You fell in a hole.Sorry 😓")
