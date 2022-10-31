import tkinter
from random import *
canvas= tkinter.Canvas(width = 700, height = 800)
canvas.pack()


def train():
    x = 10
    for i in range(4):
        canvas.create_rectangle(x+150,120,x+160,130)
        canvas.create_rectangle(x+40,100,x+150,150,fill='lime')
        x+=120
        
        x1=-50
        for i in range(8):
            x1 +=60
            canvas.create_rectangle(x1+45,110,x1+80,130,fill='blue')
            canvas.create_oval(x1+50,150,x1+80,180,fill='black')
  
def rusen():
    x2 = 500
    x3 = 520 
    canvas.create_rectangle(530,80,680,150,fill='dark green')
    canvas.create_rectangle(530,30,580,80,fill='red')
    canvas.create_rectangle(630,50,650,80,fill='blue')

    for i in range(4):
        canvas.create_line(x3+120-30,20,x3+130-30,40,fill='black')
        x3 +=10 
    for i in range(4):
        

            
        canvas.create_oval(x2+50,150,x2+80,180,fill='black')
        
        x2 += 30
        
rusen()
train()




def vlak():
    for i in range(4):
        canvas.create_rectangle(x+150,120,x+160,130)



        
        canvas.create_rectangle(x+40,100,x+150,150)
        x+=120
    





















































                                
