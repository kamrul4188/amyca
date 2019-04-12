from tkinter import *
from tkinter import PhotoImage
import time


class GreetingScreen:
	def __init__(self):
		self.greeting_window = Tk()
		self.greeting_window.geometry('500x400')
		self.greeting_window.title('Welcome')
		self.img_title = PhotoImage(file='img_title.png')
		self.greeting_window.iconphoto(self.greeting_window, self.img_title)
		self.img_amyca = Label(self.greeting_window, image=self.img_title)
		self.img_amyca.pack(padx=5, pady=5, fill='x')
		self.heading = Label(self.greeting_window, text='WELCOME TO AMYCA', fg='green', font=('Courier New', 30, 'bold'))
		self.heading.pack(padx=5, pady=5)
		self.sub_heading_text = 'Your Project Management Assistance'
		self.sub_heading = Label(self.greeting_window, text=self.sub_heading_text, fg='orange', font=('Courier New', 16))
		self.sub_heading.pack(padx=5, pady=5)
		self.ok_button = Button(self.greeting_window, text='  OK  ', fg='blue', font=('Courier New', 16), command=self.stop)
		self.ok_button.pack(padx=10, pady=10)

	def start(self):
		self.greeting_window.mainloop()
		return True

	def stop(self):
		return self.greeting_window.destroy()



if __name__ == '__main__':
	GreetingScreen().start()
