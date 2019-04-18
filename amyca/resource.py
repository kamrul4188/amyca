"""
Module Name : resource

This is module is to create resource object for Amyca
"""


class Resource:
	"""Class to generate resource object"""
	TYPE_KEY = 'R'

	def __init__(self, description, quantity):
		"""
		Initialize resource class
		:param description: name/details of resources object to be create
		:param quantity: quantity of resource object
		"""
		self.description = description
		self.quantity = quantity

	def get_description(self):
		"""
		This function is to get name/details of resources objects
		:return: description
		"""
		return self.description

	def get_quantity(self):
		"""
		This function is to get quantity of resource object
		:return: quantity
		"""
		return self.quantity

	def as_csv(self):
		"""
		This function is to get resource object as string in csv format
		Suitable to storage into .csv file
		:return: obj as list
		"""
		return ['R', self.description, self.quantity]

	def __str__(self):
		"""
		This function is execute during initialize
		:return: confirmation
		"""
		return 'Resource is added to project'


if __name__ == '__main__':
	pass

