import binascii
import hashlib
import os
import sys
import pyfiglet
from colorama import init; init(autoreset=True)
from colorama import Fore, Back, Style


class Project:
	def __init__(self, name):
		self.name = name
		self.task = []


class User:
	__users = []
	__total = 0
	__current_user_name = ''
	__current_user_level = 0

	INDEX_USER_NAME = 0
	INDEX_USER_PASSWORD = 1
	INDEX_USER_ACCESS_LEVEL = 2

	def __init__(self, user_name, password, access_level):
		self.__user_name = user_name
		self.__password = Password.hash(password)
		self.__access_level = access_level
		User.__total = User.__total + 1
		User.__users.append([self.__user_name, self.__password, self.__access_level])

	@classmethod
	def verify(cls, name, password):
		try:
			for i, user in enumerate(cls.__users):
				temp_user_name = cls.__users[i][cls.INDEX_USER_NAME]
				temp_user_password = cls.__users[i][cls.INDEX_USER_PASSWORD]
				temp_user_access_level = cls.__users[i][cls.INDEX_USER_ACCESS_LEVEL]
				if temp_user_name == name and Password.verify(temp_user_password, password):
					cls.__current_user_name = temp_user_name
					cls.__current_user_level = temp_user_access_level
					return True
		except IndexError:
			raise IndexError('Index is our of range')

	@classmethod
	def get_total(cls):
		return cls.__total

	@classmethod
	def get_current_user_name(cls):
		return cls.__current_user_name

	@classmethod
	def get_current_user_access_level(cls):
		return cls.__current_user_level


class Password:

	@classmethod
	def hash(cls, password):
		"""Hash a password for storing."""
		salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
		password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
		password_hash = binascii.hexlify(password_hash)
		return (salt + password_hash).decode('ascii')

	@classmethod
	def verify(cls, stored_password, provided_password):
		"""Verify a stored password against one provided by user"""
		salt = stored_password[:64]
		stored_password = stored_password[64:]
		assert isinstance(salt, object)
		password_hash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
		password_hash = binascii.hexlify(password_hash).decode('ascii')
		return password_hash == stored_password


class Print:

	@classmethod
	def greeting(cls):

		banner = pyfiglet.figlet_format('Welcome to AMYCA')
		print(Fore.MAGENTA + banner)


class Process:

	@classmethod
	def login(cls):
		while True:
			try:
				user_input = input(Fore.LIGHTGREEN_EX + 'Please enter username and password: ')
				user_name = user_input.split(' ', 1)[0]
				user_password = user_input.split(' ', 1)[1]
				if User.verify(user_name, user_password):
					break
				else:
					print(Fore.RED + 'Error: username or password in incorrect. Please try again...!!!')
					continue
			except IndexError:
				print(Fore.RED + 'Invalid user input. Please try again...!!! ')
				continue

	@classmethod
	def logout(cls):
		print('You have successfully logout as ' + Fore.RED + User.get_current_user_name())
		main()

	@classmethod
	def terminate(cls):
		print('>>> Are you sure? y/n')
		response = input()
		if response.lower() == 'y':
			print(">>> Bye!")
			sys.exit()
		elif response.lower() == 'n':
			print(pyfiglet.figlet_format('Welcome back !', font='digital'))

		else:
			raise ValueError('Invalid input')

	@classmethod
	def add_user(cls, user_input):
		"""
		:param user_input: command + user parameter
		:parameter 0 and 1: command
		:parameter 2: user name
		:parameter 3: user password
		:parameter 4: user access level
		:return: null
		"""
		name = user_input.split(' ', 5)[2]
		password = user_input.split(' ', 5)[3]
		level = user_input.split(' ', 5)[4]
		User(name, password, level)
		print('A user has  been added as ' + Fore.RED + name + Style.RESET_ALL + ' with level of access is : ' + Fore.RED + str(level))


class Command:

	@classmethod
	def read(cls):
		print(Fore.BLUE + '----------------------------------------------------------')
		print(Fore.BLUE + ">>> What can I do for you?\n")
		read = input(Fore.LIGHTGREEN_EX + '>>> ')
		return read

	@classmethod
	def execute(cls, command):
		if command == '':
			raise ValueError('You did not input anything')
		elif command == 'exit':
			Process.terminate()
		elif command == 'logout':
			Process.logout()
		elif command.startswith('add user '):
			Process.add_user(command)
		else:
			raise ValueError('command not recognized')


def main():
	User('admin', 'admin123', 4)
	Process.login()
	Print.greeting()
	while True:
		try:
			command = Command.read()
			Command.execute(command)
		except Exception as e:
			print(Fore.RED + '>>> Sorry, I could not perform that command. Problem:', e)


if __name__ == '__main__':
	main()