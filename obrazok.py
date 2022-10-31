from random import *
import tkinter
canvas=tkinter.Canvas(bg='white',width=1000,height=800)
canvas.pack()
x=0
y=0


def obrazok():
    y=-80
    canvas.create_oval(50,420,150,500,fill='brown')
    canvas.create_rectangle(0,450,1000,800,fill='blue')
    canvas.create_line(100,300,100,420,fill='black',width=2)
    canvas.create_rectangle(100,300,150,350,fill='green',width=2)
    canvas.create_oval(110,310,140,340,fill='yellow',outline='yellow')
    canvas.create_oval(120,310,148,335,fill='green',outline='green')
    canvas.create_polygon(350,470, 450,470, 480,420, 320,420,fill='white',outline='black',width = 2)
    canvas.create_polygon(350,470, 450,470, 461,450, 339,450,fill='blue',outline='black',width = 2)
    canvas.create_line(400,320,400,420,fill='black',width = 2)
    canvas.create_polygon(400,420, 450,390, 400,320,  fill='white',outline='black',width=2)
    for i in range(2):
        canvas.create_oval(750,300+y,850,400+y,fill='yellow',outline='yellow')
        y +=300
    
    canvas.create_oval(790,220,900,320,fill='white',outline='white')
    canvas.create_oval(790,520,900,620,fill='blue',outline='blue')


obrazok()
