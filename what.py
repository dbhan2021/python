
# Title: Friend Database
# Version: 1.0
# Date: Feb,24,2022

# Author: Diya Bhan
# Course: Computer Science ICS2O
# School: Ashbury College, Ottawa
# Teacher: Mr. Giansante

# Description: This program simulates a database that stores
# the names of the author's friends.


choice = 0

while(choice != 6):
 print("[1] Lily Green")
 print("[2] Stella Noen")
 print("[3] Bianca Smith")
 print("[4] Robby Birkin")
 print("[5] Melssa Branc")
 print("[6] Exit Program")
   
 choice = int(input("Please select a number (1 to 6): "))

 if(choice < 1 or choice > 6):
  print("That number is not valid.")
    
    
 if(choice == 1):
  print("-------------------------------------------------------------------")
  print("Lily Green")
  print("123 Main Street")
  print("613-555-0001")
  print("-------------------------------------------------------------------")
     
 if(choice == 2):
  print("-------------------------------------------------------------------")
  print("Stella Noen")
  print("34 Bank Street")
  print("343-293-9045")
  print("-------------------------------------------------------------------")
 if(choice == 3):
  print("-------------------------------------------------------------------")
  print("Bianca Smith")
  print("04 Highland Street")
  print("613-453-1243")
  print("-------------------------------------------------------------------")
 if(choice == 4):
  print("-------------------------------------------------------------------")
  print("Robby Birkin")
  print("23 Bayward Street")
  print("613-214-0303")
  print("-------------------------------------------------------------------")
 if(choice == 5):
  print("-------------------------------------------------------------------")
  print("Melssa Branc")
  print("2 Meries Street")
  print("613-222-9453")
  print("-------------------------------------------------------------------")
       
    
 if(choice == 6):
  print("Goodbye")
  break


  
      

