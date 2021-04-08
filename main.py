print('''
              ,
          _,-""-._
        ,"        ".
       /    ,-,  ,"\
      "    /   \ | o|
      \    `-o-"  `-',
       `,   _.--'`'--`
         `--`---'                    |   _)
           ,' '      _  /  _ \  ` \   _ \ |  -_)
         ./ ,  `,    ___|\___/_|_|_|_.__/_|\___|
         / /     \
        (_)))_ _,"
           _))))_,
  --------(_,-._)))-------------------------------
''')


print("Welcome to COVID-19 Zombie Apocalypse\n")
print('Your mission is to find the vaccine\n')

print("Each decision you make will be consequential. Choose Wisely!\n")

print("COVID-19 has turned every deceased patient into the living-dead. You are stuck in a path and need to choose where to go. Going BACK, will take you back where you came from, going FORWARD, will require traversing through the cemetery.\n")

BvF = input("Which one will it be, BACK or FORWARD?\n").lower()

if BvF == 'forward':
  DvH = input('You\'ve come across much of the living dead, but your post-apocalptic training kicked in and you have made it past the cemetery. To your surprise, you have to make another important decision. The road splits off into two different cities, HOUSTON and DALLAS. You are not sure which road to take, but know that DALLAS is the bigger city. Which city do you travel to, DALLAS or HOUSTON\n').lower()

  if DvH == 'dallas':

    lol = input("Congratulations, you\'ve made it to Dallas. Once in Dallas, you immideatly are faced with one of three choices. Go to the CDC, visit a local HOSPITAL, or SCAVANGE for food and suppplies. Your main task is to find a vaccine for your family. Which path will you take, CDC, HOSPITAL, or SCAVANGE\n").lower()

    if lol == 'scavange':
      print('You chose to scavange. You found food, supplies and to your surprise, a dozen vaccines, perfectly incubated and ready to administered for the next 12 days. You take the vaccines, and give them to your family. Congratulations, you have survied the COVID-19 zombie apocalypse!\n')

    else:
      print('On your way into the city, you were attacked by local citizens attempting to scare outsiders away. You were captured, and subseqently eated. You are dead. Game Over!\n')

  else:
    print("You traveled to Houston, and along the way came across a swarm of zombies. You tried to fight them off to no avail. You are dead. Game over!\n")
else:
  print("You came across other post-apocalptic survivors. They shot you dead. Game over!")