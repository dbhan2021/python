
print(""" ____   ____       __                                   _ _______                        ________                             ______         _                                  
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



while choice != "r" or choice!="R" or choice!="S" or choice!="s" or choice!="P" or choice!="p" or choice!="Q" or choice!="q":

        print("that is not a valid value please try again")
        choice=input("Please enter Rock[R] Paper[P] Scissor[S] or Quit[Q]:")


else:

        print(" ")


if choice == "R" or choice == "r":

        print("Your choice is:rock")


if choice == "S" or choice == "s":

        print("Your choice is:scissors")

if choice == "P" or choice == "p":

        print("Your choice is:paper")




if choice == "R" or choice == "r" and comp_choice == "P":
        print("The computer chose: Paper")
      
        print("You Lose!")

        lose = lose + 1
  
elif choice == "R" or choice == "r" and comp_choice == "S":
        print("The computer chose: Scissors")

        print("You Win!!")
    
        win = win + 1



elif choice == comp_choice:

        print("tie!!")

        tie = tie + 1
      

elif choice == "R" or choice == "r" and comp_choice == "P":
        print("The computer chose: Paper")
      
        print("You Lose!")

        lose = lose + 1
  
elif choice == "R" or choice == "r" and comp_choice == "S":
    print("The computer chose: Scissors")

    print("You Win!!")

    win = win + 1
    

elif choice == "P" or choice == "p" and comp_choice == "S":
    print("The computer chose: paper")
    print("You Lose!!")

    lose = lose + 1
    
   
elif choice == "P" or choice == "p" and comp_choice == "R":
    print("The computer chose: Rock")

    print("You Win!!")

    win = win + 1


elif choice == "S" or choice == "s" and comp_choice == "R":
    print("The computer chose: Rock")

    lose = lose + 1
   
    print("You Lose!!")


elif choice == "S" or choice == "s" and comp_choice == "P":
    print("The computer chose: Paper")
  
    print("You Win!!")
 
    win = win + 1
 
while choice=="q" or choice=="Q":
    print("goodbye")
    break
    



