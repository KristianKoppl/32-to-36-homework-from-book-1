import tkinter
import random
canvas = tkinter.Canvas(width=600,height=600)
canvas.pack()


for i in range(40):
    x = random.randrange(350)
    y = random.randrange(350)
    hrubka = random.randrange(0, 8,)
    velkost = random.randint(30, 200,)
    farba = random.choice(('red','black', 'blue','green','red','yellow','orange','gray'))
    canvas.create_line(50, 50, x+velkost, y+velkost, fill=farba,width=hrubka)


