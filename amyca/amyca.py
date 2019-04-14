"""
Amyca is a software is software enginnering project
"""

import datetime
import logging
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import sys
from user import User
from todo import ToDo
from deadline import Deadline
from project import Project
from resource import Resource
from cost import Cost
from display import GreetingScreen
from display import MessageScreen
from storage import StorageManager


class MainScreen:
	"""Main screen display"""
	def __init__(self):
		"""Initialize GUI main window"""

		self.project = Project('p1')
		self.current_user_name = User.get_current_user_name()
		self.current_user_level = User.get_current_user_access_level()
		self.current_time = self.get_current_time()
		self.log_file = 'program_data/amyca.log'


		# self.nus_orange = '#EF7C00'
		# self.nus_blue = '#003D7C'

		self.main_window = Tk()
		self.main_window.geometry('1600x700')  # set window size
		#self.window.attributes('-fullscreen', True) # create full screen
		print(self.current_user_name)
		self.main_window.title('AMYCA - Project Management Assistance' + ' [ Login as : ' + self.current_user_name + ' ]')  # set window title

		#self.window.configure(background=self.nus_blue)
		self.main_window.iconphoto(self.main_window, PhotoImage(file='img_title.png'))

		# Create Frame
		self.header = Frame(self.main_window, height=40)
		self.content= Frame(self.main_window)
		self.footer = Frame(self.main_window, height=20)

		self.header.pack(fill='both')
		self.content.pack(fill='both', expand=True)
		self.footer.pack(fill='both')

		# create menus
		self.menu_bar = Menu(self.main_window)
		self.file_menu = Menu(self.menu_bar, tearoff=0)
		self.user_menu = Menu(self.menu_bar, tearoff=0)
		self.task_menu = Menu(self.menu_bar, tearoff=0)
		self.resource_menu = Menu(self.menu_bar, tearoff=0)
		self.cost_menu = Menu(self.menu_bar, tearoff=0)
		self.help_menu = Menu(self.menu_bar, tearoff=0)


		# Configuration and cascade of menus
		self.menu_bar.add_cascade(label='File', menu=self.file_menu)
		self.menu_bar.add_cascade(label='User', menu=self.user_menu)
		self.menu_bar.add_cascade(label='Task', menu=self.task_menu)
		self.menu_bar.add_cascade(label='Resource', menu=self.resource_menu)
		self.menu_bar.add_cascade(label='Cost', menu=self.cost_menu)
		self.menu_bar.add_cascade(label='Help', menu=self.help_menu)
		self.main_window.config(menu=self.menu_bar)

		# add command to menus	- TODO: need to add commad for fucntioning
		self.file_menu.add_command(label='save', command=self.save_data)
		self.file_menu.add_command(label='Exit', command=self.main_window.destroy)
		self.user_menu.add_command(label='Add User', command=self.add_user)
		self.user_menu.add_command(label='Remove User')
		self.user_menu.add_command(label='Change Passowrd')
		self.user_menu.add_command(label='Change Level')
		self.user_menu.add_command(label='Logout', command=self.logout)
		self.task_menu.add_command(label='Add ToDo')
		self.task_menu.add_command(label='Add Deadline')
		self.task_menu.add_command(label='Add Timeline')
		self.task_menu.add_command(label='Update Status')
		self.task_menu.add_command(label='View Timeline')
		self.task_menu.add_command(label='Delete')
		self.resource_menu.add_command(label='Add Resource')
		self.resource_menu.add_command(label='Remove Resource')
		self.cost_menu.add_command(label='Add cost')
		self.cost_menu.add_command(label='Remove Cost')
		self.help_menu.add_command(label='? Help', command=self.help)
		self.help_menu.add_command(label= 'Log', command=self.get_log)



		# create default font
		self.output_font = ('Courier New', 12)
		self.header_font = ('Courier New', 30)
		self.footer_font = ('Courier New', 10)

		# add Label as header box
		self.header_box = Label(self.header, text='AMYCA - Project Management Assistance',
		                        font=self.header_font) # ('Helvetica', 30)
		self.header_box.pack()

		# add Label as footer box
		self.footer_box = Label(self.footer, text='Copyright © 2019 Amyca | Develop By: Md Kamruzzaman (A0107851),'
		 + ' Abdullah-al-mamun Khan (A0147365Y) and Chia Xiao Hui (A0147375X) | Project: TE3201-Software Engineering | NUS', font=self.footer_font)
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
		self.list_area.tag_configure('title_format', foreground='blue', font=self.output_font)
		self.list_area.tag_configure('line_format', foreground='blue', font=self.output_font)

		# add a Text area to show all resources
		self.resource_area = Text(self.content, width='50')
		self.resource_area.pack(padx=5, pady=5, side=LEFT, fill='y')
		self.resource_area.tag_configure('normal_format', font=self.output_font)
		self.resource_area.tag_configure('title_format', foreground='blue', font=self.output_font)

		# add a Text area to show all cost
		self.cost_area = Text(self.content, width='50')
		self.cost_area.pack(padx=5, pady=5, side=LEFT, fill='both')
		self.cost_area.tag_configure('normal_format', font=self.output_font)
		self.cost_area.tag_configure('total_cost_format', foreground='red', font=self.output_font)
		self.cost_area.tag_configure('title_format', foreground='blue', font=self.output_font)

		# show the welcome message and the list of tasks
		self.start_logging()
		self.load_data()
		self.update_chat_history('start', 'Welcome to AMYCA ! Your project management assistance.', 'success_format')
		self.update_task_list(self.project.tasks)
		self.update_resource_list(self.project.resources)
		self.update_cost_list(self.project.cost)

	def start(self):
		"""This function is for call main loop for starting GUI"""
		self.main_window.mainloop()

	def start_logging(self):
		logging.basicConfig(filename=self.log_file,
		                    format='%(asctime)s %(levelname)-8s %(message)s',
		                    datefmt='%d/%m/%Y %I:%M:%S %p',
		                    filemode='w',
		                    level=logging.INFO)
		logging.info('Start Amyca...')

	def load_data(self):
		self.project.tasks = StorageManager('data/tasks.csv').load_tasks()
		self.project.resources = StorageManager('data/resources.csv').load_resource()
		self.project.cost = StorageManager('data/cost.csv').load_cost()
		logging.info('Load Data')

	def save_data(self):
		StorageManager('data/tasks.csv').save_data(self.project.tasks)
		StorageManager('data/resources.csv').save_data(self.project.resources)
		StorageManager('data/cost.csv').save_data(self.project.cost)
		messagebox.showinfo('Save', 'All data save to directory [ Amyca/Data ]')
		logging.info('Save Data')

	def add_user(self):
		logging.warning('New User Added')
		AddUserScreen().start()

	def logout(self):
		self.main_window.destroy()
		LoginScreen().start()

	def help(self):
		#msg = self.execute_command.__doc__
		logging.info('Help Wanted')
		msg = help(Project)
		MessageScreen('Help', msg).start()


	def get_log(self):
		file = open(self.log_file, 'r').read()
		MessageScreen('Log', file)

	def get_current_time(self):
		self.current_time = datetime.datetime.now().strftime('%H:%M:%S')
		return self.current_time

	def clear_input_box(self):
		"""This function is for clear input box"""
		self.input_box.delete(0, END)

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

		completed_task = 0
		total_task = 0
		self.list_area.insert(END, ' '*12 + 'LIST OF TASKS' + '\n', 'title_format')
		self.list_area.insert(END, '-'*40 + '\n', 'line_format')
		for i, task in enumerate(tasks):
			total_task = i + 1
			if task.get_status():
				output_format = 'done_format'
				completed_task = completed_task + 1
			else:
				output_format = 'pending_format'
			if type(task) == ToDo:
				self.list_area.insert(END, task.get_status_as_icon() + ' ' + str(i+1) + '. ' + task.get_as_string() + '\n', output_format)
			elif type(task) == Deadline:
				self.list_area.insert(END, task.get_status_as_icon() + ' ' + str(i+1) + '. ' + task.get_as_string() + '\n', output_format)
		self.list_area.insert(END, '-'*40 + '\n', 'line_format')
		self.list_area.insert(END, 'Total Tasks    : ' + str(total_task) + '\n', 'normal_format')
		self.list_area.insert(END, 'Completed Task : ' + str(completed_task) + '\n', 'done_format')
		self.list_area.insert(END, 'Pending Task   : ' + str(total_task-completed_task) + '\n', 'pending_format')
		self.list_area.insert(END, '-' * 40 + '\n', 'line_format')

	def update_resource_list(self, resources):
		self.resource_area.delete('1.0', END)
		self.resource_area.insert(END, ' ' * 11 + 'LIST OF RESOURCES' + '\n', 'title_format')
		self.resource_area.insert(END, '-' * 40 + '\n', 'title_format')
		for i, resource in enumerate(resources):
			self.resource_area.insert(END, str(i+1) + '. ' + resource.get_description() + ': ' + resource.get_quantity() + '\n', 'normal_format')
		self.resource_area.insert(END, '-' * 40 + '\n', 'title_format')

	def update_cost_list(self, cost_list):
		self.cost_area.delete('1.0', END)
		self.cost_area.insert(END, ' ' * 11 + 'LIST OF COST' + '\n', 'title_format')
		self.cost_area.insert(END, '-' * 34 + '\n', 'title_format')

		total_cost = 0
		for i, cost in enumerate(cost_list):
			total_cost = total_cost + int(cost.get_cost())
			self.cost_area.insert(END, str(i+1) + '. ' + cost.get_description() + ': ' + '$' + str(cost.get_cost()) + '\n', 'normal_format')
		self.cost_area.insert(END, '-' * 34 + '\n', 'title_format')
		self.cost_area.insert(END, 'Total cost = $' + str(total_cost) + '\n', 'total_cost_format')
		self.cost_area.insert(END, '-' * 34 + '\n', 'title_format')

	def command_entered(self, event):
		command = None

		try:
			command = self.input_box.get()
			command.strip().lower()
			logging.info('Command Entered: ' + str(command))
			output = self.execute_command(command)

			self.update_chat_history(command, output, 'success_format')
			print('print update history')
			self.update_task_list(self.project.tasks)
			self.update_resource_list(self.project.resources)
			self.update_cost_list(self.project.cost)
			self.clear_input_box()

		except Exception as e:
			self.update_chat_history(command, str(e) + '\n', 'error_format')
			messagebox.showerror('Error...!!!', str(e))

	def remove_from_word(self, text, word):
		tail_start_position = text.find(word)
		if tail_start_position != -1:
			text = text[:tail_start_position]
			text = text.strip()
			return text
		else:
			raise ValueError('Your command not in correct format')

	def remove_to_word(self, text, word):
		word_size = len(word) + 1  # world length + a space after word
		word_start_position = text.find(word)
		if word_start_position != -1:
			word_tail_position = word_start_position + word_size
			text = text[word_tail_position:]
			text = text.strip()
			return text
		else:
			raise ValueError('Your command not in correct format')

	def execute_command(self, command):
		"""
		Amyca only accept following command
		Enter [exit] to terminate from Amyca
		"""

		if command == 'exit':
			sys.exit()
		elif command.startswith('todo '):
			description = command.split(' ', 1)[1]
			return self.project.add_task(ToDo(description, False))

		elif command.startswith('deadline '):
			command_part = command.split(' ', 1)[1]
			description = self.remove_from_word(command_part, 'by')
			by = self.remove_to_word(command_part, 'by')
			return self.project.add_task(Deadline(description, False, by))

		elif command.startswith('done '):
			user_index = command.split(' ', 1)[1]
			index = int(user_index) - 1
			if index < 0:
				raise Exception('Index must be grater then 0')
			else:
				try:
					self.project.tasks[index].mark_as_done()
					return 'Congrats on completing a task ! :-)'
				except Exception:
					raise Exception('No item at index ' + str(index + 1))

		elif command.startswith('pending '):
			user_index = command.split(' ', 1)[1]
			index = int(user_index) - 1
			if index < 0:
				raise Exception('Index must be grater than 0')
			else:
				try:
					self.project.tasks[index].mark_as_pending()
					return 'Task mark as pending'
				except Exception:
					raise Exception('No item at index' + str(index + 1))

		elif command.startswith('resource '):
			command_part = command.split(' ', 1)[1]
			description = self.remove_from_word(command_part, 'is')
			quantity = self.remove_to_word(command_part, 'is')
			return self.project.add_resources(Resource(description, quantity))

		elif command.startswith('cost of '):
			command_part = command.split(' ', 2)[2]
			description = self.remove_from_word(command_part, 'is')
			cost = self.remove_to_word(command_part, 'is')
			return self.project.add_cost(Cost(description, cost))

		elif command.startswith('remove '):
			try:
				command_part = command.split(' ', 2)[1]
				command_index = command.split(' ', 2)[2]
				index = int(command_index) - 1
				if 	command_part == 'task':
					return  self.project.remove_task(index)
				elif command_part == 'resource':
					return self.project.remove_resource(index)
				elif command_part == 'cost':
					return self.project.remove_cost(index)
			except Exception:
				raise ValueError('Command format not recognize.\n Command: >>> remove [task/resource/cost] [index]')
		else:
			logging.warning('Command not recognized. Command Entered: %', command)
			raise Exception('Command not recognized')


