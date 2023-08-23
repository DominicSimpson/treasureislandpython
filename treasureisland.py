print('''
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Write your code below this line 👇
choice = input(
    "You are at a crossroads. Where do you want to go? Type 'Left' or 'Right'."
).lower()

if choice == "left":
    swimorwait = input(
        "You have come to a lake. There is an island in the middle of the lake. Type 'Wait' to wait for a boat. Type 'Swim' to swim across."
    ).lower()

    if swimorwait == "wait":
        whichdoor = input(
            "You got the boat and arrive at the island unharmed. There is a house with three doors. One red, one yellow, and one blue. Which color do you choose?"
        ).lower()

        if whichdoor == "red":
            print("It's a room full of fire. Game Over")
        elif whichdoor == "yellow":
            print("You found the treasure map! Now let's find the treasure!")

            row1 = ["⬜️", "⬜️", "⬜️"]
            row2 = ["⬜️", "⬜️", "⬜️"]
            row3 = ["⬜️", "⬜️", "⬜️"]
            treasure_map = [row1, row2, row3]
            print(f"{row1}\n{row2}\n{row3}")

            position = input("Where do you want to put the treasure? Enter two digits ")

            horizontal_row = int(position[0])
            vertical_column = int(position[1])

            treasure_map[vertical_column - 1][horizontal_row - 1] = "X"

            print("Congratulations! You have placed the treasure on the map:")
            print(f"{row1}\n{row2}\n{row3}")
            print("You found the treasure and won the game! Ooh aar, me hearties! Congratulations!!")

        elif whichdoor == "blue":
            print("You enter a room full of poisonous beasts. Game Over")
        else:
            print(
                "You chose a door that doesn't exist and spontaneously combust. Game Over."
            )

    else:
        print(
            "You got attacked by an angry trout and equally angry shark. Game Over."
        )

else:
    print("You fell into a hole. Oh well. Game Over.")
