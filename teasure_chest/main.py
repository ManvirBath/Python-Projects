from turtle import left


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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("Welcome to Treasure Island!")
print("Your mission to find the treasure.")

flag = 0

while flag == 0:
    print("                     Treasure Island")
    print("------------------------------------------------------------")
    choice = input("Move left or right? ").lower()
    if choice == "left":
        choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
        if choice2 == "wait":
            choice3 = input("You arrived at the island unharmed. There is a house with three doors: red, yellow and blue. Which color do you choose? ").lower()
            if choice3 == "yellow":
                print("Congratulations, you win! You found the treasure!")
            elif choice3 == "red":
                print("You chose the wrong door and walked into a room full of fire. Game over.")
            elif choice3 == "blue":
                print("You fell into a pond filled with starving crocidiles. Game over.")
            else:
                print("That door does not exist. Game over.")
        else:
            print("You got attacked by an hungry lion. Game over.")
    else:
        print('You fell into a deep hole. Game over.')

    play_again = input("Do you want to continue? Y for Yes. N for No. ").lower()

    if play_again == 'y':
        flag == 0
    else:
        flag == 1
        break

print("Thanks for playing!")