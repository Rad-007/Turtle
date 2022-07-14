import turtle

turtle.speed(0)

turtle.pensize(4)

turtle.bgcolor('black')

for i in range(80):
    if i%2==0:

        turtle.circle(150)
        turtle.color('yellow')
        turtle.left(25)

    else:

        turtle.circle(150)
        turtle.color('blue')
        turtle.left(25)


turtle.done()