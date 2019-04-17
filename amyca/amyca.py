"""
==============================================================================================================
The software is named 'Amyca' is a Project Management Assistance
It has been build as project requirement of TE3201 - Software Engineering of National University of Singapore
==============================================================================================================

Project Naming:
===============
The software to help the project team to run the project smoothly.
As our software is part of the project team as assistance, So we get a lovely Name.
The latin female form of Amicus of Latin Origin: Meaning: Female friend or Friendly, Loving Woman
Form latin Amicus to English Amyca. We have selected name of our software is Amyca
[Amyca - Project Management Assistance]

Basic Functionality:
====================
1. Initially Amyca interface build in text-base than updated Graphical User Interface (GUI).
2. Amyca and storing and retrieving various data type is require to project management. following are:
	eg: todo, deadline, timeline, resource and cost
3. Amyca is not understand natural language but command format most likely as natural and user friendly.
	but user require to follow those strict format. more information you can found on help menu.
	Example: cost of DESCRIPTION is AMOUNT
4. Amyca data stored into hard disk.
	a. Project and user data stored as .csv
	2. Logging data stored as .log
	3. Documentation data stored as .txt

Additional Functionality:
=========================
1. Timeline as graph: User can view all of there timeline task as graph by just clicking TimeLine menu
2. View Calender: User can view calender in monthly view. Pup up in current date by clicking can be view as needed.
3. Multiple Users: Multiple users is support by Amyca. Amyca has four user access levels.
	a. Team Member: Access Level = 1
	b. Team Leader: Access Level = 2
	c. Project Manager: Access Level = 3
	d. System Admin: Access Level = 4
4. Password: Amyca has posword policy to stored password not understandable by users.
	a. Minimum length of password is 6. Amyca not add user with below minimum length.
	b. Stored user particular into hard disk with password as hash (encrypted)

"""
import datetime
import logging
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
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
from timeline import TimeLine
from my_calendare import CalendarScreen


