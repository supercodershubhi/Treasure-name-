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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. Where do you want to go?")
cross_road = input('Type "left" or "right"').lower()

if cross_road == "left":
    print("You have come to a lake. There is an island in the middle of the lake.")
    swim_or_wait = input('Type "wait to wait for the boat. Type "swim" to swim across.').lower()

    if swim_or_wait == "wait":
        print("You\'ve arrived at the island unharmed. There is a house with 3 doors")
        choose_color = input("One red, one yellow and one blue. Which one will you choose?").lower()

        if choose_color == "yellow":
            print("You found the treasure. You win!")
        elif choose_color == "red":
            print("Burned by fire. Game over.")
        elif choose_color == "blue":
            print("Eaten by beasts. Game over")
        else:
            print("Game over.")

    else:
        print("Attacked by trout. Game over.")

else:
    print("You fell into a hole. Game over.")