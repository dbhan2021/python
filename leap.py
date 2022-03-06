#Pyth leap year
#By Diya
#Feb 2022

year=int(input("Please enter a date between 1900 and 2100: "))

if(year <1900 or year >2100):
    print("Out of Range")
else:
    print(" ")
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) :
      print("Leap Year")
    else:
        print("Not a Leap Year")


