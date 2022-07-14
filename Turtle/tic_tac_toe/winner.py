

import turtle

import tic_tac_toe.tic as tic
import tic_tac_toe.graphics as graphics


graphics.table()

def get_mouse_click_coor(x, y):
    #turtle.onscreenclick(None)
    print(x, y)
    print("start")
    #A=graphics.check(x,y)
    #tic.game(A)

screen = turtle.Screen()

turtle.onscreenclick(get_mouse_click_coor,1)

screen.mainloop()

#get_mouse_click_coor()
#A=graphics.click2()
#tic.game(A)