import tkinter
from random import *
canvas= tkinter.Canvas(width = 1000, height = 600)
canvas.pack()






def hrad():
    canvas.create_rectangle(280,300,710,500,fill='white')

    x=-20
    for i in range (2):
        canvas.create_polygon(x+350,100, x+300,300, x+400,300,fill= 'white',outline = 'black')
        x +=330
        
    x3=250
    for i in range (3):
        canvas.create_rectangle(x3+130,250,x3+160,300,fill='red')
        x3 +=100
        
    x2=210
    for i in range (2):
        canvas.create_oval(x2+110,350,x2+160,400,fill='blue')
        x2 +=300







hrad()
