import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage

import sys


class GUI:

	def __init__(self, tasks):
		"""Initialize GUI main window"""

		self.tasks = tasks
		self.resources = [['Manpower', 50], ['Aircon', 2]]  # Todo: Need to add project resource
		self.cost_list = [['Manpower', 2000], ['Equipment', 5000]]  # Todo: Need to add project cost
		self.current_time = 0
		self.nus_orange = '#EF7C00'
		self.nus_blue = '#003D7C'

		self.window = Tk()
		#self.window.geometry('1600x700')  # set window size
		self.window.attributes('-fullscreen', True) # create full screen
		self.window.title('AMYCA - Your Project Management Assistance')  # set window title
		#self.window.configure(background=self.nus_blue)
		self.window.iconphoto(self.window, PhotoImage(file='title_image.png'))

		# Create Frame
		self.header = Frame(self.window, height=40)
		self.content= Frame(self.window)
		self.footer = Frame(self.window, height=20)

		self.header.pack(fill='both')
		self.content.pack(fill='both', expand=True)
		self.footer.pack(fill='both')

		'''
		self.window.columnconfigure(0, weight=1)
		self.window.rowconfigure(0, weight=1)
		self.window.rowconfigure(1, weight=25)
		self.window.rowconfigure(2, weight=1)

		self.header.grid(row=0, sticky='news')
		self.content.grid(row=1, sticky='news')
		self.footer.grid(row=2, sticky='news')
        '''

		# create menu
		self.menu_bar = Menu(self.window)
		self.file_menu = Menu(self.menu_bar, tearoff=0) # add file menu
		self.file_menu.add_command(label='Exit', command=self.window.destroy)
		self.help_menu = Menu(self.menu_bar, tearoff=0)
		self.help_menu.add_command(label='Help', command=self.help)

		self.menu_bar.add_cascade(label='File', menu=self.file_menu)
		self.menu_bar.add_cascade(label='Help', menu=self.help_menu)
		self.window.config(menu=self.menu_bar)

		# create default font
		self.output_font = ('Courier New', 12)
		self.header_font = ('Courier New', 30)
		self.footer_font = ('Courier New', 10)

		# add Label as header box
		self.header_box = Label(self.header, text='AMYCA - Project Management Assistance',
		                        font=self.header_font) # ('Helvetica', 30)
		self.header_box.pack()

		# add Label as footer box
		self.footer_box = Label(self.footer, text='Copyright © 2019 Amyca | Develop By: Md Kamruzzaman(A0107851),'
		 + ' Abdullah-al-mamun(Axxxxx) and Xai (Axxxx) | Project: TE3201-Software Engineering', font=self.footer_font)
		self.footer_box.pack()

		# add a Entry as input_box to enter command
		self.input_box = Entry(self.content)  # create input box
		self.input_box.pack(padx=5, pady=5, fill='x')
		self.input_box.bind('<Return>', self.command_entered)  # bind the command_entered function to the Enter key
		self.input_box.focus()

		# add a Text area to show chat history
		self.history_area = Text(self.content, width='50')
		self.history_area.pack(padx=5, pady=5, side=LEFT, fill='y')
		self.history_area.tag_configure('normal_format', font=self.output_font)
		self.history_area.tag_configure('success_format', foreground='green', font=self.output_font)
		self.history_area.tag_configure('error_format', foreground='red', font=self.output_font)

		# add a Text area to show list of tasks
		self.list_area = Text(self.content, width='50')
		self.list_area.pack(padx=5, pady=5, side=LEFT, fill='y')
		self.list_area.tag_configure('normal_format', font=self.output_font)
		self.list_area.tag_configure('pending_format', foreground='red', font=self.output_font)
		self.list_area.tag_configure('done_format', foreground='green', font=self.output_font)

		# add a Text area to show all resources
		self.resource_area = Text(self.content, width='50')
		self.resource_area.pack(padx=5, pady=5, side=LEFT, fill='y')
		self.resource_area.tag_configure('normal_format', font=self.output_font)

		# add a Text area to show all cost
		self.cost_area = Text(self.content, width='50')
		self.cost_area.pack(padx=5, pady=5, side=LEFT, fill='both')
		self.cost_area.tag_configure('normal_format', font=self.output_font)
		self.cost_area.tag_configure('total_cost_format', foreground='red', font=self.output_font)

		# show the welcome message and the list of tasks
		self.update_chat_history('start', 'Welcome to AMYCA ! Your project management assistance.', 'success_format')
		self.update_task_list(self.tasks)
		self.update_resource_list(self.resources)
		self.update_cost_list(self.cost_list)

	def start(self):
		"""This function is for call main loop for starting GUI"""
		self.window.mainloop()

	def clear_input_box(self):
		"""This function is for clear input box"""
		self.input_box.delete(0, END)

	def get_current_time(self):
		self.current_time = datetime.datetime.now().strftime('%H:%M:%S')
		return self.current_time

	def update_chat_history(self, command, response, status_format):
		"""

		:param command:
		:param response:
		:param status_format: indicates which color to use for the status message. eg 'normal_format', 'error_format' or 'success_format'
		:return:
		"""
		current_time = datetime.datetime.now().strftime('%H:%M:%S')
		self.history_area.insert(1.0, '-'*40 + '\n', 'normal_format')
		self.history_area.insert(1.0, '>>> ' + response + '\n', status_format)
		self.history_area.insert(1.0, 'You said: ' + command + '\n', 'normal_format')
		self.history_area.insert(1.0, current_time + '\n', 'normal_format')

	def update_task_list(self, tasks):
		self.list_area.delete('1.0', END)  # Clear the list area
		for i, task in enumerate(tasks):
			if task[1]:
				icon = '✓'
				output_format = 'done_format'
			else:
				icon = '✗'
				output_format = 'pending_format'
			self.list_area.insert(END, icon + ' ' + str(i+1) + '. ' + task[0] + '\n', output_format)

	def update_resource_list(self, resources):
		self.resource_area.delete('1.0', END)
		for i, resource in enumerate(resources):
			self.resource_area.insert(END, str(i+1) + '. ' + resource[0] + ' = ' + str(resource[1]) + ' pcs' + '\n', 'normal_format')
			# Todo: Need to update as per project resource

	def update_cost_list(self, cost_list):
		self.cost_area.delete('1.0', END) # Todo: Need to ask prof what is mean by '1.0' and END
		total_cost = 0
		for i, cost in enumerate(cost_list):
			total_cost = total_cost + cost[1]
			self.cost_area.insert(END, str(i+1) + '. ' + cost[0] + ' = $' + str(cost[1]) + '\n', 'normal_format')
		self.cost_area.insert(END, '-'*25 + '\n', 'normal_format')
		self.cost_area.insert(END, 'Total cost = $' + str(total_cost) + '\n', 'total_cost_format')

	def command_entered(self, event):
		command = None
		try:
			command = self.input_box.get()
			if command.strip().lower() == 'exit':
				sys.exit()
			# Todo: Need to complete this [output = self.task_manager.execute.command(command)]
			self.tasks.append([command, False])
			output = 'Task added'
			self.update_chat_history(command, output, 'success_format')
			self.update_task_list(self.tasks)
			self.clear_input_box()

		except Exception as e:
			self.update_chat_history(command, str(e) + '\n', 'error_format')
			messagebox.showerror('Error...!!!', str(e))

	def help(self):
		messagebox.showinfo('Help', 'I am amyca to help you')  # Todo: Need to impliment help function


if __name__ == '__main__':
	tasks = []
	tasks.append(['read book', False])
	tasks.append(['Return book', True])


	try :
		GUI(tasks).start()
	except Exception as e:
		print('Problem: ', e)
		messagebox.showerror('Error...!!!', str(e))


