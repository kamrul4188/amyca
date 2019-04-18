"""
Module      : test_project
Test Case   : A001
Test Module : project.py
Test Type   : Unit Test
"""

import unittest
from project import Project


class TestProject(unittest.TestCase):
	"""This module is created to test project.py module. called all method form project.py module and test is function """

	# Created project object
	p1 = Project('p1')
	p2 = Project('p2')
	p3 = Project('p3')

	def test_add_task(self):
		"""This function to test add_task method of project.py module"""
		task_1 = ['read book', False]
		task_2 = ['return book', False]
		self.assertEqual(TestProject.p1.add_task(task_1), 'task added')
		self.assertEqual(TestProject.p1.add_task(task_2), 'task added')
		self.assertEqual(TestProject.p2.add_task(task_1), 'task added')
		self.assertEqual(TestProject.p2.add_task(task_2), 'task added')

	def test_add_resources(self):
		"""This function to test add_resources method of project.py module"""
		resource_1 = ['Manpower', 50]
		resource_2 = ['Material', 100]
		self.assertEqual(TestProject.p1.add_resources(resource_1), 'resource added')
		self.assertEqual(TestProject.p1.add_resources(resource_2), 'resource added')
		self.assertEqual(TestProject.p2.add_resources(resource_1), 'resource added')
		self.assertEqual(TestProject.p2.add_resources(resource_2), 'resource added')

	def test_add_cost(self):
		"""This function to test add_cost method of project.py module"""
		cost_1 = ['Manpower', 1000]
		cost_2 = ['Material', 5000]
		self.assertEqual(TestProject.p1.add_cost(cost_1), 'cost added')
		self.assertEqual(TestProject.p1.add_cost(cost_2), 'cost added')
		self.assertEqual(TestProject.p2.add_cost(cost_1), 'cost added')
		self.assertEqual(TestProject.p2.add_cost(cost_2), 'cost added')

	def test_get_name(self):
		"""This function to test get_name method of project.py module"""
		self.assertEqual(TestProject.p1.get_name(), 'p1')
		self.assertEqual(TestProject.p2.get_name(), 'p2')

	def test_get_id(self):
		"""This function is to test get_id (project ID) method of project.py module"""
		self.assertEqual(TestProject.p1.get_id(), 1)
		self.assertEqual(TestProject.p2.get_id(), 2)

	def test_get_tasks(self):
		"""This function is to test get_task method of project.py module"""
		task_1 = ['read book', False]
		task_2 = ['return book', False]
		tasks = [task_1, task_2]
		self.assertEqual(TestProject.p1.get_tasks(), tasks)
		self.assertEqual(TestProject.p2.get_tasks(), tasks)

	def test_get_resources(self):
		"""This function is to test get_resources method of project.py module"""
		resource_1 = ['Manpower', 50]
		resource_2 = ['Material', 100]
		resources = [resource_1, resource_2]
		self.assertEqual(TestProject.p1.get_resources(), resources)
		self.assertEqual(TestProject.p2.get_resources(), resources)

	def test_get_cost(self):
		"""This function is to test get_cost method of project.py module"""
		cost_1 = ['Manpower', 1000]
		cost_2 = ['Material', 5000]
		cost = [cost_1, cost_2]
		self.assertEqual(TestProject.p1.get_cost(), cost)
		self.assertEqual(TestProject.p2.get_cost(), cost)

	def test_get_total(self):
		"""This function is to test get_total (total project) method of project.py"""
		self.assertEqual(TestProject.p1.get_total(), 3)
		self.assertEqual(TestProject.p2.get_total(), 3)
		self.assertNotEquals(TestProject.p3.get_total(), 2)


if __name__ == '__name__':
	"""Call unit test module to run and test"""
	unittest.main()
