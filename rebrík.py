from random import *
import tkinter
canvas=tkinter.Canvas(width=1000,height=500,background='white')
canvas.pack()


x=190
y=30
x1=250
for i in range(20):
    print(i+5)
    x=x+5
    y=y+15
    x1=x1+5
    canvas.create_line(x, y, x1, y)
    canvas.update()
    canvas.after(20)
    

canvas.create_line(200, 30, 300, 340)
canvas.create_line(240, 30, 340, 340)
