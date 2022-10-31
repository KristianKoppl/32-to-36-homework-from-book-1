from random import *
import tkinter
canvas=tkinter.Canvas(bg='white',width=1000,height=800)
canvas.pack()
x=0
y=0






def jaskina():
    x=-50
    

    for i in range(1000):
        canvas.create_line(x+50,randrange(700,750),x+50,800,fill='green')
        canvas.create_line(x+50,0,x+50,randrange(0,50),fill='green')
        x+=1

    x1=-50
    for i in range (20):
        canvas.create_rectangle(x1+40,650,x1+120,700,outline='brown',width=2)
        x1+=80
def kvapky():
    x2=randrange(0,1000)
    y2=randrange(50,700)
    for i in range(20):
        canvas.create_oval(x2+randrange(20,100),y2+randrange(20,100),x2+randrange(20,100),y2+randrange(20,100),fill='blue')
        x2+=50
        y2+=50

        





    
        





jaskina()
kvapky()
