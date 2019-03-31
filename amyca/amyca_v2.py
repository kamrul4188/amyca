import sys
import pyfiglet
from colorama import init;
import user


init(autoreset=True)
from colorama import Fore, Back, Style


class Project:
	def __init__(self, name):
		self.name = name
		self.task = []


class Confirmed:

	@classmethod
	def number(cls, number):
		try:
			number = int(number)
			return number
		except ValueError:
			raise ValueError(str(number) + ' not a number')


class DisplayManager:

	@classmethod
	def greeting(cls):
		banner = pyfiglet.figlet_format('Welcome to AMYCA')
		print(Fore.MAGENTA + banner)

	@classmethod
	def help(cls):
		pass

	# TODO: add all command instruction with example

	@classmethod
	def users(cls):
		pass
	# TODO: add functionality to print user info


class Process:

	@classmethod
	def login(cls):
		while True:
			try:
				user_input = input(Fore.LIGHTGREEN_EX + '>>> Please enter username and pwd: ')
				user_name = user_input.split(' ', 1)[0]
				user_password = user_input.split(' ', 1)[1]
				if user.User.verify(user_name, user_password):
					break
				else:
					print(Fore.RED + 'Error: username or pwd in incorrect. Please try again...!!!')
					continue
			except IndexError:
				print(Fore.RED + 'Invalid user input. Please try again...!!! ')
				continue

	@classmethod
	def logout(cls):
		print(Back.LIGHTCYAN_EX + 'You have successfully logout as ' + user.User.get_current_user_name())
		main()

	@classmethod
	def terminate(cls):
		print('>>> Are you sure? y/n')
		response = input()
		if response.lower() == 'y':
			print(pyfiglet.figlet_format('>>> Bye!', font='digital'))
			sys.exit()
		elif response.lower() == 'n':
			print(pyfiglet.figlet_format('Welcome back !', font='digital'))

		else:
			raise ValueError('Invalid input')

	@classmethod
	def add_user(cls, user_input):
		"""
		:param user_input: add user [user_name] [user_password] [user_access_level]
		:return: null
		"""
		if user.User.get_current_user_access_level() == 4:
			try:
				name = user_input.split(' ', 5)[2]
				password = user_input.split(' ', 5)[3]
				level = user_input.split(' ', 5)[4]
				user.User(name, password, level)
				msg_1 = Back.LIGHTYELLOW_EX + ' A user has  been added as ' + Back.LIGHTYELLOW_EX + Fore.RED + name
				msg_2 = Back.LIGHTYELLOW_EX + ' with level of access is : ' + Back.LIGHTYELLOW_EX + Fore.RED + str(
					level) + ' '
				print(msg_1 + msg_2)
			except IndexError:
				raise IndexError('Invalid input...!!!. Please use AMYCA CLI.')
		else:
			raise ValueError('Only admin can add new user')

	@classmethod
	def remove_user(cls):
		# TODO: Update functionality (only admin can remove)
		pass

	@classmethod
	def change_user_password(cls):
		# TODO: add functionality (only admin can change)
		pass

	@classmethod
	def change_user_access_level(cls):
		# TODO: add functionality (only admin can change)
		pass

	@classmethod
	def add_project(cls):
		# Todo: add functionality (only manage can add project)
		pass


class Command:

	@classmethod
	def read(cls):
		print(Fore.BLUE + '----------------------------------------------------------')
		print(Fore.BLUE + ">>> What can I do for you?\n")
		read = input(Fore.LIGHTGREEN_EX + '>>> ')
		read = read.lower()
		read = read.strip()
		read = ' '.join(read.split())
		return read

	@classmethod
	def execute(cls, command):
		if command == '':
			raise ValueError('You did not input anything.')
		elif command == 'exit':
			Process.terminate()
		elif command == 'logout':
			Process.logout()
		elif command.startswith('add user '):
			Process.add_user(command)
		else:
			raise ValueError('command not recognized')

	# TODO: add all command to be execute on amyca_v1.0


def main():
	admin = user.User('admin', 'admin123', 4)
	Process.login()
	DisplayManager.greeting()
	while True:
		try:
			command = Command.read()
			Command.execute(command)
		except Exception as e:
			print(Fore.RED + '>>> ' + Back.LIGHTYELLOW_EX + Fore.RED + 'Sorry...!!!, I could not perform that command.')
			msg_problem = 'Problem  : ' + str(e)
			msg_info = 'INFO     : You can get more information about AMYCA CLI by entering \'help\' '
			if len(msg_problem) > len(msg_info):
				msg_len = len(msg_problem)
			else:
				msg_len = len(msg_info)
			print(Fore.RED + '=' * msg_len)
			print(Fore.RED + msg_problem)
			print(Fore.MAGENTA + msg_info)
			print(Fore.RED + '=' * msg_len)


if __name__ == '__main__':
	main()
