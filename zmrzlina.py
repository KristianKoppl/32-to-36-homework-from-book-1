from random import *
import tkinter
canvas=tkinter.Canvas(width=1000,height=800,background='white')
canvas.pack()

canvas.create_oval(180,140,235,195,outline='red',width=8,fill='red')
canvas.create_oval(160,160,225,215,outline='yellow',width=8,fill='yellow')
canvas.create_oval(195,160,255,215,outline='green',width=8,fill='green')
canvas.create_rectangle(160,200,255,245,outline='saddle brown',width=6,fill='white')
canvas.create_line(200,400,255,245,fill='saddle brown',width=6)
canvas.create_line(160,245,200,400,fill='saddle brown',width=6)
y=200
for i in range(1,4):
    y=y+10
    canvas.create_rectangle(160,200,255,y,outline='saddle brown',width=6)

