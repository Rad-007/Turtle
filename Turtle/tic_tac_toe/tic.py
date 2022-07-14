import tic_tac_toe.graphics as graphics 
import turtle

player1=[]
player2=[]


board=['','','','','A','','','','']

X={0:[-104,61],1:[-43,53],2:[23,54],
        3:[-102,21],4:[-44,24],5:[19,21],
        6:[-102,-11],7:[-41,-10],8:[16,-10]}

O={0:[-92,46],1:[-37,46],2:[25,46],
        3:[-92,17],4:[-37,17],5:[25,17],
        6:[-92,-17],7:[-37,-17],8:[25,-17]}



graphics.table()

def winner(l):
    l.sort()
    print(l)
    op={1:[0,1,2],
    2:[3,4,5],3:[6,7,8],4:[0,3,6],5:[1,4,7],6:[2,5,8],7:[0,4,8],8:[2,4,6]}
    l1=l[0:3]
    s=0
    for i in range(1,9):
        p=False
        if l1==op[i]:
            p=True
            break
        else:
           p= False 
    return (p)   






    

 #onscreen function to send coordinate
# set the speed
#           
 # listen to incoming connections
#
#turtle.speed(10)

def game():
    
    p=0
    
    flag=False
    c=0
    while c<=8:
        c+=1
        print('PLAYER 1')
        x=int(input("Enter Position:"))
        player1.append(x)
        
        graphics.drawX(X[x][0],X[x][1])
        
        print(player1)
        if c>=10:
            break
        if c>=5:
            if c%2==1:
                

                flag=winner(player1)
                print(flag)
            else:
                flag=winner(player2)    
        if flag:
            p=c%2
            break
        
        c+=1
        
        print('PLAYER 2')
        o=int(input("Enter postion:"))
        player2.append(o)
            
        graphics.drawO(O[o][0],O[o][1])
            
        print(player2)
        

        

    if p==1:
        print("Player 1 Wins")
    else:
        print("Player 2 Wins ")    
        
        
game()            
        
turtle.done()



    
