class MainScreen:
	"""
	The class MainScreen si Main user interface.
	All project tasks, resources and cost viable as main screen.
	Added menu bar with addition functionality as require by project
		eg:  file, user, TimeLine, Calender, Help, and Amyca
	"""
	def __init__(self):
		"""Initialize GUI main window"""
		self.project = Project('p1')
		self.users_list = User.get_users()
		self.current_user_name = User.get_current_user_name()
		self.current_user_level = int(User.get_current_user_access_level())
		self.current_time = self.get_current_time()
		self.log_file = 'program_data/amyca.log'
		self.help_file = 'program_data/help.txt'
		self.about_developer_file = 'program_data/about_developer.txt'
		self.about_amyca_file = 'program_data/about_amyca.txt'
		self.users_file = 'program_data/users.csv'

		# Create root window
		self.main_window = Tk()
		self.width = self.main_window.winfo_screenwidth()
		self.height = self.main_window.winfo_screenheight()
		self.main_window.geometry(('%dx%d')%((self.width, self.height)))
		self.main_window.title('AMYCA - Project Management Assistance' + ' [ Login as : ' + self.current_user_name + ' ]')
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
		self.calendar_menu = Menu(self.menu_bar, tearoff=0)
		self.timeline_menu = Menu(self.menu_bar, tearoff=0)
		self.help_menu = Menu(self.menu_bar, tearoff=0)
		self.amyca_menu = Menu(self.menu_bar, tearoff=0)

		# Configuration and cascade of menus
		self.menu_bar.add_cascade(label='File', menu=self.file_menu)
		self.menu_bar.add_cascade(label='User', menu=self.user_menu)
		self.menu_bar.add_cascade(label='TimeLine', menu=self.timeline_menu)
		self.menu_bar.add_cascade(label='Calendar', menu=self.calendar_menu)
		self.menu_bar.add_cascade(label='Help', menu=self.help_menu)
		self.menu_bar.add_cascade(label='Amyca', menu=self.amyca_menu)
		self.main_window.config(menu=self.menu_bar)

		# Add command into menu
		self.file_menu.add_command(label='save', command=self.save_data)
		self.file_menu.add_command(label='Exit', command=self.main_window.destroy)
		self.user_menu.add_command(label='Add User', command=self.add_user)
		self.user_menu.add_command(label='Remove User', command=self.remove_user)
		self.user_menu.add_command(label='Change Passowrd', command=self.change_password)
		self.user_menu.add_command(label='Logout', command=self.logout)
		self.timeline_menu.add_command(label='Show Graph', command=self.get_timeline_graph)
		self.calendar_menu.add_command(label='Calendar(month)', command=self.get_calendar)
		self.help_menu.add_command(label='? Help', command=self.help)
		self.help_menu.add_command(label= 'Log', command=self.get_log)
		self.amyca_menu.add_command(label='About developer', command=self.get_about_developer)
		self.amyca_menu.add_command(label='About Amyca', command=self.get_about_amyca)

		# create default font
		self.output_font = ('Courier New', 12)
		self.header_font = ('Courier New', 30)
		self.footer_font = ('Courier New', 10)

		# add Label on header box
		self.header_box = Label(self.header,
		                        text='AMYCA - Project Management Assistance',
		                        font=self.header_font)
		self.header_box.pack()

		# add Label on footer box
		self.footer_box = Label(self.footer,
		                        text='Copyright © 2019 Amyca | Develop By: Md Kamruzzaman (A0107851),'
		                             + ' Abdullah-al-mamun Khan (A0147365Y) and Chia Xiao Hui (A0147375X) | '
		                               'Project: TE3201-Software Engineering | NUS', font=self.footer_font)
		self.footer_box.pack()

		# add a Entry as input_box to enter command
		self.input_box = Entry(self.content)
		self.input_box.pack(padx=5, pady=5, fill='x')
		self.input_box.bind('<Return>', self.command_entered)
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
		"""This function is initial configuration of logging module"""
		logging.basicConfig(filename=self.log_file,
		                    format='%(asctime)s %(levelname)-8s %(message)s',
		                    datefmt='%d/%m/%Y %I:%M:%S %p',
		                    filemode='a',
		                    level=logging.INFO)
		logging.info('Amyca Start')

	def load_data(self):
		"""This function called during runtime to load project date from hard disk to project list """
		self.project.tasks = StorageManager('data/tasks.csv').load_tasks()
		self.project.resources = StorageManager('data/resources.csv').load_resource()
		self.project.cost = StorageManager('data/cost.csv').load_cost()
		logging.info('Data loaded')

	def save_data(self):
		"""This function to save project data form project list to hard dive"""
		StorageManager('data/tasks.csv').save_data(self.project.tasks)
		StorageManager('data/resources.csv').save_data(self.project.resources)
		StorageManager('data/cost.csv').save_data(self.project.cost)
		User.save_as_csv(self.users_file)
		messagebox.showinfo('Save', 'All data save to directory [ Amyca/Data ]')
		logging.info('Save data to hard disk to back up')

	def add_user(self):
		"""This function to add user to amyca"""
		if self.current_user_level == 4:  # condition: Only admin to add user
			AddUserScreen(self.project).start()
		else:
			messagebox.showwarning('Add User', 'Only admin can add user')

	def remove_user(self):
		if self.current_user_level == 4:  # Condition: Only admin to remove user
			RemoveUserScreen().start()
		else:
			messagebox.showwarning('Remove User','Only admin can add user')

	def change_password(self):
		if self.current_user_level == 4:  # Condition: Only admin to change password
			ChangePasswordScreen().start()
		else:
			messagebox.showwarning('Change Password', 'Only Admin can password')

	def logout(self):
		"""
		This function is called at Menu bar>User>Logout button click
		To execute: destroy current and window and pop up login window
		Registered user only can login to access Amyca
		"""
		self.save_data()
		logging.warning('User [' + str(self.current_user_name) + '] logout')
		self.main_window.destroy()
		LoginScreen().start()

	def get_calendar(self):
		"""This function is to view calendar"""
		CalendarScreen().start()

	def get_timeline_graph(self):
		"""
		This function to call for display timeline object as graph
		timeline object is a task with start and end date of task
		"""
		task_id = []
		duration = []
		timeline_task = []

		def duration_datetime(start_date, end_date):
			"""
			This function is to calculate duration between start and end date
			:param start_date: Starting date of timeline object
			:param end_date: End date of timeline object
			:return: Duration
			"""
			try:
				if end_date >= start_date:
					duration = end_date - start_date
					duration = str(duration).split(',', 1)[0]
					return duration
				else:
					return 'Your end date ims earlier than start'
			except ValueError:
				raise ValueError('Format of your input ins not detetime')

		for i, task in enumerate(self.project.tasks):
			if type(task) == TimeLine:
				timeline_task.append(task)  # append timeline task from the task list

		if len(timeline_task) == 0:
			messagebox.showinfo('Timeline',  'Nothing to show on time-line')
		else:
			for i, task in enumerate(timeline_task):
				index_id = 'Task ID : ' + str(i + 1)
				task_id.append(index_id)
				start_date = task.get_start_date()
				end_date = task.get_end_date()
				task_duration = duration_datetime(start_date, end_date)
				task_duration = str(task_duration).split(' ', 1)[0]
				duration.append(int(task_duration))
			x_pos = np.arange(len(task_id))
			plt.barh(x_pos, duration, align='center', alpha=0.5)
			plt.yticks(x_pos, task_id)
			plt.xlabel('days')
			plt.title('Tasks Time Line')
			plt.show()

	def help(self):
		"""This function is call to show/display help info"""
		file = open(self.help_file, 'r').read()
		MessageScreen('Help', file).start()

	def get_log(self):
		"""
		This function is called to display logging.
		Open log file form hard disk as read only mode.
		File stored in hard disk as .log format
		"""
		file = open(self.log_file, 'r').read()
		MessageScreen('Log', file).start()

	def get_about_developer(self):
		"""
		This function is call to display developer personal and contract information.
		File stored in hard disk as .txt format
		"""
		file = open(self.about_developer_file, 'r').read()
		MessageScreen('About Developer', file)

	def get_about_amyca(self):
		"""
		This function is call to display software information
		File stored in .txt format. and open file as read mode
		"""
		file = open(self.about_amyca_file, 'r').read()
		MessageScreen('About Amyca', file)

	def get_current_time(self):
		"""
		This function is to get current time as datetime format
		:return: current time
		"""
		self.current_time = datetime.datetime.now().strftime('%H:%M:%S')
		return self.current_time

	def clear_input_box(self):
		"""This function is for clear input box"""
		self.input_box.delete(0, END)

	def update_chat_history(self, command, response, status_format):
		"""
		This function is update chat history and display with following parameter
		:param command: command entered by user in command window
		:param response: return response form execute function
		:param status_format: tag: normal_format, success_format, error_format.
		"""
		current_time = datetime.datetime.now().strftime('%H:%M:%S')
		self.history_area.insert(1.0, '-'*40 + '\n', 'normal_format')
		self.history_area.insert(1.0, '>>> ' + response + '\n', status_format)
		self.history_area.insert(1.0, 'You said: ' + command + '\n', 'normal_format')
		self.history_area.insert(1.0, current_time + '\n', 'normal_format')

	def update_task_list(self, tasks):
		"""
		This function is to update task list into display  as string
		:param tasks: Project task list
		"""
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
			elif type(task) == TimeLine:
				self.list_area.insert(END, task.get_status_as_icon() + ' ' + str(i+1) + '. ' + task.get_as_string() + '\n', output_format)
		self.list_area.insert(END, '-'*40 + '\n', 'line_format')
		self.list_area.insert(END, 'Total Tasks    : ' + str(total_task) + '\n', 'normal_format')
		self.list_area.insert(END, 'Completed Task : ' + str(completed_task) + '\n', 'done_format')
		self.list_area.insert(END, 'Pending Task   : ' + str(total_task-completed_task) + '\n', 'pending_format')
		self.list_area.insert(END, '-' * 40 + '\n', 'line_format')

	def update_resource_list(self, resources):
		"""
		This function is to update project resources list into display as string
		:param resources: project resources
		"""
		self.resource_area.delete('1.0', END)
		self.resource_area.insert(END, ' ' * 11 + 'LIST OF RESOURCES' + '\n', 'title_format')
		self.resource_area.insert(END, '-' * 40 + '\n', 'title_format')
		for i, resource in enumerate(resources):
			self.resource_area.insert(END, str(i+1) + '. ' + resource.get_description() + ': ' + resource.get_quantity() + '\n', 'normal_format')
		self.resource_area.insert(END, '-' * 40 + '\n', 'title_format')

	def update_cost_list(self, cost_list):
		"""
		This function is to update project cost list into display as string
		:param cost_list: project cost list
		"""
		self.cost_area.delete('1.0', END)
		if self.current_user_level >= 3:
			self.cost_area.insert(END, ' ' * 11 + 'LIST OF COST' + '\n', 'title_format')
			self.cost_area.insert(END, '-' * 34 + '\n', 'title_format')

			total_cost = 0
			for i, cost in enumerate(cost_list):
				total_cost = total_cost + int(cost.get_cost())
				self.cost_area.insert(END, str(i+1) + '. ' + cost.get_description() + ': ' + '$' + str(cost.get_cost()) + '\n', 'normal_format')
			self.cost_area.insert(END, '-' * 34 + '\n', 'title_format')
			self.cost_area.insert(END, 'Total cost = $' + str(total_cost) + '\n', 'total_cost_format')
			self.cost_area.insert(END, '-' * 34 + '\n', 'title_format')
		else:
			self.cost_area.insert(END, 'Only Manager and above can view and update cost', '\n')

	def command_entered(self, event):
		"""
		This function is event interrupt function.
		At command enter window press enter to call this function
		:param event: command
		"""
		command = None

		try:
			command = self.input_box.get()
			command.strip().lower()
			logging.info('Command Entered: ' + str(command))
			output = self.execute_command(command)

			self.update_chat_history(command, output, 'success_format')
			self.update_task_list(self.project.tasks)
			self.update_resource_list(self.project.resources)
			self.update_cost_list(self.project.cost)
			self.clear_input_box()

		except Exception as e:
			self.update_chat_history(command, str(e) + '\n', 'error_format')
			messagebox.showerror('Error...!!!', str(e))

	def remove_from_word(self, text, word):
		"""
		This function is to break a string by key word
		:param text: Input string to be break
		:param word: Key word to break the string
		:return: first part of string
		"""
		tail_start_position = text.find(word)
		if tail_start_position != -1:
			text = text[:tail_start_position]
			text = text.strip()
			return text
		else:
			raise ValueError('Your command not in correct format')

	def remove_to_word(self, text, word):
		"""
		This function is to break the string by key word
		:param text: input string to be break
		:param word: last part of the string
		:return:
		"""
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
		This function is to execute the command entered
		Do pre processing before call the execution function is need
		:param command: Command entered
		:return: value form execute function
		"""
		if command == 'exit':
			sys.exit()
		elif command.startswith('todo '):
			if self.current_user_level >= 2:
				"""Team leader and above is access to add task"""
				description = command.split(' ', 1)[1]
				return self.project.add_task(ToDo(description, False))
			else:
				raise ValueError('Team leader or above only can add task')

		elif command.startswith('deadline '):
			if self.current_user_level >= 2:
				"""Team leader and above is access to add task"""
				command_part = command.split(' ', 1)[1]
				description = self.remove_from_word(command_part, 'by')
				by = self.remove_to_word(command_part, 'by')
				return self.project.add_task(Deadline(description, False, by))
			else:
				raise ValueError('Team leader or above only can add task')

		elif command.startswith('timeline '):
			if self.current_user_level >= 2:
				"""Team leader and above is access to add task"""
				command_part = command.split(' ', 1)[1]
				description = self.remove_from_word(command_part, 'from')
				date = self.remove_to_word(command_part, 'from')
				start_date = self.remove_from_word(date, 'to')
				end_date = self.remove_to_word(date, 'to')
				return self.project.add_task(TimeLine(description, False, start_date, end_date))
			else:
				raise ValueError('Team leader or above only can add task')

		elif command.startswith('done '):
			if self.current_user_level >= 2:
				"""Team leader and above is access to update task"""
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
			else:
				raise ValueError('Team leader or above only can add task')

		elif command.startswith('pending '):
			if self.current_user_level >= 2:
				"""Team leader and above is access to update task"""
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
			else:
				raise ValueError('Team leader or above only can add task')

		elif command.startswith('resource '):
			if self.current_user_level >= 2:
				"""Team leader and above is access to add resource"""
				command_part = command.split(' ', 1)[1]
				description = self.remove_from_word(command_part, 'is')
				quantity = self.remove_to_word(command_part, 'is')
				return self.project.add_resources(Resource(description, quantity))
			else:
				raise ValueError('Team leader or above only can add task')

		elif command.startswith('cost of '):
			if self.current_user_level >= 3:
				"""Manager and above is access to add cost"""
				command_part = command.split(' ', 2)[2]
				description = self.remove_from_word(command_part, 'is')
				cost = self.remove_to_word(command_part, 'is')
				return self.project.add_cost(Cost(description, cost))
			else:
				raise ValueError('Manager and above only can add cost')

		elif command.startswith('remove '):
			try:
				command_part = command.split(' ', 2)[1]
				command_index = command.split(' ', 2)[2]
				index = int(command_index) - 1
				if 	command_part == 'task':
					if self.current_user_level >= 2:
						"""Team leader and above to access to remove task"""
						return self.project.remove_task(index)
					else:
						raise ValueError('Team leader and above only can remove task')
				elif command_part == 'resource':
					if self.current_user_level >= 2:
						"""Team Leader and above to access to remove resource"""
						return self.project.remove_resource(index)
					else:
						raise ValueError('Team leader and above only can remove resource')
				elif command_part == 'cost':
					if self.current_user_level >= 3:
						"""Manager and above to access to remove cost"""
						return self.project.remove_cost(index)
					else:
						raise ValueError('Manager adn above only remove cost')
			except Exception:
				raise ValueError('Command format not recognize.\n Command: >>> remove [task/resource/cost] [index]')
		else:
			logging.error('Command not recognized.')
			raise Exception('Command not recognized')


class LoginScreen:
	"""This is for GUI window for user login"""
	def __init__(self):
		"""Initialize Login GUI window"""
		self.user = User
		self.login = False

		self.login_window = Tk()
		self.login_window.geometry('300x250')
		self.login_window.title('Login to Amyca')
		self.login_window.iconphoto(self.login_window, PhotoImage(file='img_title.png'))

		# Create a Form label
		self.label = Label(text='Please enter details below to login')
		self.label.pack(padx=10, pady=10)

		# Create label and entry for user name
		self.label_user_name = Label(self.login_window, text='Username *')
		self.label_user_name.pack(padx=5, pady=5)
		self.username_login_entry = Entry(self.login_window)
		self.username_login_entry.pack(padx=5, pady=5)

		# Create label and entry for user password
		self.label_password = Label(self.login_window, text='Password *')
		self.label_password.pack(padx=5, pady=5)
		self.password_login_entry = Entry(self.login_window, show='*')
		self.password_login_entry.pack(padx=5, pady=5)

		self.login_button = Button(self.login_window, text='Login', command=self.verify_user_login)
		self.login_button.pack(padx=5, pady=5)

	def start(self):
		"""This function is for call mainloop for starting GUI"""
		return self.login_window.mainloop()

	def verify_user_login(self):
		"""Tins function is to verify valid user in registered in database"""
		user_name = self.username_login_entry.get()
		user_password = self.password_login_entry.get()
		access_login = self.user.verify(user_name, user_password)
		if access_login:
			self.login_success()
		else:
			messagebox.showerror('Login', 'Login not successful')

	def login_success(self):
		"""
		This function is call after get successfully verify a valid users
		This function will kil login window screed and call welcome/greeting window
		Get ack form greeting window to start MainScreen window
		"""
		self.login_window.destroy()
		greeting = GreetingScreen().start()
		if greeting:
			MainScreen().start()


class AddUserScreen:
	"""This class is as GUI to add new user"""
	def __init__(self, project):
		"""Initialize add user screen GUI window"""
		self.user = User
		self.project = project

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
		"""Ths function is to execute user object"""
		user_name = self.entry_user_name.get()
		password = self.entry_user_password.get()
		access_level = self.entry_user_access_level.get()
		message = User(user_name, password, access_level)
		self.add_user_window.destroy()
		logging.warning(message)
		messagebox.showwarning('User', message)

	def start(self):
		"""This function is for call mainloop for starting GUI"""
		return self.add_user_window.mainloop()


class RemoveUserScreen:
	"""This class is a GUI to remove user"""
	def __init__(self):
		self.user = User

		self.remove_user_window = Toplevel()
		self.remove_user_window.geometry('300x230')
		self.remove_user_window.title('Remove User')
		self.remove_user_window.iconphoto(self.remove_user_window, PhotoImage(file='img_title.png'))

		self.label = Label(self.remove_user_window, text='Please enter details below to remove user')
		self.label.pack(padx=5, pady=5)

		self.label_user_name = Label(self.remove_user_window, text='Username *')
		self.label_user_name.pack(padx=5, pady=5)
		self.entry_user_name = Entry(self.remove_user_window)
		self.entry_user_name.pack(padx=5, pady=5)

		self.label_user_password = Label(self.remove_user_window, text='Password *')
		self.label_user_password.pack(padx=5, pady=5)
		self.entry_user_password = Entry(self.remove_user_window, show='*')
		self.entry_user_password.pack(padx=5, pady=5)

		self.remove_user_button = Button(self.remove_user_window, text=' Remove User ', command=self.remove_user)
		self.remove_user_button.pack(padx=10, pady=10)

	def remove_user(self):
		"""This function is called user remove method"""
		user_name = self.entry_user_name.get()
		user_password = self.entry_user_password.get()
		message = User.remove(user_name, user_password)
		logging.warning(message)
		messagebox.showwarning('User', message)

	def start(self):
		"""This function is for call mainloop for starting GUI"""
		return self.remove_user_window.mainloop()


class ChangePasswordScreen:
	"""This cass is GUI to change password"""
	def __init__(self):
		self.user = User

		self.change_password_window = Toplevel()
		self.change_password_window.geometry('300x300')
		self.change_password_window.title('Change Password')
		self.change_password_window.iconphoto(self.change_password_window, PhotoImage(file='img_title.png'))

		self.label = Label(self.change_password_window, text='Please enter details below to change password')
		self.label.pack(padx=5, pady=5)

		self.label_user_name = Label(self.change_password_window, text='Username *')
		self.label_user_name.pack(padx=5, pady=5)
		self.entry_user_name = Entry(self.change_password_window)
		self.entry_user_name.pack(padx=5, pady=5)

		self.label_user_password = Label(self.change_password_window, text='Password *')
		self.label_user_password.pack(padx=5, pady=5)
		self.entry_user_password = Entry(self.change_password_window, show='*')
		self.entry_user_password.pack(padx=5, pady=5)

		self.label_new_password = Label(self.change_password_window, text='New Password *')
		self.label_new_password.pack(padx=5, pady=5)
		self.entry_new_password = Entry(self.change_password_window, show='*')
		self.entry_new_password.pack(padx=5, pady=5)

		self.change_password_button = Button(self.change_password_window, text=' Change Password ', command=self.change_password)
		self.change_password_button.pack(padx=10, pady=10)

	def change_password(self):
		"""This function call user to change password method"""
		user_name = self.entry_user_name.get()
		current_password = self.entry_user_password.get()
		new_password = self.entry_new_password.get()
		message = User.change_password(user_name, current_password, new_password)
		logging.warning(message)
		messagebox.showwarning('User', message)

	def start(self):
		"""This function is for call mainloop for starting GUI"""
		return self.change_password_window.mainloop()


if __name__ == '__main__':
	"""
	This is called main. When reun this module the executable module run as name main
	Here is this th begain of Amyca runtime.  
	"""
	try:
		User('admin', 'admin123', 4)  # Create default user admin
		user_file = 'program_data/users.csv'
		User.load_form_csv(user_file) # load user database
		LoginScreen().start()  # Start Amyca loging window to began

	except Exception as e:
		messagebox.showerror('Error...!!!', str(e))
