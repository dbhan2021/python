
print=(""" ____   ____       __                                   _ _______                        ________                             ______         _                                  
|_  _|    |_  _|  [  |                                 / |_        |_   __ \              [  |  _   |_   __ \                           .' ____ \       (_)                                 
  \ \  /\  / .---. | | .---.  .--.  _ .--..--. .---.  `| |-'.--.     | |__) |  .--.  .---. | | / ]    | |__) ,--. _ .--.  .---. _ .--.  | (___ \_|.---. __  .--.  .--.  .--.  _ .--. .--.   
   \ \/  \/ / /__\\| |/ /'`\/ .'`\ [ `.-. .-. / /__\\  | |/ .'`\ \   |  __ / / .'`\ / /'`\]| '' <     |  ___`'_\ [ '/'`\ / /__\[ `/'`\]  _.____`./ /'`\[  |( (`\]( (`\/ .'`\ [ `/'`\( (`\]  
    \  /\  /| \__.,| || \__.| \__. || | | | | | \__.,  | || \__. |  _| |  \ \| \__. | \__. | |`\ \   _| |_  // | || \__/ | \__.,| |     | \____) | \__. | | `'.'. `'.'| \__. || |    `'.'.  
     \/  \/  '.__.[___'.___.''.__.'[___||__||__'.__.'  \__/'.__.'  |____| |___'.__.''.___.[__|  \_] |_____| \'-;__| ;.__/ '.__.[___]     \______.'.___.[___[\__) [\__) '.__.'[___]  [\__) ) 
                                                                                                                 [__|                                                                       """)
choice = ""

import random


win = int(0)
lose = int(0)
tie = int(0)

mylist = ["R", "P", "S"]

comp_choice = random.choice(mylist)



choice=input("Please enter Rock[R] Paper[P] Scissor[S] or Quit[Q]:")



if choice== "R":
    if comp_choice=="R":
        print("I Tied")
        tie=tie+1

    elif comp_choice=="S":
        print("I won")
        lose=lose+1
    
    elif comp_choice=="P":
        print("I lost")
        lose=lose+1
    
