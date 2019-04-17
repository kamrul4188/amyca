"""
This
"""
class Project:
	__total = 0

	def __init__(self, name):
		self.name = name
		self.tasks = []
		self.resources = []
		self.cost = []
		self.id = Project.__total + 1
		Project.__total = Project.__total + 1

	def add_task(self, tasks):
		self.tasks.append(tasks)
		return 'task added'

	def add_resources(self, resources):
		self.resources.append(resources)
		return 'resource added'

	def add_cost(self, cost):
		self.cost.append(cost)
		return 'cost added'

	def get_name(self):
		return self.name

	def get_id(self):
		return self.id

	def get_tasks(self):
		return self.tasks

	def get_resources(self):
		return self.resources

	def get_cost(self):
		return self.cost

	def remove_task(self, index):
		del self.tasks[index]
		return 'A task with index ' + str(index + 1) + ' is removed.'

	def remove_resource(self, index):
		del self.resources[index]
		return 'A resource with index ' + str(index + 1) + ' is removed.'

	def remove_cost(self, index):
		del self.cost[index]
		return 'A cost with index ' + str(index+1) + ' is removed.'

	@classmethod
	def get_total(cls):
		return Project.__total

	def __str__(self):
		return 'Project name is: ' + self.name + ' and ID: ' + str(self.id)


if __name__ == '__main__':
	pass
