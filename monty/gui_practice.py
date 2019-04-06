from tkinter import *
import pyfiglet
from colorama import Fore, Back, Style


#create window
window = Tk()
window.title('Hello World')
window.geometry('250x150')

# Create level
banner = pyfiglet.figlet_format('Welcome to AMYCA')
label = Label(window, text=banner)
label.grid(column=0, row=0)

# create a text book
textbox = Entry(window, width=2)
textbox.grid(column=0, row=1)
textbox.insert(0, '2')


def greeting(cls):
	banner = pyfiglet.figlet_format('Welcome to AMYCA')
	print(Fore.MAGENTA + banner)


# define a function to be called when the button is clicked
def button_clicked():
	lavel_value = int(label['text'])
	textbox_value = int(textbox.get())
	label.configure(text=str(lavel_value+textbox_value))


def button_reset():
	label_value = int(label['text'])
	label.configure(text=str(0))


button_ok = Button(window, text='Add', command=button_clicked)
button_ok.grid(column=1, row=1)

button_reset = Button(window, text='Reset', command=button_reset)
button_reset.grid(column=2, row=1)

window.mainloop()