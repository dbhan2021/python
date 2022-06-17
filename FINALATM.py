##ATM Program
CurrentClinet = 0
ClientName = list(range(11))
PIN = list(range(11))
Balance = list(range(11))

ClientName[1] = "John Smith"
PIN[1] = "1212"
Balance[1] = 20000.00

ClientName[2] = "Mary Jane"
PIN[2] = "5555"
Balance[2] = 100.00

ClientName[3] = "Josh Brooks"
PIN[3] = "2222"
Balance[3] = 40.00

ClientName[4] = "Casey White"
PIN[4] = "0000"
Balance[4] = 4000000.00

ClientName[5] = "Adam Stan"
PIN[5] = "1242"
Balance[5] = 2000.00

ClientName[6] = "Lily Green"
PIN[6] = "9090"
Balance[6] = 300000.00

ClientName[7] = "Brandy Kate"
PIN[7] = "1234"
Balance[7] = 1000000.00

ClientName[8] = "Sandy Bell"
PIN[8] = "6662"
Balance[8] = 9000.00

ClientName[9] = "Sasha Hill"
PIN[9] = "9494"
Balance[9] = 230000.00

ClientName[10] = "Nick Rich"
PIN[10] = "6000"
Balance[10] = 3030.00




while input != "q":
   print("""


░▒█░░▒█░█▀▀░█░░█▀▄░▄▀▀▄░█▀▄▀█░█▀▀░░░▀█▀░▄▀▀▄░░░█▀▀▄░█▀▀▄░█▀▀▄░█░▄░░░█▀▄▀█░█▀▀▄░█▀▄░█░░░░░▀░░█▀▀▄░█▀▀
░▒█▒█▒█░█▀▀░█░░█░░░█░░█░█░▀░█░█▀▀░░░░█░░█░░█░░░█▀▀▄░█▄▄█░█░▒█░█▀▄░░░█░▀░█░█▄▄█░█░░░█▀▀█░░█▀░█░▒█░█▀▀
░▒▀▄▀▄▀░▀▀▀░▀▀░▀▀▀░░▀▀░░▀░░▒▀░▀▀▀░░░░▀░░░▀▀░░░░▀▀▀▀░▀░░▀░▀░░▀░▀░▀░░░▀░░▒▀░▀░░▀░▀▀▀░▀░░▀░▀▀▀░▀░░▀░▀▀▀

""")
   valid_client = False
   name = input(
       "Please enter the first and last name associated with your account seperated by a space: ")
   # Check if Name is the cutomers
   for client_id in range(1, 10):
       # Compare the Name - case insensitive
       if name.casefold() == ClientName[client_id].casefold():
           valid_client = True
           break
   if valid_client == False:
       print(
           "Sorry, we don't seem to have an account under that name, please try again "
       )
       continue
   else:
       valid_pin = False
       for pin_attempts in range(3):
           code = input("Enter your 4 digit code associated with your account please: ")
           
           if code == PIN[client_id]:
               print("Valid Pin")
               valid_pin = True
               break
           else:
               valid_pin = False
               print("Invalid Pin")
   if valid_pin == False:
       print("You have entered an invalid pin 3 times, please try again try later")
       continue
   else:
       choice = ""
       while choice != "q":
           print("Welcome " + name)
           choice = str(
               input(
"""
┏━━━─────────────────────────────────────────━━━┓
|Press 1 to withdraw money                      | 
|───────────────────────────────────────────────|
|Press 2 to deposit money                       |       
|───────────────────────────────────────────────|
|Press 3 to check your balance                  |
|───────────────────────────────────────────────|
|Press 4 to change your pin code                |
|───────────────────────────────────────────────|
|Press q to exit                                |
┗━━━─────────────────────────────────────────━━━┛


"""


"choice:" )
           )
           if choice == "q":
               print("Bye " + name, " thank you for visiting our bank machine")
               break
           elif choice == "1":
               print("Client : " + name)
               withdraw_key = ""
               print("""
┏━━━─────────────────────────────────────────━━━┓
|Quick Cash-Press A for $20                     | 
|───────────────────────────────────────────────|
|Quick Cash  Press B for $100                   |       
|───────────────────────────────────────────────|
|Quick Cash  Press C for $200                   |
|───────────────────────────────────────────────|
|Press any other key to choose your own amount  |
|───────────────────────────────────────────────|
|Press q to log out and exit                    |
┗━━━─────────────────────────────────────────━━━┛ """)

               withdraw_key = str(input("Enter Choice:"))
               if withdraw_key == "a":
                   withdraw = 20
               elif withdraw_key == "b":
                   withdraw = 100
               elif withdraw_key == "c":
                   withdraw = 200
               elif withdraw_key == "A":
                   withdraw = 20
               elif withdraw_key == "B":
                   withdraw = 100
               elif withdraw_key == "C":
                   withdraw = 200
               else:
                   valid_amount = False
                   while valid_amount == False:
                       withdraw = float(
                           input(
                               "Please enter the amount you want to withdraw in multiples of 20 : "
                           )
                       )
                       multiple_of_20 = withdraw % 20
                       if multiple_of_20 == 0:
                           valid_amount = True
               if withdraw > Balance[client_id]:
                   print("We are sorry, there are currently insufficient funds in your account which makes that transaction impossible, please try again.")
                   str(input("Press any key to continue"))
                   continue
               elif withdraw > 500:
                   print("Welcome " + name)
                   print("The transaction limit at this ATM is $500, please try again with a lower amount of money")
                   str(input("press any key to continue"))
                   continue
               else:
                   Balance[client_id] = Balance[client_id] - withdraw
                   Balance_withcents = "{:.2f}".format(Balance[client_id])
                   withdraw = "{:.2f}".format(withdraw)
                   print("You have Withdrawn  : $",withdraw )
                   print("Your current balance is : $", Balance_withcents)
                   str(input("Press any key to continue"))
                   continue
           elif choice == "2":
               Balance_withcents = "{:.2f}".format(Balance[client_id])
               print("Your Current Balance is : $", Balance[client_id])
               depot = float(input("Enter the amount you want to deposit :"))
               Balance[client_id] = Balance[client_id] + depot
               Balance_withcents = "{:.2f}".format(Balance[client_id])
               print("Your new balance is : $", Balance_withcents)
               str(input("Press any key to continue"))
               continue
           elif choice == "3":    
               print("Welcome " + name)
               Balance_withcents = "{:.2f}".format(Balance[client_id])
               print("Your Balance is : $", Balance[client_id])
               str(input("Press any key to continue"))
               continue
           elif choice == "4":
               print("Welcome " + name)
               valid_pin = False
               for pin_attempts in range(3):
                   code = (input("Enter your Current Pin: "))
                   if code == PIN[client_id]:
                       newPin = (input("Enter your New Pin :"))
                       PIN[client_id] = newPin
                       str(input("Your PIN has been updated ..press any key to continue"))
                       valid_pin = True
                       break
                   else:
                       valid_pin = False
                       print("Invalid Pin")
               if valid_pin == False:
                   str(input("You have entered an incorrect pin 3 times, please try again later."))
                   continue
           else:
               print("That is an invalid chgoice, please try again.")
