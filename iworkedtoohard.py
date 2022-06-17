#Date and time project
#Author:Diya bhan

date=" "

month={
    1:1,
    2:4,
    3:4,
    4:0,
    5:2,
    6:5,
    7:0,
    8:3,
    9:6,
    10:1,
    11:4,
    12:6,
}

leap_year={
    1:0,
    2:3,
    3:4,
    4:0,
    5:2,
    6:5,
    7:0,
    8:3,
    9:6,
    10:1,
    11:4,
    12:6,
}

day={
    1:"Sunday",
    2:"Monday",
    3:"Tuesday",
    4:"Wednesday",
    5:"Thursday",
    6:"Friday",
    0:"Saturday",
}



while date !="q":
    date=(input("Please enter any date in the format DD-MM-YYYY, print 'q' to quit: "))

    if  date == "q":
        print("Goodbye")
        break
    else:
        dd, mm, yyyy = map(int, date.split("-"))
        if yyyy < 1900 or yyyy > 2099:
                print("That is an invalid entry - Please enter a year between 1900 and 2099")
                continue
        if mm < 1 or mm > 12:
                print("That is an invalid entry -  Please enter a month between 1 and 12")
                continue
        if dd < 1 or dd > 31:
                print("That is an invalid Entry - Please enter a day between 1 and 31")
                continue
        
        
        last2digits = abs(yyyy)%100
        step2= int(last2digits/4)
        step3=step2+last2digits

        if (yyyy % 4 == 0) and (yyyy % 100 != 0) or (yyyy % 400 == 0) :
            print("That is a leap year")
            step4= step3 + leap_year[mm]
            step5=step4 + dd  
        else:
            step4= step3 + month[mm]
            step5= step4 + dd            
        if yyyy>1999:
           step6=step5+6
           step7 = step6 % 7
           print("The Day is :", day[step7])
        else:
            step7 = step5 % 7
            print("The Day is :", day[step7])
    
    

    

    




        






















