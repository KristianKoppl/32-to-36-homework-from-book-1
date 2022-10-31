from random import *
import tkinter
canvas=tkinter.Canvas(bg='white',width=1000,height=800)
canvas.pack()
x=0
y=0

def baloon():
    canvas.create_oval(400,265,500,365,fill='blue')
    canvas.create_line(485,350,455,450,fill='black')
    canvas.create_line(415,350,455,450,fill='black')
    canvas.create_rectangle(430,450,480,500,fill='red')





baloon()
