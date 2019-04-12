"""Try displaying a photo of yourself on the canvas using tkinter.
Make sure it’s a GIF image! Can you make it move across the
screen?"""

import time
from tkinter import *

tk = Tk()
w = 500
h = 500
canvas = Canvas(tk, width=w, height=h)
canvas.pack()

#my_image = PhotoImage(file='C:\\WinPython-64bit-3.5.3.0Qt5\\notebooks\\stani.gif')
my_image = PhotoImage(file='img_title.png')
my_img = canvas.create_image(0, 0, anchor=NW, image=my_image)

for x in range(0, 60):
	canvas.move(my_img, 5, 0)
	tk.update()
	time.sleep(0.05)
'''
for x in range(0, 60):
	canvas.move(my_img, 0, 5)
	tk.update()
	time.sleep(0.05)
'''
for x in range(0, 60):
	canvas.move(my_img, -2.5, 0)
	tk.update()
	time.sleep(0.05)
'''
for x in range(0, 60):
	canvas.move(my_img, 0, -5)
	tk.update()
	time.sleep(0.05)
'''