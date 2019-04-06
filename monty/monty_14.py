# **************************************************
# Monty weekly project | MD KAMRUZZAMAN | A0107851H
# *************************************************

import os
import csv
import sys
import todo
import deadline
import datetime
from tkinter import *

items = []
DATA_FILE = 'data.csv'


class GUI:

	def __init__(self, task_manager):
		self.task_manager = task_manager
		self.window = Tk()
		self.window.geometry('800x700')  # set Window size
		self.window.title('Monty')  # set Window title

		self.input_box = Entry(self.window)  # create an input box
		self.input_box.pack(padx=5, pady=5, fill='x')  # make the input box fill the width of the Window
		self.input_box.bind('<Return>', self.command_entered)  # bind the command_entered function to the Enter key
		self.input_box.focus()  # set focus to the input box

		# add a text area to show the chat history
		self.history_area = Text(self.window, width="50")
		self.history_area.pack(padx=5, pady=5, side=LEFT, fill="y")
		self.output_font = ('Courier New', 12)
		self.history_area.tag_configure('error_format', foreground='red', font=self.output_font)
		self.history_area.tag_configure('success_format', foreground='green', font=self.output_font)
		self.history_area.tag_configure('normal_format', font=self.output_font)

		# add a text area to show the list of tasks
		self.list_area = Text(self.window)
		self.list_area.pack(padx=5, pady=5, side=RIGHT, fill="both")
		self.list_area.tag_configure('normal_format',  font=self.output_font)
		self.list_area.tag_configure('pending_format', foreground='red', font=self.output_font)
		self.list_area.tag_configure('done_format', foreground='green', font=self.output_font)

		# show the welcome message and the list of tasks
		self.update_chat_history('start', 'Welcome to Monty!', 'success_format')
		self.update_task_list(self.task_manager.items)

	def update_chat_history(self, command, response, status_format):
		"""
		status_format: indicates which color to use for the status message
		  can be 'error_format', 'success_format', or 'normal_format'
		"""
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		self.history_area.insert(1.0, '-' * 40 + '\n', 'normal_format')
		self.history_area.insert(1.0, '>>> ' + response + '\n', status_format)
		self.history_area.insert(1.0, 'You said: ' + command + '\n', 'normal_format')
		self.history_area.insert(1.0, current_time + '\n', 'normal_format')

	def update_task_list(self, tasks):
		self.list_area.delete('1.0', END)  # clear the list area
		for i, task in enumerate(tasks):
			if type(task) == todo.ToDo:
				self.list_area.insert(END, str(i + 1).center(6) + '|' + task.as_string())
			elif type(task) == deadline.Deadline:
				print(str(i + 1).center(6) + '|' + task.as_string())
				self.list_area.insert(END, str(i + 1).center(6) + '|' + task.as_string())
			'''
			if task[1]:
				icon = '✓'
				output_format = 'done_format'
			else:
				icon = '✗'
				output_format = 'pending_format'
			self.list_area.insert(END, icon + ' ' + str(i+1) + ' ' + task[0] + '\n', output_format)
			'''

	def clear_input_box(self):
		self.input_box.delete(0, END)

	def command_entered(self, event):
		command = None
		try:
			command = self.input_box.get()
			if command.strip().lower() == 'exit':
				sys.exit()
			output = self.task_manager.execute_command(command)
			self.update_chat_history(command, output, 'success_format')
			self.update_task_list(self.task_manager.items)
			self.clear_input_box()
		except Exception as e:
			self.update_chat_history(command, str(e) + '\n' + self.task_manager.get_help(), 'error_format')

	def start(self):
		self.window.mainloop()


