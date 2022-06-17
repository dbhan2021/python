#simplescene
import turtle

colors = ['yellow','red','light yellow' 'light green','light blue', 'pink','gray', 'blue', 'orange','purple', 'green', 'white','black','light pink']
turtle.bgcolor("black")
turtle.speed(0)

turtle.screensize(canvwidth=300, canvheight=300)


turtle.dot(500, "red")
turtle.dot(450, "orange")
turtle.dot(400, "yellow")
turtle.dot(350, "green")
turtle.dot(300, "light blue")
turtle.dot(250, "blue")
turtle.dot(200, "purple")
turtle.dot(150, "light pink")
turtle.pencolor("red")

turtle.penup()
turtle.goto(0,-75)

turtle.pendown()
turtle.circle(75)
turtle.pencolor("orange")
turtle.circle(65)
turtle.pencolor("yellow")
turtle.circle(55)
turtle.pencolor("green")
turtle.circle(45)
turtle.pencolor("light blue")
turtle.circle(35)
turtle.pencolor("blue")
turtle.circle(25)
turtle.pencolor("purple")
turtle.circle(15)
turtle.pencolor("pink")
turtle.circle(5)

turtle.penup()
turtle.goto(0,-200)
turtle.pendown()

    
turtle.speed(50)
turtle.color ('white')
turtle.width(20)
turtle.left(40)
turtle.forward(60)
turtle.circle(30, 200)
turtle.left(240)
turtle.circle(30, 200)
turtle.forward(60)
turtle.penup()



turtle.goto(300,30)
turtle.width(150)
turtle.pendown()
turtle.color ('black')
turtle.goto(-300,30)
turtle.penup()
turtle.goto(300,140)
turtle.pendown()
turtle.color ('black')
turtle.goto(-300,140)
turtle.penup()
turtle.goto(-300,250)
turtle.pendown()
turtle.color ('black')
turtle.goto(300,250)
turtle.penup()
turtle.color ('light green')
turtle.width(20)
turtle.goto(-350,-34)
turtle.pendown()
turtle.goto(350,-34)
turtle.bgcolor("light blue")
turtle.penup()
turtle.goto(200,200)

#skyscene
turtle.dot(100, "white")
turtle.goto(100,200)
turtle.dot(3, "light yellow")
turtle.goto(125,200)
turtle.dot(3, "light yellow")
turtle.goto(150,200)
turtle.dot(3, "light yellow")
turtle.goto(175,200)
turtle.dot(3, "light yellow")
turtle.goto(200,200)
turtle.dot(3, "light yellow")
turtle.goto(225,200)
turtle.dot(3, "light yellow")
turtle.goto(250,200)
turtle.dot(3, "light yellow")
turtle.goto(275,200)
turtle.dot(3, "light yellow")
turtle.goto(300,200)
turtle.dot(3, "light yellow")
turtle.goto(0,200)
turtle.dot(3, "light yellow")
turtle.goto(-200,200)
turtle.dot(3, "light yellow")
turtle.goto(-300,200)
turtle.dot(3, "light yellow")
turtle.goto(-100,200)
turtle.dot(3, "light yellow")
#line 2
turtle.goto(100,100)
turtle.dot(3, "light yellow")
turtle.goto(200,100)
turtle.dot(3, "light yellow")
turtle.goto(300,100)
turtle.dot(3, "light yellow")
turtle.goto(0,100)
turtle.dot(3, "light yellow")
turtle.goto(-200,100)
turtle.dot(3, "light yellow")
turtle.goto(-300,100)
turtle.dot(3, "light yellow")
turtle.goto(-100,100)
turtle.dot(3, "light yellow")
#line3
turtle.goto(100,0)
turtle.dot(3, "light yellow")
turtle.goto(200,0)
turtle.dot(3, "light yellow")
turtle.goto(300,0)
turtle.dot(3, "light yellow")
turtle.goto(0,100)
turtle.dot(3, "light yellow")
turtle.goto(-200,0)
turtle.dot(3, "light yellow")
turtle.goto(-300,0)
turtle.dot(3, "light yellow")
turtle.goto(-100,0)
turtle.dot(3, "light yellow")

#person
turtle.goto(0,40)
turtle.dot(40, "light yellow")
turtle.goto(0,39)
turtle.dot(2, "black")
turtle.goto(7,48)
turtle.dot(2, "black")
turtle.goto(-7,48)
turtle.dot(2, "black")
turtle.goto(7,32)
turtle.pencolor("red")
turtle.pensize(5)
turtle.pendown()
turtle.goto(-7,32)
turtle.penup()
turtle.goto(0,28)
turtle.pencolor("Light yellow")
turtle.pensize(2)
turtle.pendown()
turtle.goto(0,-20)
turtle.goto(12,-25)
turtle.penup()
turtle.goto(0,-20)
turtle.pendown()
turtle.goto(-12,-25)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(12,0)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(-12,0)
turtle.penup()
turtle.goto(13,5)
turtle.pencolor("red")
turtle.pendown()
turtle.goto(30,40)
turtle.write('This is Bob ')
turtle.penup()

#text
turtle.goto(-40,280)
turtle.pencolor("green")
turtle.write('Bob imagining night vs day')