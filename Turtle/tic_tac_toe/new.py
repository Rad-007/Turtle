

import turtle

import tic_tac_toe.tic as tic
import tic_tac_toe.graphics as graphics

c=0

graphics.table()

def get_mouse_click_coor(x, y):
    global c
    c=c+1
    #turtle.onscreenclick(None)
    print(x, y)
    print("start")
    A=graphics.check(x,y)
    print('C',c)
    tic.game(A,c)

print("screen")
z=0
while z<=8:

    
    screen = turtle.Screen()

    turtle.onscreenclick(get_mouse_click_coor,1)

    screen.mainloop()
    z+=1

#get_mouse_click_coor()
#A=graphics.click2()
#tic.game(A)