import tkinter
from random import *
canvas= tkinter.Canvas(width = 1000, height = 600)
canvas.pack()

def tvar():
    x=20
    x1=-80
    for i in range(8):
        a1=randint(240,330)
        a=choice(('red','yellow','blue','green','white','orange','black','dark green'))
        b=choice(('red','yellow','blue','green','white','orange','black','dark green'))
        c=choice(('red','yellow','blue','green','white','orange','black','dark green'))
        d=choice(('red','yellow','blue','green','white','orange','black','dark green'))
        canvas.create_rectangle(x1+100,200,x1+300,400,fill=a,outline=a)
        canvas.create_rectangle(x1+150,360+randrange(-10,20),x1+240,380+randrange(-10,20),fill=b,outline=b)
        canvas.create_rectangle(x1+180,320+randrange(-10,20),x1+210,350+randrange(-10,20),fill=c,outline= c)
        x1+=250
        canvas.create_rectangle(x+20+randrange(0,20),a1-40,x+50+randrange(0,20),a1,fill=d,outline = d)
        x+= 124

    
            






tvar()
