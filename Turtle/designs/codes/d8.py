import turtle

turtle.bgcolor('black')

turtle.speed(0)

turtle.pencolor('yellow')

turtle.pensize(2)

for i in range(1,400):
    turtle.forward(10+i)

    turtle.right(91)

    i+=2

turtle.done()  