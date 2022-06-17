#Date and time project
#Author:Diya bhan


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


yyyy=1

mm=12

dd=1

while yyyy !=0:
    yyyy=int(input("Please enter any year between 1900 and 2099 print '0' to quit: "))
    
    if yyyy==0:
        print ("Goodbye")
        break
    
    if yyyy < 1900 or yyyy > 2099:
        print("That is an invalid entry - Please enter a year between 1900 and 2099")
        yyyy=int(input("Please enter any year between 1900 and 2099 print '0' to quit: "))
    else:
        mm= int(input("Please enter any month between 1 and 12 print 'q' to quit: "))
       
     
    if (yyyy % 4 == 0) and (yyyy % 100 != 0) or (yyyy % 400 == 0) :
        print("That is a leap year")
        
        mm= int(input("Please enter any month between 1 and 12 print 'q' to quit: "))

    if mm==0:
        print ("Goodbye")
        break
    
    if mm < 1 or mm > 12:
        print("That is an invalid entry -  Please enter a month between 1 and 12")
        
    else:
    
        dd=int(input("Please enter any day between 1 and 31 print 'q' to quit: "))

    if dd==0:
        print ("Goodbye")
        break

    if dd < 1 or dd > 31:
        print("That is an invalid entry - Please enter a day between 1 and 31")
   
           
    
    if (yyyy % 4 == 0) and (yyyy % 100 != 0) or (yyyy % 400 == 0) :

        
        last2digits = abs(yyyy)%100
        
        step2= int(last2digits/4)
        
        step3=step2+last2digits
        
        step4= step3 +leap_year[mm]
        
        step5=step4+dd  
    else:
        last2digits = abs(yyyy)%100
        step2= int(last2digits/4)
        step3=step2+last2digits
        step4alt= step3+mm
        step5= step4alt+dd
            
    if yyyy>1999:
        step6=step5+6
        step7 = step6 % 7
        print("The Day is :", day[step7])
    else:
        step7 = step5 % 7
        print("The Day is :", day[step7])
    
    

    

    




        






















