# Use ASCII Art
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

print("Welcome to Treasure Island!")

print("Your mission is to find the treasure.")

choice1 = input('In-front of you are 2 roads, you can only pick one.\n'
                'Which one would you like to pick?\n'
                'Type \'left\' or \'right\'.\n').lower()

if choice1 == 'left':
    choice2 = input('You have now arrived at a mysterious lake.\n'
                    'You can see an Island from afar.\n'
                    'Type \'swim\' to swim across. Type \'wait\' to wait for a boat.\n').lower()
    if choice2 == 'wait':
        choice3 = input('You have arrived safely at the Island.\n'
                        'In-front of you is a gigantic castle with 3 doors.\n'
                        'Each door has a unique color.\n'
                        'Type \'red\' to enter the Red door. Type \'blue\' to enter the Blue door. '
                        'Type \'yellow\' to enter the Yellow.\n').lower()
        if choice3 == 'yellow':
            print('Congratulations! You have found the Treasure and won the game.')
        elif choice3 == 'red':
            print('The room is full of fire and you have been burned. Game Over.')
        elif choice3 == 'blue':
            print('The room is full of deadly Gas and you have been poisoned. Game Over.')
        else:
            print('Game Over.')
    else:
        print('You have been eaten by a Shark. Game Over.')
else:
    print('You have been attacked by a bunch of Monsters. Game Over.')
