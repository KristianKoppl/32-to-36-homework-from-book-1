from random import *
import tkinter
canvas=tkinter.Canvas(width=1000,height=500,background='white')
canvas.pack()
x = randrange(900)
y = randrange(500)
velkost = randint(30, 350,)
uhol = randrange(360)


for i in range(1,150):
    canvas.create_line(550, 250,randrange(-100000,100000), randrange(-10000,10000), fill=choice(('red','black', 'blue', 'green', 'cyan', 'magenta', 'saddle brown', 'gray', 'brown', 'yellow', 'gold', 'pink')),width=randrange(0, 16,))
    canvas.create_line(550, 250,randrange(-100000,100000), randrange(-1000,10000), fill=choice(('red','black', 'blue', 'green', 'cyan', 'magenta', 'saddle brown', 'gray', 'brown', 'yellow', 'gold', 'pink')),width=randrange(0, 12,))
    canvas.create_line(550, 250,randrange(-100000,10000), randrange(-10000,10000), fill=choice(('red','black', 'blue', 'green', 'cyan', 'magenta', 'saddle brown', 'gray', 'brown', 'yellow', 'gold', 'pink')),width=randrange(0, 10,))
    canvas.create_line(550, 250,randrange(-10000,100000), randrange(-10000,10000), fill=choice(('red','black', 'blue', 'green', 'cyan', 'magenta', 'saddle brown', 'gray', 'brown', 'yellow', 'gold', 'pink')),width=randrange(0, 8,))
