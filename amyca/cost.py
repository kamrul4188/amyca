"""
Module Name : cost
This module to create cost object for amyca
"""


class Cost:
	"""This class is to create cost object"""
	TYPE_KEY = 'C'

	def __init__(self, description, cost):
		"""
		This function is initialize during creating of cost object.
		:param description: name/details of cost object
		:param cost: amount ($)
		"""
		self.description = description
		self.cost = cost

	def get_description(self):
		"""
		This function is to call to get details of cost object
		:return: description
		"""
		return self.description

	def get_cost(self):
		"""
		This function is to call to get amount of cost ($) of cost object
		:return: cost ($)
		"""
		return self.cost

	def as_csv(self):
		"""
		This function is to call to get cost object as format for .csv storage
		:return: cost object as csv format
		"""
		return ['C', self.description, self.cost]

	def __str__(self):
		"""
		This function call call during initialization
		:return: confirmation
		"""
		return 'Cost is added to project'


if __name__ == '__main__':
	pass
