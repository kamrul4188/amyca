"""
Module Name : display

This module is created to POP-UP display in GUI
"""

from tkinter import *
from tkinter import PhotoImage


class GreetingScreen:
	"""This class is to create greeting pop-up screen to display greeting message"""
	def __init__(self):
		"""Initialize of greeting screen GUI property"""
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
		"""
		This is function to start mainloop of greeting window.
		:return: True
		"""
		self.greeting_window.mainloop()
		return True

	def stop(self):
		"""
		This function is to kill greeting window
		:return: GUI window destroy
		"""
		return self.greeting_window.destroy()


class MessageScreen:
	"""This class is to create a pop-up GUI screen to display message"""
	def __init__(self, title, message):
		"""
		Initialize MessageScreen class to create GUI object
		:param title: message title
		:param message: message to display
		"""
		self.title = title
		self.message = message
		self.output_font = ('Courier New', 12)
		self.message_window = Toplevel()
		self.message_window.title = self.title
		self.message_window.iconphoto(self.message_window, PhotoImage(file='img_title.png'))
		self.message_area = Text(self.message_window)
		self.message_area.pack(padx=5, pady=5, fill='both')
		self.message_area.tag_config('normal_format', font=self.output_font)
		self.update_message_area(self.message)

	def update_message_area(self, message):
		"""
		This function is to update message area on message screen.
		:param message: message to display
		"""
		self.message_area.delete('1.0', END)
		self.message_area.insert(END, message + '\n', 'normal_format')

	def start(self):
		"""
		This function is to call mainloop method to stat gui window.
		:return: mainloop()
		"""
		return self.message_window.mainloop()


if __name__ == '__main__':
	pass
