import turtle
scr = turtle.Turtle()
scr.speed(0)
scr.hideturtle()
for i in range(10):
    for j in range(4):
      scr.forward(100)
      scr.right(90)
    scr.right(36)
    scr.forward(50)
turtle.mainloop()
