from random import *
import tkinter
canvas=tkinter.Canvas(bg='white',width=500,height=500)
canvas.pack()







def stvorcekovi():
    x=-50
    y=-50
    y1=0
    for i in range (50):
        canvas.create_line(x+50,y1,x+50,500)
        canvas.create_line(0,y+50,500,y+50)
        x+=10
        y+=10






stvorcekovi()
