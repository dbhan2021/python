#Diya Bhan
#Feb 2022
#Guessing game
#Teacher: Mr. Giansante
print("Welcome to Number Guessing Game!")
#getting random
import random
#finding random value
number = random.randint(1, 100)
#creating variable
guess=0


while number!=guess:
    guess = int(input("Please enter any number from 1-100:"))
    if(guess <1 or guess >100):
        print("Out of Range")
    else:
        if guess < number:
            print('Your guess is too low.')

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            print("Good job you win")
            break
        




