import unittest
from project import Project


class TestProject(unittest.TestCase):
	"""This class is define for test module called project"""
	p1 = Project('p1')
	p2 = Project('p2')
	p3 = Project('p3')

	def test_add_task(self):
		task_1 = ['read book', False]
		task_2 = ['return book', False]
		self.assertEqual(TestProject.p1.add_task(task_1), 'task added')
		self.assertEqual(TestProject.p1.add_task(task_2), 'task added')
		self.assertEqual(TestProject.p2.add_task(task_1), 'task added')
		self.assertEqual(TestProject.p2.add_task(task_2), 'task added')

	def test_add_resources(self):
		resource_1 = ['Manpower', 50]
		resource_2 = ['Material', 100]
		self.assertEqual(TestProject.p1.add_resources(resource_1), 'resource added')
		self.assertEqual(TestProject.p1.add_resources(resource_2), 'resource added')
		self.assertEqual(TestProject.p2.add_resources(resource_1), 'resource added')
		self.assertEqual(TestProject.p2.add_resources(resource_2), 'resource added')

	def test_add_cost(self):
		cost_1 = ['Manpower', 1000]
		cost_2 = ['Material', 5000]
		self.assertEqual(TestProject.p1.add_cost(cost_1), 'cost added')
		self.assertEqual(TestProject.p1.add_cost(cost_2), 'cost added')
		self.assertEqual(TestProject.p2.add_cost(cost_1), 'cost added')
		self.assertEqual(TestProject.p2.add_cost(cost_2), 'cost added')

	def test_get_name(self):
		self.assertEqual(TestProject.p1.get_name(), 'p1')
		self.assertEqual(TestProject.p2.get_name(), 'p2')

	def test_get_id(self):
		self.assertEqual(TestProject.p1.get_id(), 1)
		self.assertEqual(TestProject.p2.get_id(), 2)

	def test_get_tasks(self):
		task_1 = ['read book', False]
		task_2 = ['return book', False]
		tasks = [task_1, task_2]
		self.assertEqual(TestProject.p1.get_tasks(), tasks)
		self.assertEqual(TestProject.p2.get_tasks(), tasks)

	def test_get_resources(self):
		resource_1 = ['Manpower', 50]
		resource_2 = ['Material', 100]
		resources = [resource_1, resource_2]
		self.assertEqual(TestProject.p1.get_resources(), resources)
		self.assertEqual(TestProject.p2.get_resources(), resources)

	def test_get_cost(self):
		cost_1 = ['Manpower', 1000]
		cost_2 = ['Material', 5000]
		cost = [cost_1, cost_2]
		self.assertEqual(TestProject.p1.get_cost(), cost)
		self.assertEqual(TestProject.p2.get_cost(), cost)

	def test_get_total(self):
		self.assertEqual(TestProject.p1.get_total(), 3)
		self.assertEqual(TestProject.p2.get_total(), 3)
		self.assertNotEquals(TestProject.p3.get_total(), 2)


if __name__ == '__name__':
	unittest.main()
