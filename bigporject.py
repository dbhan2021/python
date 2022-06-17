print(
    """  _    _  ____  __    ___  _____  __  __  ____    ____  _____    _____  __  __  ____  ____     ___    __    __  __  ____
( \/\/ )( ___)(  )  / __)(  _  )(  \/  )( ___)  (_  _)(  _  )  (  _  )(  )(  )(_  _)(_   )   / __)  /__\  (  \/  )( ___)
 )    (  )__)  )(__( (__  )(_)(  )    (  )__)     )(   )(_)(    )(_)(  )(__)(  _)(_  / /_   ( (_-. /(__)\  )    (  )__)
(__/\__)(____)(____)\___)(_____)(_/\/\_)(____)   (__) (_____)  (___/\\(______)(____)(____)   \___/(__)(__)(_/\/\_)(____)

                                                                                                                       
   """
)
money = 0
print(
    """
Question one: Who was the first man on the moon?

(1) Abraham Lincoln

(2) Nick Jonas

(3) Neil Armstrong

(4) Bobby Green

"""
)
answer = 3

choice = int(input("Answer: "))
while choice < 1 or choice > 4:
    print("invalid value please try again")
    choice = int(input("Answer: "))

if choice == answer:

    print(
        """◃───────────▹
   Correct
◃───────────▹
"""
    )
    score = score + 1
else:
    print(
        """================================================================
 Sorry you are incorrect the right answer is ' Neil Armstrong'
================================================================'"""
    )


print(
    """Question two: Brazil is the biggest producer of?

(1) Wheat

(2) Rice

(3) Oil

(4) Coffee

"""
)

answer=4

choice = int(input("Answer: "))
while choice < 1 or choice > 4:
    print("invalid value please try again")
    choice = int(input("Answer: "))

if choice == answer:
    print(
        """◃───────────▹
   Correct
◃───────────▹
"""
    )
    score = score + 1
else:
    print(
        """================================================================
 Sorry you are incorrect the right answer is 'Coffee'
================================================================"""
    )

print(
    """Question three: Who is the richest person alive?

(1) Jeff Bezos

(2) Elon Musk

(3) Bill Gates

(4) Maddona

"""
)


answer = 2

choice = int(input("Answer: "))
while choice < 1 or choice > 4:
    print("invalid value please try again")
    choice = int(input("Answer: "))



if choice == answer:
    print(
        """◃───────────▹
   Correct
◃───────────▹"""
    )
    score = score + 1
else:
    print(
        """================================================================
Sorry you are incorrect the right answer is 'Elon Musk'
================================================================"""
    )


print(
    """Question four: Which one of these characters is not friends with Harry Potter?

(1) Ron Weasley

(2) Neville Longbottom

(3) Draco Malfoy

(4) Hermione Granger

"""
)

answer=3


choice = int(input("Answer: "))
while choice < 1 or choice > 4:
    print("invalid value please try again")
    choice = int(input("Answer: "))
   

if choice == answer:
    print(
        """◃───────────▹
   Correct
◃───────────▹
"""
    )
    score = score + 1
else:
    print(
        """================================================================
Sorry you are incorrect the right answer is 'Draco Malfoy'
================================================================"""
    )


print(
    """Question five: What is the biggest country in the world?

(1) Canada

(2) USA

(3) Brazil

(4) Russia

"""
)


choice = int(input("Answer: "))
while choice < 1 or choice > 4:
    print("invalid value please try again")
    choice = int(input("Answer: "))
   



answer = 4

if choice < 1 or choice > 5:

    print("invalid value please try again")

if choice == answer:
    print(
        """◃───────────▹
   Correct
◃───────────▹▹"""
    )
    score = score + 1
else:
    print(
        """================================================================
⃛Sorry you are incorrect the right answer is 'Russia'
================================================================"""
    )


print("Your score is " + str(score) + " out of 5")
print("Thanks for playing 'Quiz Game'  Goodbye")

