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
step1 = input("You're at a cross road. Where do you want to go? "+'(type "left" or "right")')
step1 = step1.lower()

if step1 == "left":
  step2 = input("You see a lake that you need to cross and a small boat heading towards you. But it will take ages! Do you want to attempt swimming the distance and save some time or wait for the boat?"+'(type "swim" or "wait")')
  step2 = step2.lower()
  if step2 == "wait" :
    door = input("After crossing the lake you thank the captain of the boat and delve into a dungeon fighting for every inch with your life. Exhausted but alive you reach its deepest parts where 3 misterious doors await you. Which one will you choose? "+'(type "red", "blue" or "yellow")')
    door = door.lower()
    if door == "red":
      print("Opening the door sets the trap in motion and a fiery flame engulfes you until only charred bones are left. At least it was quick enough to only be incredible painful for a few seconds... GAME OVER")
    elif door == "blue":
      print("A swarm of beast that seemed to be sleeping inside the room behind the door awaken to its sound. Hungry and free, they jump into you fighting between themselves for the most savory parts. You didn't have much to say in that discussion because you were torn to pieces in seconds. It did hurt a lot before you died. GAME OVER")
    else:
      print("Behind the yellow door a dark lit room with a treasure chest lies. You open the chest finding riches beyond your imagination, and realize it surely weights a lot and dragging it across the miles of caves and mosters of the dungeon is going to be a pain in the a$$. But well, that's a problem for later. YOU WIN!")
  else:
    print ("A massive trout devours you mercilessly. Not even a shark, a trout. GAME OVER")
else:
  print ("An unexpected hole opens at your feet and pointy spikes at its bottom end with your miserable life. GAME OVER")
