from random import *
import tkinter
canvas=tkinter.Canvas(bg='white',width=1000,height=800)
canvas.pack()
x=0
y=0




def ja_nevem_uz():
    x=-40
    canvas.create_rectangle(-1,700,1001,750,fill='green',outline='green')
    canvas.create_oval(100,450,250,600,fill='red',outline='red')
    canvas.create_rectangle(100,500,600,600,fill='white',outline='white')
    canvas.create_rectangle(150,500,200,600,fill='brown',outline='brown')
    canvas.create_oval(150,590,200,610,fill='brown',outline='brown')
    canvas.create_oval(150,460,170,480,fill='white',outline='white')
    canvas.create_oval(190,470,230,490,fill='white',outline='white')
    canvas.create_oval(130,480,150,490,fill='white',outline='white')

    for i in range(50):
        canvas.create_line(x+50,670,x+50,700,fill='green')
        x+=20

def slnko():
    for i in range(20):
        canvas.create_line(0,0,randrange(0,500),randrange(0,500),fill='yellow',width = 3)
        
def pozemky():
    y=450
    for i in range(5):
        canvas.create_rectangle(y+randrange(0,50),0+randrange(0,50),y+randrange(0,50),0+randrange(0,50),fill='white',outline='black')
        y+=50


    y1=450
    for j in range(5):
        canvas.create_rectangle(y1+randrange(0,50),100+randrange(0,50),y1+randrange(0,50),100+randrange(0,50),fill='white',outline='black')
        y1+=50       

    y2=450
    for j in range(5):
        canvas.create_rectangle(y2+randrange(0,50),150+randrange(0,50),y2+randrange(0,50),150+randrange(0,50),fill='white',outline='black')
        y2+=50       



def jazero():
    y3 =50
    for i in range(20):
        
        canvas.create_oval(350+100+y3,300+y3,350+y3+300,600-y3,outline='blue')
        y3+=10
        






def spust():
    ja_nevem_uz()
    slnko()
    pozemky()
    jazero()





    
spust()
