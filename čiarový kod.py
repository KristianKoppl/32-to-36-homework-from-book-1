from random import *
import tkinter
canvas=tkinter.Canvas(bg='white',width=1000,height=800)
canvas.pack()
x=0
y=0
for i in range(20):
    hrubka=randrange(20)
    print(hrubka)
    x+=20
    canvas.create_line(50+x,50,50+x,450,fill='black',width=hrubka)
