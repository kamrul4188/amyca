"""
Module name : todo
This module is to create todo object.
"""


class ToDo:
	"""This class to create todo object"""

	TYPE_KEY = 'T'

	def __init__(self, description, status):
		"""
		This function is initialize todo class
		:param description: name/details of todo object.
		:param status: task status -> bool
		"""
		self.description = description
		self.is_done = status

	def mark_as_done(self):
		"""This function is to set task status (True) as done"""
		self.is_done = True

	def mark_as_pending(self):
		"""This function is reset task status (False) as pending"""
		self.is_done = False

	def as_string(self):
		"""
		This is to get todo object as printable string
		Suitable to commandline print.
		:return: dodo obj as string
		"""
		status = '✓' if self.is_done else '✗'
		offset = 30 - len(self.description)
		return status.center(8) + '|'.ljust(3) + self.description

	def __status_as_icon(self):
		"""
		This function is to get status of todo object as icon
		:return: icon
		"""
		return '✓' if self.is_done else '✗'

	def get_status(self):
		"""
		This function is to get status of todo object
		:return: status -> True
		"""
		return self.is_done

	def get_status_as_icon(self):
		"""
		This function is to get status icon of todo object
		:return:
		"""
		return '✓' if self.is_done else '✗'

	def get_as_string(self):
		"""
		This function is to get name/details of todo object as string
		:return: description
		"""
		return self.description + '.'

	def __str__(self):
		"""
		This function is call during initialization.
		:return: todo object as string.
		"""
		return '(' + self.__status_as_icon() + ')' + self.description

	@classmethod
	def get_str(cls):
		"""
		This function ist to get todo object as string
		:return: as string
		"""
		return cls.__str__()

	def as_csv(self):
		""" Return the details of todo object as a list,
		suitable to be stored in a csv file.
		:return: as csv
		"""
		return ['T', self.description, 'done' if self.is_done else 'pending']
