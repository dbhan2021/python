# Title: 
# Version: 1.0
# Date: Mar 5 2022

# Author: Diya Bhan
# Course: Computer Science ICS2O
# School: Ashbury College, Ottawa
# Teacher: Mr. Giansante

# Description: Quiz game
print("""  _    _  ____  __    ___  _____  __  __  ____    ____  _____    _____  __  __  ____  ____     ___    __    __  __  ____ 
( \/\/ )( ___)(  )  / __)(  _  )(  \/  )( ___)  (_  _)(  _  )  (  _  )(  )(  )(_  _)(_   )   / __)  /__\  (  \/  )( ___)
 )    (  )__)  )(__( (__  )(_)(  )    (  )__)     )(   )(_)(    )(_)(  )(__)(  _)(_  / /_   ( (_-. /(__)\  )    (  )__) 
(__/\__)(____)(____)\___)(_____)(_/\/\_)(____)   (__) (_____)  (___/\\(______)(____)(____)   \___/(__)(__)(_/\/\_)(____)
                                                                                                                                                                                                                                
                                                                                          `---`                      ---`-'                         `---`     `--`---'                    `----'   
   """)                                                                                                                                                                                                                             



score = 0


print("""
Question one: Who was the first man on the moon?

(1) Abraham Lincoln

(2) Nick Jonas

(3) Neil Armstrong

(4) Bobby Green

""")


choice = (input("Answer: "))
answerone= "3"
    



try:
     if choice == answerone:
          print("""◃───────────▹
   Correct
◃───────────▹
""")
     score = score + 1
except ValueError:
    print("Not a valid answer please try again.")
else:
         print("""================================================================
 Sorry you are incorrect the right answer is ' Neil Armstrong'
================================================================'""")


    
print("""Question two: Brazil is the biggest producer of?

(1) Wheat

(2) Rice

(3) Oil

(4) Coffee

""")


choice = (input("Answer: "))
answertwo= "4"
if choice == answertwo:
     print("""◃───────────▹
   Correct
◃───────────▹
""")
     score = score + 1
else:
         print("""================================================================
 Sorry you are incorrect the right answer is 'Coffee'
================================================================""")

print("""Question three: Who is the richest person alive?

(1) Jeff Bezos

(2) Elon Musk

(3) Bill Gates

(4) Maddona

""")


choice = (input("Answer: "))
answerthree= "2"
if choice == answerthree:
     print("""◃───────────▹
   Correct
◃───────────▹""")
     score = score + 1
else:
     print("""================================================================
Sorry you are incorrect the right answer is 'Elon Musk'
================================================================""")


print("""Question four: Which one of these characters is not friends with Harry Potter?

(1) Ron Weasley

(2) Neville Longbottom

(3) Draco Malfoy

(4) Hermione Granger

""")


choice = (input("Answer: "))
answerfour= "3"
if choice == answerfour:
     print("""◃───────────▹
   Correct
◃───────────▹
""")
     score = score + 1
else:
     print("""================================================================
Sorry you are incorrect the right answer is 'Draco Malfoy'
================================================================""")


print("""Question five: What is the biggest country in the world?

(1) Canada

(2) USA

(3) Brazil

(4) Russia

""")


choice = (input("Answer: "))


answerfive= "4"

    
if choice == answerfive:
     print("""◃───────────▹
   Correct
◃───────────▹▹""")
     score = score + 1
else:
     print("""================================================================
⃛Sorry you are incorrect the right answer is 'Russia'
================================================================""")



print("Your score is " + str(score) + " out of 5")
print("Thanks for playing 'Quiz Game'Goodbye")

