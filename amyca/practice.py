from tkinter import *
from tkinter import PhotoImage
import time


root = Tk()
root.geometry('600x600')
img = PhotoImage(file='img_title.png')

img_amyca = Label(root, image = img)
img_amyca.pack(padx=5, pady=5,  fill='x')
time.sleep(5)
#header_font = ('Courier New', 30)
#welcome_text = Label(root, text='WELCOME TO AMYCA', font=header_font)
#welcome_text.pack(padx=10, pady=10)

#body_font = ('Courier New', 16)

