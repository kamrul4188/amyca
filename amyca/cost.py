class Cost:
	TYPE_KEY = 'C'

	def __init__(self, description, cost):
		self.description = description
		self.cost = cost

	def get_description(self):
		return self.description

	def get_cost(self):
		return self.cost

	def as_csv(self):
		return ['C', self.description, self.cost]

	def __str__(self):
		return 'Cost is added to project'

if __name__ == '__main__':
	my_cost = []
	x = Cost('Install aircon', 5000)
	y = Cost('Service Charge', 1000)
	my_cost.append(x)
	my_cost.append(y)
	#print(dir(x))

	print(my_cost)
