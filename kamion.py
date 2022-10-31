import tkinter
from random import *
canvas= tkinter.Canvas(width = 1000, height = 600)
canvas.pack()








def kamion():
    x3=250
    canvas.create_rectangle(350,100,650,230,fill='red')
    canvas.create_rectangle(650,150,700,230,fill='black')
    canvas.create_rectangle(670,160,690,200,fill='blue')
    for i in range(2):
        canvas.create_oval(x3+120,200,x3+180,260,fill='black')
        canvas.create_oval(x3+130,210,x3+170,250,fill='gray')
        x3 +=180





kamion()
