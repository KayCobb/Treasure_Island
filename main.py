#https://ascii.co.uk/art
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

go = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()
if go == "right":
  print('You\'ve come to a lake. There is an island in the middle of the lake.')
  wait_or_swim = input('Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
  if wait_or_swim == "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
    colour = input("Which colour do you choose?\n").lower()
    if colour == "red":
      print("You found the treasure! You Win!")
    elif colour == "yellow":
      print("It's a room full of fire. Game Over.")
    elif colour == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  elif wait_or_swim == "swim":
    print("You get attacked by an angry trout. Game Over.")
  else:
    print("You drowned. Game Over.")
elif go == "left":
  print("You fell into a hole. Game Over.")
else:
  print("You lost your way and never found it. Game Over.")
