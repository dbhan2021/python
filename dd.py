
score = 0
score = int(score)


print("""Question one: Who was the first man on the moon?
(1)Abraham Lincoln 
(2)Nick Jonas
(3)Neil Armstrong
(4)Bobby Green""")


choice = int(input("Answer: "))
answer1= "3"
if choice == answer1:
     print("Correct, here have a point")
else:
     print("sorry you are incorrect the right asnwer is 'Neil Armstrong'")






#Question2
print("""What is the Maori term for ‘tribe’ or ‘mob’?
1. Mihi 
2. Iwi 
3. Awi 
4. Hapu""")

answer2 = "2"
response2 = input("Your answer is:")

if (response2 != answer2):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response2 + " is correct!")
    score = score + 1

#Question3
print("""What is the term for the formal welcome, where two individuals press their nose together?
1. Hongi 
2. Haka 
3. Hangi 
4. Huka""")

answer3 = "1"
response3 = input("Your answer is:")

if (response3 != answer3):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response3 + " is correct!")
    score = score + 1



#Question4
print("""Who is the ‘demi-god’ or the ‘great creator’ who fished NZ out from the sea?
1. Zeus
2. Hercules
3. Maui
4. Maori""")

answer4 = "3"
response4 = input("Your answer is:")

if (response4 != answer4):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response4 + " is correct!")
    score = score + 1



#Question5
print("""What is the name for the traditional Maori method of cooking?
1. Roast
2. Hangi
3. Hongi
4. Bake""")

answer5 = "2"
response5 = input("Your answer is:")

if (response5 != answer5):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response5 + " is correct!")
    score = score + 1

print("Your score is " + str(score) + " out of 5")
print("Thanks for playing!")
