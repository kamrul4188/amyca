#import sys
import hashlib, binascii, os


class Project:
	def __init__(self, name):
		self.name = name
		self.task = []


class User:

	__users = []
	__current_user_name = ''
	__current_user_level = 0

	INDEX_USER_NAME = 0
	INDEX_USER_PASSWORD = 1
	INDEX_USER_ACCESS_LEVEL = 2

	def __init__(self, user_name, password, access_level):
		self.__user_name = user_name
		self.__password = Password.hash(password)
		self.__access_level = access_level
		User.__users.append([self.__user_name, self.__password, self.__access_level])

	def get_password(self, name):
		if self.__user_name == name:
			return self.__password
		else:
			raise ValueError('User name not found')

	@classmethod
	def info(cls):
		return cls.__users

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
			raise('Index is our of range')

	@classmethod
	def get_current_user_name(cls):
		return cls.__current_user_name

	@classmethod
	def get_current_user_access_level(cls):
		return cls.__current_user_level


class Password:

	@classmethod
	def hash(self, password):
		"""Hash a password for storing."""
		salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
		pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
		pwdhash = binascii.hexlify(pwdhash)
		return (salt + pwdhash).decode('ascii')

	@classmethod
	def verify(self, stored_password, provided_password):
		"""Verify a stored password against one provided by user"""
		salt = stored_password[:64]
		stored_password = stored_password[64:]
		assert isinstance(salt, object)
		pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
		pwdhash = binascii.hexlify(pwdhash).decode('ascii')
		return pwdhash == stored_password


class Access:

	@classmethod
	def login(cls):
		while True:
			user_input = input('Please enter username and password: ')

			user_name = user_input.split(' ', 1)[0]
			user_password = user_input.split(' ', 1)[1]
			if User.verify(user_name, user_password):
				break
			else:
				print('Error: username or passwod in incorrect. Please try again...!!!')
				continue

	@classmethod
	def logout(cls):
		main()
		#TODO: Add more functionality

	@classmethod
	def exit(cls):
		pass
		#TODO: Inplement exit functionality


class Command:

	@classmethod
	def read(cls):
		print('----------------------------------------------------------')
		print(">>> What can I do for you?\n")
		read = input()
		return read

	@classmethod
	def execute(cls, command):
		if command == '':
			raise ValueError('You did not input anything')
		elif command == 'logout':
			Access.logout()
		else:
			raise ValueError('command not recognized')


def main():
	User('admin', 'admin123', 4)
	Access.login()
	while True:
		try:
			command = Command.read()
			Command.execute(command)
		except Exception as e:
			print('Sorry, I could not perform that command. Problem:', e)


if __name__ == '__main__':
	main()
