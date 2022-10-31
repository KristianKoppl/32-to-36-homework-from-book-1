from random import *
import tkinter
canvas=tkinter.Canvas(width=1000,height=700,background='black')
canvas.pack()

#auto
canvas.create_rectangle(190,600,290,640,outline='gray12',width=8,fill='gold')
canvas.create_rectangle(120,560,355,600,outline='gray12',width=8,fill='gold')
y=560
for i in range(1,3):
    y=y+12
    canvas.create_rectangle(120,560,355,y,outline='gray8',width=8)

#mesiac
canvas.create_oval(160,160,225,215,outline='light gray',width=8,fill='light gray')
canvas.create_oval(175,160,225,215,outline='black',width=8,fill='black')

#tráva
canvas.create_rectangle(-10,680,1020,720,outline='dark green',fill='green',width=8)

#kolesá
canvas.create_oval(110,600,185,672,outline='gray10',width=8,fill='gray16')
canvas.create_oval(290,600,365,672,outline='gray10',width=8,fill='gray16')
canvas.create_oval(310,620,345,652,outline='gray10',width=8,fill='gray68')
canvas.create_oval(130,620,165,652,outline='gray10',width=8,fill='gray68')


#čelné sklo
canvas.create_line(250,500,320,560,width=8,fill='cyan')

#svetlo
canvas.create_rectangle(355,565,365,595,outline='yellow3',width=4,fill='yellow2')
canvas.create_rectangle(110,565,120,595,outline='red3',width=4,fill='red')

#HAUSE
canvas.create_rectangle(650,450,955,672,outline='gray12',width=8,fill='yellow2')
      #okno
canvas.create_rectangle(810,500,910,582,outline='gray12',width=4,fill='blue')
      #dverá
canvas.create_rectangle(680,500,780,672,outline='gray12',width=4,fill='saddle brown')
       #rámy
canvas.create_line(810,541,910,541,width=3,fill='black')
canvas.create_line(860,500,860,582,width=3,fill='black')
       #rúčka na dverách
canvas.create_line(760,581,760,600,width=3,fill='gray4')
canvas.create_line(760,581,780,581,width=3,fill='gray4')
       #strecha 
canvas.create_line(800,200,606,500,width=3,fill='red')
canvas.create_line(800,200,995,500,width=3,fill='red')




