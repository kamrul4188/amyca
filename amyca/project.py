"""
Module Name: project

This is one of the core module of Amyca. This module create project object.
Project attributes store various object list are:
	1. Tasks object
	2. Resource object
	3.  Cost object
Those are key object of the project.
"""


class Project:
	__total = 0

	def __init__(self, name):
		"""
		Initialize project class with argument of project name
		:param name: project name
		"""
		self.name = name
		self.tasks = []
		self.resources = []
		self.cost = []
		self.id = Project.__total + 1
		Project.__total = Project.__total + 1

	def add_task(self, tasks):
		"""
		This function is to add task object into project
		:param tasks: task object
		:return: confirmation
		"""
		self.tasks.append(tasks)
		return 'task added'

	def add_resources(self, resources):
		"""
		This function is to add resource object into project
		:param resources: resource object
		:return: confirmation
		"""
		self.resources.append(resources)
		return 'resource added'

	def add_cost(self, cost):
		"""
		This function is to add cost object into project
		:param cost: cost object
		:return: confirmation
		"""
		self.cost.append(cost)
		return 'cost added'

	def get_name(self):
		"""
		This is to call project name
		:return: project name
		"""
		return self.name

	def get_id(self):
		"""
		This function is to call project ID
		:return: project ID
		"""
		return self.id

	def get_tasks(self):
		"""
		This function is to call task object
		:return: tasks list
		"""
		return self.tasks

	def get_resources(self):
		"""
		This function is to call resource
		:return: resources list
		"""
		return self.resources

	def get_cost(self):
		"""
		This function is to call cost
		:return: cost list
		"""
		return self.cost

	def remove_task(self, index):
		"""
		This function is call to remove task object as per index entered from task list.
		:param index: index of task to remove
		:return: confirmation
		"""
		del self.tasks[index]
		return 'A task with index ' + str(index + 1) + ' is removed.'

	def remove_resource(self, index):
		"""
		This function is to call to remove resource object as per index entered from resource list.
		:param index: index of resource to remove.
		:return: confirmation
		"""
		del self.resources[index]
		return 'A resource with index ' + str(index + 1) + ' is removed.'

	def remove_cost(self, index):
		"""
		This function is to remove cost object as per idex entered form cost list.
		:param index: index of cost to remove.
		:return: confirmation
		"""
		del self.cost[index]
		return 'A cost with index ' + str(index+1) + ' is removed.'

	@classmethod
	def get_total(cls):
		"""
		This function is to call for getting number of project object has created.
		:return: total project.
		"""
		return Project.__total

	def __str__(self):
		"""
		This function automatic call during initialize of project class to create project object.
		:return: project name and ID
		"""
		return 'Project name is: ' + self.name + ' and ID: ' + str(self.id)


if __name__ == '__main__':
	pass
