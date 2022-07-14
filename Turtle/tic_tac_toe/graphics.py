import turtle



bud=turtle.Turtle()



def table():

    
    bud.left(90)
    bud.backward(30)
    bud.forward(90)
    bud .backward(30)
    bud.right(90)
    bud.forward(60)
    bud .backward(180)
    bud.forward(60)
    bud.left(90)
    bud.forward(30)
    bud.backward(90)
    bud.forward(30)
    bud.right(90)
    bud.backward(60)
    bud.forward(180)
    bud.backward(60)

def drawX(x,y):
    bud.setheading(0)
    bud.penup()
    bud.setpos(x,y)
    bud.pendown()
    bud.right(45)
    bud.forward(30)
    bud.penup()
    bud.setpos(x+20,y)
    bud.pendown()
    bud.left(180)
    bud.left(90)
    bud.forward(30)
    bud.left(0)


def drawO(X,Y):
    bud.setheading(270)
    bud.penup()
    bud.setpos(X,Y)
    bud.pendown()
    bud.circle(10)

def check(P,Q):
    
    
    

    if P<=-59 and 59>=Q>=29:
        return(0)
    if -59<P<=0 and  59>=Q>=29: 
        return(1) 
    if     P>0 and Q>29:
        return (2)
    if P<=-59 and 0<=Q<=29:
        return 3
    if -60<=P<=0 and  0<=Q<=29:
        return(4)
    if P>=0 and  0<=Q<=29:
        return (5)

    if P<=-59 and -30<=Q<=0:
        return(6)

    if -60<=P<=0 and -30<=Q<=0:
        return(7)  

    if  P>=0 and  -30<=Q<=0:  
        return(8)   




def buttonclick(x,y):
    P=x
    Q=y
    A=check(x,y)
    print('A',A)
    return
    print("You clicked at this coordinate({0},{1})".format(x,y))
    

def get_coor(x, y):
    A=check(x, y)
    
    print('A',A)

def click2():
    A=0
    screen = turtle.Screen()

    turtle.onscreenclick(get_coor)
    screen.mainloop()
    return A




def click():
    A=0
    c=0
    if c==0:
        turtle.onscreenclick(buttonclick,1)
        turtle.done()
        

        return(A)
        
        turtle.listen()  # listen to incoming connections
        #
        turtle.speed(10) 
        c+=1
        
        
    
    

#

#drawO()

def main():
    table()
    #t=tic.game()
    



    
    turtle.done() 
#drawO(O[0][0],O[0][1])
#drawO(O[2][0],O[2][1])

#click2()



    


    
 
