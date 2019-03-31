


class Project:
	__total = 0

	def __init__(self, project_name):
		self.project_name = project_name
		self.project_task = []
		self.project_budget = 0
		self.project_id = Project.__total + 1
		Project.__total = Project.__total + 1

	@classmethod
	def get_total_project(cls):
		return Project.__total

	def add_task(self, activity, start_date, end_date,  ):
		pass



class Task:
	tasks = []

	def __init__(self, activity):
		self.activity = activity

if __name__ == '__main__':
	p1 = Project('project_1')
	print('Project name: ',  p1.project_name)
	print('Project ID: ', p1.project_id)

	p2 = Project('Project_2')
	print('Project name: ', p2.project_name)
	print('Project ID: ', p2.project_id)

	print('Total Project: ', Project.get_total_project())

	T1 = Task(p1)
