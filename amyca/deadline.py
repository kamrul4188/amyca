import todo


class Deadline (todo.ToDo):
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

	def as_csv(self):
		""" Return the details of todo object as a list,
		suitable to be stored in a csv file.
		"""
		return ['D', self.description, 'done' if self.is_done else 'pending', self.by]