class LoginScreen:
	def __init__(self):
		self.user = User
		self.login = False

		self.login_window = Tk()
		self.login_window.geometry('300x250')
		self.login_window.title('Login to Amyca')
		self.login_window.iconphoto(self.login_window, PhotoImage(file='img_title.png'))

		# Create a Form label
		self.label = Label(text='Please enter details below to login')
		self.label.pack(padx=10, pady=10)

		self.label_user_name = Label(self.login_window, text='Username *')
		self.label_user_name.pack(padx=5, pady=5)
		self.username_login_entry = Entry(self.login_window)
		self.username_login_entry.pack(padx=5, pady=5)

		self.label_password = Label(self.login_window, text='Password *')
		self.label_password.pack(padx=5, pady=5)
		self.password_login_entry = Entry(self.login_window, show='*')
		self.password_login_entry.pack(padx=5, pady=5)

		self.login_button = Button(self.login_window, text='Login', command=self.verify_user_login)
		self.login_button.pack(padx=5, pady=5)

	def start(self):
		return self.login_window.mainloop()

	def verify_user_login(self):
		user_name = self.username_login_entry.get()
		user_password = self.password_login_entry.get()
		access_login = self.user.verify(user_name, user_password)
		if access_login:
			self.login_success()
		else:
			messagebox.showerror('Login', 'Login not successful')

	def login_success(self):
		self.login_window.destroy()
		greeting = GreetingScreen().start()
		if greeting:
			MainScreen().start() # Todo: Main Screen


