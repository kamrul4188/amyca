from tkinter import *
from tkinter import ttk

root = Tk()

textbox = Text(root, width=60, height=3)
textbox.grid(sticky=(N, S, E, W))

def KeyboardEvent(event):
    if event.keysym_num > 0 and event.keysym_num < 60000:
        print('This is a printable key. The character is: %r keysym: %r' % \
            (event.char, event.keysym_num))
    else:
        print('This key is unprintable. The character is: %r keysym: %r' % \
            (event.char, event.keysym_num))
textbox.bind('<KeyPress>', KeyboardEvent)
root.mainloop()