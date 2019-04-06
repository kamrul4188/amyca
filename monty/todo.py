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
