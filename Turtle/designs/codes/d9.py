import turtle

turtle.bgcolor("blue")

turtle.pensize(4)

turtle.speed(0)

for i in range(10,350,2):
    turtle.pencolor("yellow")
    turtle.forward(i)
    turtle.left(59.3)

turtle.done()