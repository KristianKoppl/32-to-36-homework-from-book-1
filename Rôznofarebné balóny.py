from random import *
import tkinter
canvas=tkinter.Canvas(width=1000,height=500,background='white')
canvas.pack()

x=130
for i in range(8):
    x=x+50
    farba= choice(('red','black', 'blue', 'green', 'cyan', 'magenta', 'saddle brown', 'gray', 'brown', 'yellow', 'gold', 'pink'))
    canvas.create_oval(x+60,100,x+150,185,outline='black',width=1,fill= farba)
x=150
for i in range(8):
    x=x+50
    canvas.create_line(380,450,x+80,185,width=1,fill='black')

