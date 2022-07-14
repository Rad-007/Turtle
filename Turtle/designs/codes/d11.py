import colorsys
import turtle
import colorsys
t=turtle.Turtle()

s=turtle.Screen()

s.bgcolor('black')
t.speed(0)

h=6

for i in range(150):
    c=colorsys.hls_to_rgb(h,0.5,0.5)
    t.pencolor(c)
    h+=.005

    t.right(i)
    t.circle(200,i)
    t.forward(i)

    for j in range(5):
        t.forward(i)
        t.right(90)

t.hideturtle()
turtle.done()

