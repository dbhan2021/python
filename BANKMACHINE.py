##ATM Program
CurrentClinet=0
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




print("Welcome to the Bank")
while input !='q' or input !="Q"
    name=input("Enter your first and last name associated with your account seperated by a space: ")

    if name != ClientName:
        print("Sorry, we don't seem to have an account under that name, please try again ")

        input("Enter your first and last name associated with your account seperated by a space: ")

    else:
        code=int(input("Enter your 4 digit code associated with your account please: "))


    if code==PIN

    print("welcome" + name)
    print(
    """Press 1 to withdraw money
    Press 2 to  deposit money
    Press 3 to check your balance
    Press 4 to change your pin
    Press q to quit
   """)



