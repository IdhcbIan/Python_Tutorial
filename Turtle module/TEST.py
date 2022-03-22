


import turtle as tu
import tkinter
#import turtle
"""
times = 0
branchLen = 150
t = tu.Turtle()
t.down()
while times == 0:
    if t.forward(branchLen > 15):
        #t.backward(100)
        
        t.color("green")
        t.forward(branchLen)
        t.right(20)
        (branchLen-15)
        t.forward(branchLen)
        t.left(40)
        (branchLen-15)
        t.forward(branchLen)
        t.right(20)
        t.backward(branchLen)


t.mainloop()
"""
#-------------------------


import turtle

MyWin = turtle.Screen()
MyWin.screensize(20000, 20000)

t = turtle.Turtle()

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-15, t)
        t.right(20)
        t.backward(branchLen)


def main():
    
    myWin = turtle.Screen()
    
    t.up()
    #t.backward(100)
    t.down()
    t.color("green")
    tree(100, t)
    myWin.exitonclick()



t.color("white")
t.right(90)
t.forward(400)
t.right(180)
main()

tu.getscreen().getcanvas().postscript(file='outputname.ps')


#////////////////////////////////


"""

import turtle



def init_turtle(t):
    '''
    Set pen size, speed, and color
    '''
    t.pensize(2)
    t.speed(0)
    t.color('white')


def base(t, length, n=4):
    '''
    Draw a polygon of a given side length
    '''
    for k in range(n):
        t.forward(length)
        t.left(360/n)


def flake(t, length, copies=4, n=4):
    for k in range(copies):
        base(t, length, n)
        t.left(360/copies)


# %% Main code if script is run
if __name__ == '__main__':
    wn = turtle.Screen()
    # wn.clearscreen()
    wn.bgcolor('dark blue')
    kasa = turtle.Turtle()

    L = 90
    S = 6
    N = 17
    init_turtle(kasa)
    kasa.penup()
    kasa.setposition(0, 0)
    kasa.left(360/S/2)
    kasa.pendown()
    flake(kasa, L, N, S)
    wn.exitonclick()

"""




#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
