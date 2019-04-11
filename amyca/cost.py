class Cost:
	TYPE_KEY = 'C'

	def __init__(self, description, cost):
		self.description = description
		self.cost = cost

	def get_description(self):
		return self.description

	def get_cost(self):
		return self.cost

	def __str__(self):
		return 'Cost is added to project'

