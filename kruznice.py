from random import *
import tkinter
canvas=tkinter.Canvas(bg='white',width=1000,height=800)
canvas.pack()
x=0
y=0

def kruznice ():
    x=0
    for i in range(20):
        color=choice(('purple','pink','yellow','black','brown','blue','green','red'))
        canvas.create_oval(x+randrange(50,100),50+randrange(50,100),x+randrange(50,100),100+randrange(50,100), outline=color,fill='white',width=3)
        x +=20
        








kruznice()
