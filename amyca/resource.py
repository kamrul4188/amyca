class Resource:
	TYPE_KEY = 'R'

	def __init__(self, description, quantity):
		self.description = description
		self.quantity = quantity

	def get_description(self):
		return self.description

	def get_quantity(self):
		return self.quantity

	def as_csv(self):
		return ['R', self.description, self.quantity]

	def __str__(self):
		return 'Resource is added to project'
