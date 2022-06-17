import turtle
turtle.speed(5)
#LINE IN THE MIDDLE
turtle.penup( )
turtle.goto(1,7) 
turtle.pendown( )
turtle.goto(1,-70) 
turtle.penup( )
turtle.goto(1,50) 
turtle.pendown( )
turtle.goto(1,113)
#RIGHT LINE
turtle.penup( )
turtle.goto(40,7) 
turtle.pendown( )
turtle.goto(40,-70) 
turtle.penup( )
turtle.goto(40,50) 
turtle.pendown( )
turtle.goto(40,113)
#LEFT LINE
turtle.penup( )
turtle.goto(-39,7) 
turtle.pendown( )
turtle.goto(-39,-70) 
turtle.penup( )
turtle.goto(-39,50) 
turtle.pendown( )
turtle.goto(-39,113)
#DIAGONAL 1
turtle.penup( )
turtle.goto(1,7) 
turtle.pendown( )
turtle.goto(-39,50)
#DIAGONAL 2
turtle.penup( )
turtle.goto(40,7)
turtle.pendown( )
turtle.goto(1,50)
turtle.penup( )
#TRIANGLE1
turtle.goto(-39,113)
turtle.pendown( )
turtle.goto(1,170)
turtle.goto(40,113)
turtle.penup( )
#TRINAGLE TWO
turtle.goto(-39,-70)
turtle.pendown( )
turtle.goto(1,-107)
turtle.goto(40,-70)
turtle.penup( )
#diagonal line1
turtle.goto(-39,7)
turtle.pendown( )
turtle.goto(-20,30)
turtle.penup( )
#diagonal line2
turtle.goto(40,50)
turtle.pendown( )
turtle.goto(20,28)
turtle.penup( )
#finish
turtle.goto(1000,200)


