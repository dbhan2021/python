import turtle
colors = ['light green','white','black','dark green']
turtle.bgcolor("dark green")
turtle.speed(0)
turtle.pensize(4)
##measurements are 630,395
#rectangle
turtle.penup()
turtle.pencolor('white')
turtle.goto(600,360)
turtle.pendown()
turtle.goto(-600,360)
turtle.goto(-600,-360)
turtle.goto(600,-360)
turtle.goto(600,360)
turtle.penup()



###circlemini2

turtle.pencolor("dark green")
turtle.penup()
turtle.goto(-600,360)
turtle.circle(8,120)


##center
turtle.pensize(4)
turtle.pencolor("white")
turtle.penup()
turtle.goto(0,-360)
turtle.pendown()
turtle.goto(0,360)
turtle.penup()
turtle.goto(87,50)
turtle.pendown()
turtle.circle(100,360)
turtle.penup()
turtle.goto(0,0)
turtle.dot(10, "white")
turtle.penup()

#rect1
turtle.goto(-600,200)
turtle.pendown()
turtle.goto(-450,200)
turtle.goto(-450,-200)
turtle.goto(-600,-200)
turtle.penup()
#rect1.2
turtle.goto(-600,-100)
turtle.pendown()
turtle.goto(-550,-100)
turtle.goto(-550,100)
turtle.goto(-600,100)
turtle.penup()
turtle.goto(-505,0)
turtle.dot(10, "white")
#semicircle1
turtle.goto(-450,130)
turtle.right(160)
turtle.pendown()
for i in range (99):
    turtle.right(1)
    turtle.forward(3)


#rect1
turtle.penup()
turtle.goto(600,200)
turtle.pendown()
turtle.goto(450,200)
turtle.goto(450,-200)
turtle.goto(600,-200)
turtle.penup()
#rect1.2
turtle.goto(600,-100)
turtle.pendown()
turtle.goto(550,-100)
turtle.goto(550,100)
turtle.goto(600,100)
turtle.penup()
turtle.goto(505,0)
turtle.dot(10, "white")
#semicircle1
turtle.goto(450,130)

turtle.pendown()
for i in range (97):
    turtle.left(1)
    turtle.forward(3)



turtle.penup()


#circleminitbotoomleft
turtle.goto(-595,-355)


turtle.dot(13)
turtle.dot(9,'dark green')

#circleminitopright

turtle.goto(595,355)
turtle.dot(14)
turtle.dot(9,'dark green')

###circleminitbottomright

turtle.goto(595,-355)
turtle.dot(14)
turtle.dot(9,'dark green')


#circlemini2topleft

turtle.goto(-595,355)
turtle.dot(14)
turtle.dot(9,'dark green')