class UserInterface:
	"""this class used to handle reading input from the user and showing output back to the user"""

	@staticmethod
	def show_greeting():
		banner = '''    
		*******************************************************************************************
		*  __          __  _                            _          __  __             _           *
		*  \ \        / / | |                          | |        |  \/  |           | |          *
		*   \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | \  / | ___  _ __ | |_ _   _   *
		*    \ \/  \/ / _ \ |/ __/ _ \| '_ ' _ \ / _ \ | __/ _ \  | |\/| |/ _ \| '_ \| __| | | |  *
		*     \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |  | | (_) | | | | |_| |_| |  *
		*      \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  |_|\___/|_| |_|\__|\__, |  *
		*                                                                                  __/ |  *
		*                                                                                 |___/   *
		*******************************************************************************************
		'''
		print(banner.strip(), '\n')

	@staticmethod
	def read_command():
		print(">>> What can I do for you?\n")
		read = input()
		read = read.lower()
		read = read.strip()
		read = ' '.join(read.split())
		return read

	@staticmethod
	def display(user_input):
		print(user_input)

	@staticmethod
	def help():
		need_help = '''
	>>> I'm glad you asked. Here it is:
	==================================================
	Monty can understand the following commands:

	todo DESCRIPTION 
		Adds a task to the list
		Example: todo read book

	deadline DESCRIPTION by: DEADLINE
		Adds a task to the list
		Example: deadline read book by: tomorrow

	done INDEX
		Marks the task at INDEX as 'done'
		Example: done 1

	pending INDEX
		Marks the task at INDEX as 'pending'
		Example: pending 1

	exit
		Exits the application

	help_info
		Shows the help_info information

	list
		 Lists the tasks in the list
	-------------------------------------------------- 
	'''
		print(need_help.strip(), '\n')


class StorageManager:
	"""this class used to read data from the data file and write data back to the data file."""
	def __init__(self, file_path):
		self.file_path = file_path

	def __str__(self):
		return self.file_path


class TaskManager:
	"""this class is hold the list of Task/Deadline objects and will execute commands"""

	##self.storage = str(storage)

	def __init__(self, items):
		self.items = items

	def get_help(self):
		return 'help:\n...'

	def execute_command(self, command):

		if command == 'exit':
			sys.exit()
		elif command == 'help':
			self.get_help()
		elif command == 'list':
			message = self.get_items_as_table()
			#ui.display(message)
		elif command.startswith('todo '):
			description = command.split(" ", 1)[1]
			message = self.add_item(todo.ToDo(description, False))
			return message
			#ui.display(message)
		elif command.startswith('deadline '):
			command_part = command.split(" ", 1)[1]
			description = remove_from_word(command_part, 'by:')
			dl = remove_to_word(command_part, 'by:')
			message = self.add_item(deadline.Deadline(description, False, dl))
			#ui.display(message)
		elif command.startswith('done '):
			message = self.done_item(command)
			#ui.display(message)
		elif command.startswith('pending '):
			message = self.pending_item(command)
			#ui.display(message)
		elif command.startswith('delete '):
			message = self.delete_item(command)
			#ui.display(message)
		else:
			return 'command not recognize'

	'''
	def execute_command(self, command):
		if command == 'help':
			return self.get_help()
		elif command.startswith('add '):
			self.items.append([command[4:], False])
			return 'task added'
		else:
			raise Exception('Command not recognized') 
	'''

	@staticmethod
	def add_item(user_input):
		items.append(user_input)
		return '>>> Task added to the list'

	@staticmethod
	def delete_item(user_input):
		new_input = user_input.split(' ', 1)[1]
		index = confirm_is_number(new_input) - 1
		if index >= 0:
			del items[index]
			return '>>> Task deleted from the list'
		else:
			raise ValueError('Invalid index')

	@staticmethod
	def done_item(user_input):
		new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
		new_input = confirm_is_number(new_input)  # Return as integer
		new_input = new_input - 1
		if new_input < 0:
			raise ValueError('Index must be grater than 0')
		else:
			try:
				items[new_input].mark_as_done()  # Task complited
				return '>>> Congrats on completing a task! :-)'
			except IndexError:
				raise IndexError('No item at index ' + str(new_input + 1))

	@staticmethod
	def pending_item(user_input):
		new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
		new_input = confirm_is_number(new_input)  # Return as integer
		new_input = new_input - 1
		if new_input < 0:
			raise ValueError('Index must be greather than 0')
		else:
			try:
				items[new_input].mark_as_pending()  # Task pending
				return '>>> OK, I have marked that item as pending'
			except IndexError:
				raise IndexError('No item at index ' + str(new_input + 1))

	@staticmethod
	def get_items_as_table():
		if len(items) == 0:
			return '>>> Nothing to list'
		else:

			print(">>> Here is the list of tasks:")
			print('==================================================================')
			print('INDEX | STATUS | DESCRIPTION                    | DEADLINE')
			print('------------------------------------------------------------------')
			for i, item in enumerate(items):
				if type(item) == todo.ToDo:
					print(str(i + 1).center(6) + '|' + item.as_string())
				elif type(item) == deadline.Deadline:
					print(str(i + 1).center(6) + '|' + item.as_string())
			print('------------------------------------------------------------------')
			return '>>> You can use INDEX as ID to farther operation on particular task'

	def load_data(self):
		data_file = open(self.storage)
		deliveries_reader = csv.reader(data_file)
		for row in deliveries_reader:
			if row[0] == 'T':
				items.append(todo.ToDo(row[1], True if row[2] == 'done' else False))
			elif row[0] == 'D':
				items.append(deadline.Deadline(row[1], True if row[2] == 'done' else False, row[3]))
		data_file.close()

	def save_data(self):
		output_file = open(self.storage, 'w', newline='')
		output_writer = csv.writer(output_file)
		for item in items:
			output_writer.writerow(item.as_csv())
		output_file.close()


