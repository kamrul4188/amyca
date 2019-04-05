# **************************************************
# Monty weekly project | MD KAMRUZZAMAN | A0107851H
# *************************************************

import os
import csv
import sys

items = []
DATA_FILE = 'monty10.csv'


class ToDo:
	"""This class add todo objdect into items"""

	TYPE_KEY = 'T'

	def __init__(self, description, status):
		self.description = description
		self.is_done = status

	def mark_as_done(self):
		self.is_done = True

	def mark_as_pending(self):
		self.is_done = False

	def as_string(self):
		""" Return the details of todo object as a string"""
		status = '✓' if self.is_done else '✗'
		offset = 30 - len(self.description)
		return status.center(8) + '|'.ljust(3) + self.description + ' '.ljust(offset) + '|'.ljust(3) + '-'

	def __status_as_icon(self):
		""" Return the details of todo object as a string"""
		return '✓' if self.is_done else '✗'

	def __str__(self):
		return '(' + self.__status_as_icon() + ')' + self.description

	@classmethod
	def get_str(cls):
		return cls.__str__()

	def as_csv(self):
		""" Return the details of todo object as a list,
		suitable to be stored in a csv file.
		"""
		return ['T', self.description, 'done' if self.is_done else 'pending']


class Deadline (ToDo):
	"""This class is to add deadline object into items"""
	TYPE_KEY = 'D'

	def __init__(self, description, status, by):
		super().__init__(description, status)
		self.by = by

	def as_string(self):
		""" Return the details of todo object as a string"""
		status = '✓' if self.is_done else '✗'
		offset = 30 - len(self.description)
		return status.center(8) + '|'.ljust(3) + self.description + ' '.ljust(offset) + '|'.ljust(3) + self.by

	def __str__(self):
		return super().__str__() + '[by: ' + self.by + ']'


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

	def __init__(self, storage):
		self.storage = str(storage)

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
				if type(item) == ToDo:
					print(str(i + 1).center(6) + '|' + item.as_string())
				elif type(item) == Deadline:
					print(str(i + 1).center(6) + '|' + item.as_string())
			print('------------------------------------------------------------------')
			return '>>> You can use INDEX as ID to farther operation on particular task'

	def load_data(self):
		data_file = open(self.storage)
		deliveries_reader = csv.reader(data_file)
		for row in deliveries_reader:
			if row[0] == 'T':
				items.append(ToDo(row[1], True if row[2] == 'done' else False))
			elif row[0] == 'D':
				items.append(Deadline(row[1], True if row[2] == 'done' else False, row[3]))
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


def execute_command(command, task_manager, ui):

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
		message = task_manager.add_item(ToDo(description, False))
		ui.display(message)
	elif command.startswith('deadline '):
		command_part = command.split(" ", 1)[1]
		print(command_part)
		description = remove_from_word(command_part, 'by:')
		deadline = remove_to_word(command_part, 'by:')
		print(deadline)
		message = task_manager.add_item(Deadline(description, False, deadline))
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
	storage = StorageManager('data.csv')

	# create a TaskManager object and load data
	task_manager = TaskManager(storage)
	task_manager.load_data()

	while True:
		try:

			command = ui.read_command()
			execute_command(command, task_manager, ui)
			task_manager.save_data()
		except Exception as e:
			ui.display('SORRY, I could not perform that command. Problem:' + str(e))


main()
