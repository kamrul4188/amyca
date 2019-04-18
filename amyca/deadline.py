"""
Module Name     : deadline
Parent Module   : todo
This module is to create deadline task object for Amyca.
"""
import todo


class Deadline (todo.ToDo):
	"""This class create deadline object"""
	TYPE_KEY = 'D'

	def __init__(self, description, status, by):
		"""
		Initialize of deadline class object
		:param description: name/details of deadline task
		:param status: status of object. type: bool
		:param by: due to complite the task
		"""
		super().__init__(description, status)
		self.by = by

	def as_string(self):
		"""
		This function is to call to get printable as string of deadline object
		Suitable to commandline print function.
		:return: deadline as string
		"""
		status = '✓' if self.is_done else '✗'
		offset = 30 - len(self.description)
		return status.center(8) + '|'.ljust(3) + self.description + ' '.ljust(offset) + '|'.ljust(3) + self.by

	def get_as_string(self):
		"""
		This function is to call to get string to display of deadline object.
		Suitable for GUI display.
		:return: deadline as string
		"""
		return self.description + '. ' + 'Due: ' + self.by

	def __str__(self):
		"""
		This function is call during initialization
		:return: obj as string
		"""
		return super().__str__() + '[by ' + self.by + ']'

	def as_csv(self):
		""" Return the details of todo object as a list,
		suitable to be stored in a csv file.
		"""
		return ['D', self.description, 'done' if self.is_done else 'pending', self.by]


if __name__ == '__main__':
	pass
