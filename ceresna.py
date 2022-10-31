from random import *
import tkinter
canvas=tkinter.Canvas(bg='white',width=1000,height=800)
canvas.pack()
x=0
y=0

def ceresna():
    x3=320
    canvas.create_rectangle(430,340,470,450,fill='brown')
    canvas.create_oval(400,250,500,350,fill='green')
    canvas.create_line(475,290,485,310,fill='black')
    canvas.create_line(475,290,465,310,fill='black')
    
    for i in range(2):
        canvas.create_oval(x3+140,310,x3+150,320,fill='red')
        x3 +=20



ceresna()
