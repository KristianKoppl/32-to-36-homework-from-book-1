import tkinter
from random import *
canvas= tkinter.Canvas(width = 1000, height = 600)
canvas.pack()






def postavicka():
    x3=250
    canvas.create_polygon(450,100, 300,300, 600,300,fill= 'white',outline = 'black')
    canvas.create_oval(405,20,495,110,fill='red')    
    for i in range(2):
        canvas.create_rectangle(x3+130,300,x3+160,360,fill='red')

        x3 +=100






postavicka()
