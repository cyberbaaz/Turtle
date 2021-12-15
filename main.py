import turtle
ninja = turtle.Turtle()

ninja.speed(700)

for i in range(200):
    ninja.forward(100)
    ninja.left(30)
    ninja.right(40)
    ninja.right(30)
    ninja.right(40)
    ninja.left(100)
    ninja.forward(100)
    ninja.right(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()