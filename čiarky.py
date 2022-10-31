from random import *
import tkinter
canvas=tkinter.Canvas(bg='white',width=1000,height=800)
canvas.pack()
x=0
y=0
for i in range(50):
    x+=20
    canvas.create_line(50+x,50,450,450,fill='black',width=2)
    canvas.create_line(50,50+x,1000,800,fill='green',width=2)
    canvas.update()
    canvas.after(100)
    
