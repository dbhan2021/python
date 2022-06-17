import getpass
import string
import os

##ATM Program
CurrentClinet = 0
ClientName = list(range(11))
PIN = list(range(11))
Balance = list(range(11))

ClientName[1] = "John Smith"
PIN[1] = 1212
Balance[1] = 20000.00

ClientName[2] = "Mary Jane"
PIN[2] = 5555
Balance[2] = 100.00

ClientName[3] = "Josh Brooks"
PIN[3] = 2222
Balance[3] = 40.00

ClientName[4] = "Casey White"
PIN[4] = 0000
Balance[4] = 4000000.00

ClientName[5] = "Adam Stan"
PIN[5] = 1242
Balance[5] = 2000.00

ClientName[6] = "Lily Green"
PIN[6] = 9090
Balance[6] = 300000.00

ClientName[7] = "Brandy Kate"
PIN[7] = 1234
Balance[7] = 1000000.00

ClientName[8] = "Sandy Bell"
PIN[8] = 6662
Balance[8] = 9000.00

ClientName[9] = "Sasha HilSasha Hilll"
PIN[9] = 9494
Balance[9] = 230000.00

ClientName[10] = "Nick Rich"
PIN[10] = 6000
Balance[10] = 3030.00


while input != "q":
    print("Welcome to the Bank")
    valid_client = False
    name = input(
        "Enter your first and last name associated with your account seperated by a space: "
    )
    # Check if Name is the cutomers
    for client_id in range(1, 10):
        if name == ClientName[client_id]:
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
            code = int(
                input("Enter your 4 digit code associated with your account please: ")
            )
            if code == PIN[client_id]:
                print("Valid Pin")
                valid_pin = True
                break
            else:
                valid_pin = False
                print("Invalid Pin")
    if valid_pin == False:
        print("Your Entered Invalid Pin 3 Times Pls try later...")
        continue
    else:
        choice = ""
        while choice != "q":
            print("Welcome " + name)
            choice = str(
                input(
                    """    Press 1 to withdraw money
            Press 2 to  deposit money
            Press 3 to check your balance
            Press 4 to change your pin
            Press q to quit
            """
                )
            )
            if choice == "q":
                print("Bye " + name)
                break
            elif choice == "1":
                withdraw = int(input("Enter Amount you want to Withdraw : "))
                if withdraw > Balance[client_id]:
                    print("Insufficient Funds in your account ...")
                    continue
                else:
                    Balance[client_id] = Balance[client_id] - withdraw
                    print("Your Balance is : $", Balance[client_id])
                    continue
            elif choice == "2":
                depot = int(input("Enter Amount you want to Deposit"))
                Balance[client_id] = Balance[client_id] + depot
                print("Your Balance is : $", Balance[client_id])
                continue
            elif choice == "3":
                print("Your Balance is : $", Balance[client_id])
                continue
            elif choice == "4":
                newPin = int(input("Enter  New Pin :"))
                PIN[client_id] = newPin
                continue
            else:
                print("Invalid Choice...")
