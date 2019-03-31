# Monty weekly project | MD KAMRUZZAMAN | A0107851H
# *************************************************
import os
import csv
import sys

items = []
DATA_FILE = 'monty7.csv'


def print_items():
	if len(items) == 0:
		print('>>> Nothing to list')
	else:
		print(">>> Here is the list of tasks:")
		print('''
==================================================
STATUS |  INDEX  |  DESCRIPTION                
-------------------------------------------------- ''')
		for i, item in enumerate(items):
			if items[i][1]:
				print('  ✓ ' + '  |    ' + str(i + 1) + '    |  ' + items[i][0])
			else:
				print('  ✗ ' + '  |    ' + str(i + 1) + '    |  ' + items[i][0])
		print('--------------------------------------------------')


def add_item(user_input):
	new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
	items.append([new_input, False])  # Added new items to list
	print('>>> Task added to the list')


def delete_item(user_input):
	new_input = user_input.split(' ', 1)[1]
	index = confirm_is_number(new_input) - 1
	if index >= 0:
		del items[index]
		print('>>> Task deleted from the list')
	else:
		raise ValueError('Invalid index')


def done_item(user_input):
	new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
	new_input = confirm_is_number(new_input)  # Return as integer
	new_input = new_input - 1
	if new_input < 0:
		raise ValueError('Index must be greather than 0')
	else:
		try:
			items[new_input][1] = True  # Task complited
			print('>>> Congrats on completing a task! :-)')
		except IndexError:
			raise IndexError('No item at index ' + str(new_input + 1))


def pending_item(user_input):
	new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
	new_input = confirm_is_number(new_input)  # Return as integer
	new_input = new_input - 1
	if new_input < 0:
		raise ValueError('Index must be greather than 0')
	else:
		try:
			items[new_input][1] = False  # Task pending
			print('>>> OK, I have marked that item as pending')
		except IndexError:
			raise IndexError('No item at index ' + str(new_input + 1))


def confirm_is_number(number):
	try:
		number = int(number)
		return number
	except ValueError:
		raise ValueError((str(number) + ' is not a number'))


def terminate():
	print('>>> Are you sure? y/n')
	response = input()
	if response == 'y':
		print(">>> Bye!")
		sys.exit()


def print_greeting():
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


def help_monty():
	need_help = '''
>>> I'm glad you asked. Here it is:
==================================================
Monty can understand the following commands:

add DESCRIPTION 
    Adds a task to the list
    Example: add read book
done INDEX
    Marks the task at INDEX as 'done'
    Example: done 1
exit
    Exits the application
help_info
    Shows the help_info information
list
     Lists the tasks in the list
-------------------------------------------------- 
'''
	print(need_help.strip(), '\n')


def execute_command(command):
	if command == 'exit':
		terminate()
	elif command == 'list':
		print_items()
	elif command.startswith('add '):
		add_item(command)
	elif command.startswith('delete '):
		delete_item(command)
	elif command.startswith('done '):
		done_item(command)
	elif command.startswith('pending '):
		pending_item(command)
	elif command.startswith('help'):
		help_monty()
	else:
		raise ValueError('command not recognized')


def read_command():
	print(">>> What can I do for you?\n")
	read = input()
	read = read.lower()
	read = read.strip()
	read = ' '.join(read.split())
	return read


def load_data(filename):
	data_file = open(filename)
	deliveries_reader = csv.reader(data_file)
	for row in deliveries_reader:
		if not row:
			print('not row')
			continue
		add_item_from_csv_line(row)
	data_file.close()


def add_item_from_csv_line(values):
	status = True if values[1] == 'done' else False
	items.append([values[0], status])  # items is a global variable


def save_data(filename, items):
	data_file = open(DATA_FILE, 'w', newline='')
	output_writer = csv.writer(data_file)
	for item in items:
		if item[1]:
			value = [item[0], 'done']
			output_writer.writerow(value)
		else:
			value = [item[0], 'pending']
			output_writer.writerow(value)
	data_file.close()  # close file


def main():
	load_data(DATA_FILE)  # load task data from the file
	print_greeting()
	while True:
		try:
			command = read_command()
			execute_command(command)
			save_data(DATA_FILE, items)  # save all tasks in the file
		except Exception as e:
			print('>>> SORRY, I could not perform that command. Problem:', e)


main()