def confirm_is_number(number):
	try:
		number = int(number)
		return number
	except ValueError:
		raise ValueError((str(number) + ' is not a number'))


def remove_from_word(text, word):
	tail_start_position = text.find(word)
	if tail_start_position != -1:
		text = text[:tail_start_position]
		text = text.strip()
		return text
	else:
		raise ValueError('Your command not in correct format')


def remove_to_word(text, word):
	word_size = len(word) + 1  # world length + a space after word
	word_start_position = text.find(word)

	if word_start_position != -1:
		word_tail_position = word_start_position + word_size
		return text[word_tail_position:]
	else:
		raise ValueError('Your command not in correct format')


class Command:

	@staticmethod
	def execute(command, task_manager, ui):

		if command == 'exit':
			ui.display('Bye!')
			sys.exit()
		elif command == 'help':
			ui.help()
		elif command == 'list':
			message = task_manager.get_items_as_table()
			ui.display(message)
		elif command.startswith('todo '):
			description = command.split(" ", 1)[1]
			message = task_manager.add_item(todo.ToDo(description, False))
			ui.display(message)
		elif command.startswith('deadline '):
			command_part = command.split(" ", 1)[1]
			description = remove_from_word(command_part, 'by:')
			dl = remove_to_word(command_part, 'by:')
			message = task_manager.add_item(deadline.Deadline(description, False, dl))
			ui.display(message)
		elif command.startswith('done '):
			message = task_manager.done_item(command)
			ui.display(message)
		elif command.startswith('pending '):
			message = task_manager.pending_item(command)
			ui.display(message)
		elif command.startswith('delete '):
			message = task_manager.delete_item(command)
			ui.display(message)
		else:
			ui.display('Invalid command')


def main():
	# create a UserInterface object and show the greeting
	ui = UserInterface()
	ui.show_greeting()

	# create a StorageManager object
	storage = StorageManager(DATA_FILE)

	# create a TaskManager object and load data
	task_manager = TaskManager(storage)
	task_manager.load_data()

	while True:
		try:

			command = ui.read_command()
			#execute_command(command, task_manager, ui)
			task_manager.save_data()
		except Exception as e:
			ui.display('SORRY, I could not perform that command. Problem:' + str(e))

GUI(TaskManager(items)).start()
