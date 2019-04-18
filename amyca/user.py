"""
Module name: user
This module is to create user object.
"""

import password as pw
import csv


class User:
	"""This class is to create user object"""
	__users = []
	__total = 0
	__current_user_name = ''
	__current_user_level = 0

	INDEX_USER_NAME = 0
	INDEX_USER_PASSWORD = 1
	INDEX_USER_ACCESS_LEVEL = 2

	def __init__(self, user_name, password, access_level):
		"""
		This function is to initialize user class.
		:param user_name: username/ID
		:param password: password to be set for the user
		:param access_level: user access level
		"""
		self.__user_name = user_name
		self.__password = pw.Password.hash(password)
		self.__access_level = int(access_level)
		User.__total = User.__total + 1
		User.__users.append([self.__user_name, self.__password, self.__access_level])

	@classmethod
	def verify(cls, name, password):
		"""
		This function is to verify user with database.
		:param name: user name
		:param password: user password
		:return: bool
		"""
		try:
			for i, user in enumerate(cls.__users):
				temp_user_name = cls.__users[i][cls.INDEX_USER_NAME]
				temp_user_password = cls.__users[i][cls.INDEX_USER_PASSWORD]
				temp_user_access_level = cls.__users[i][cls.INDEX_USER_ACCESS_LEVEL]
				if temp_user_name == name and pw.Password.verify(temp_user_password, password):
					cls.__current_user_name = temp_user_name
					cls.__current_user_level = temp_user_access_level
					return True
		except IndexError:
			raise IndexError('Index is our of range')

	@classmethod
	def remove(cls, name, password):
		"""
		This function is to remove user from database.
		:param name: user name
		:param password: user password
		:return: confirmation
		"""
		user_name = name
		user_password = password
		for i, user in enumerate(cls.__users):
			if cls.verify(user_name, user_password):
				del cls.__users[i]
				return '[' + user_name + '] has been remove from user.'

		return '[' + user_name + '] Not exit in user list'

	@classmethod
	def change_password(cls, name, current_password, new_password):
		"""
		This function is to change registered user password.
		:param name: usr name
		:param current_password: user current password
		:param new_password: user new password
		:return: confirmation.
		"""
		user_name = name
		current_password = current_password
		new_password = pw.Password.hash(new_password)
		for i, user in enumerate(cls.__users):
			if cls.verify(user_name, current_password):
				cls.__users[i][1] = new_password
				return 'Password Change for user [ ' + user_name + ' ]'
		return 'Username or password not match'

	@classmethod
	def get_total(cls):
		"""
		This function is to get total registered users.
		:return: total user
		"""
		return cls.__total

	@classmethod
	def get_current_user_name(cls):
		"""
		This function is to get current user login / verify
		:return: user name
		"""
		return cls.__current_user_name

	@classmethod
	def get_current_user_access_level(cls):
		"""
		This function is to get current user access level
		:return: user level
		"""
		return cls.__current_user_level

	@classmethod
	def get_users(cls):
		"""
		This function is to get all user
		:return: user list
		"""
		return User.__users

	@classmethod
	def save_as_csv(cls, storage):
		"""
		This function is to save user object into storage
		:param storage: path of storage
		:return: confirmation
		"""
		output_file = open(storage, 'w', newline='')
		output_writer = csv.writer(output_file)
		for user in User.__users:
			output_writer.writerow(user)
		output_file.close()
		return 'User info save'

	@classmethod
	def load_form_csv(cls, storage):
		"""
		This function is to get/load user data from storage
		:param storage: path of user data
		:return: confirmation
		"""
		file = open(storage)
		deliveries_reader = csv.reader(file)
		for row in deliveries_reader:
			User.__users.append([row[0], row[1], row[2]])
		file.close()

		return 'User is loaded'

	def __str__(self):
		"""
		This function run during initialization
		:return: confirmation
		"""
		return 'New User added. [' + self.__user_name + ']'


if __name__ == '__main__':
	pass