class AddUserScreen:
	def __init__(self):
		self.user = User

		self.add_user_window = Toplevel()
		self.add_user_window.geometry('300x300')
		self.add_user_window.title('Add New User')
		self.add_user_window.iconphoto(self.add_user_window, PhotoImage(file='img_title.png'))

		self.label = Label(self.add_user_window, text='Please enter details below to add new user')
		self.label.pack(padx=10, pady=10)

		self.label_user_name = Label(self.add_user_window, text='Username *')
		self.label_user_name.pack(padx=5, pady=5)
		self.entry_user_name = Entry(self.add_user_window)
		self.entry_user_name.pack(padx=5, pady=5)

		self.label_user_password = Label(self.add_user_window, text='Password *')
		self.label_user_password.pack(padx=5, pady=5)
		self.entry_user_password = Entry(self.add_user_window, show='*')
		self.entry_user_password.pack(padx=5, pady=5)

		self.label_user_access_level = Label(self.add_user_window, text='Access Level *')
		self.label_user_access_level.pack(padx=5, pady=5)
		self.entry_user_access_level = Entry(self.add_user_window)
		self.entry_user_access_level.pack(padx=5, pady=5)

		self.add_user_button = Button(self.add_user_window, text='Add User', command=self.add_user)
		self.add_user_button.pack(padx=5, pady=5)


	def add_user(self):
		user_name = self.entry_user_name.get()
		password = self.entry_user_password.get()
		access_level = self.entry_user_access_level.get()
		message = User(user_name, password, access_level)
		self.add_user_window.destroy()
		messagebox.showinfo('User', message)

	def start(self):
		return self.add_user_window.mainloop()





if __name__ == '__main__':
	try:
		#User('admin', 'admin123', 4)
		#User('kamrul', 'kamrul123', 3)
		#GreetingScreen().start()
		#LoginScreen().start()
		MainScreen().start()
		#AddUserScreen().start()



	except Exception as e:
		print('Problem: ', e)
		messagebox.showerror('Error...!!!', str(e))


