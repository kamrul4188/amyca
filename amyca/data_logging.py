from tkinter import *
import sys
from tkinter import scrolledtext

filename = "index.htm"
root = Tk()
top = Frame(root)
top.pack(side='top')



text.pack()

text.insert('end', open(filename, 'r').read())
Button(top, text='Quit', command=root.destroy).pack(pady=15)
root.mainloop()

