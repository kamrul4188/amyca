"""
Module Name : storage
This module is to mange storage data to hard disk to back up.
"""

import csv
from todo import ToDo
from deadline import Deadline
from timeline import TimeLine
from resource import Resource
from cost import Cost


class StorageManager:
	"""this class used to read data from the data file and write data back to the data file."""
	def __init__(self, file_path):
		"""
		This function is to initialize storage manager.
		:param file_path: path to storage datal.
		"""
		self.storage = file_path

	def load_tasks(self):
		"""
		This function is to lead task list date from storage.
		:return: task object list.
		"""
		data_task = []
		data_file = open(self.storage)
		deliveries_reader = csv.reader(data_file)
		for row in deliveries_reader:
			if row[0] == 'T':
				data_task.append(ToDo(row[1], True if row[2] == 'done' else False))
			elif row[0] == 'D':
				data_task.append(Deadline(row[1], True if row[2] == 'done' else False, row[3]))
			elif row[0] == 'TL':
				data_task.append(TimeLine(row[1], True if row[2] == 'done' else False, row[3], row[4]))
		data_file.close()
		return data_task

	def load_deadline(self):
		"""
		This function is to load deadline object data form storage.
		:return: deadline object list.
		"""
		data_deadline = []
		data_file = open(self.storage)
		deliveries_reader = csv.reader(data_file)
		for row in deliveries_reader:
			if row[0] == 'D':
				data_deadline.append(Deadline(row[1], True if row[2] == 'done' else False, row[3]))
		data_file.close()
		return data_deadline

	def load_resource(self):
		"""
		This function is to load resource object date form storage.
		:return: resource object list.
		"""
		data_resource = []
		data_file = open(self.storage)
		deliveries_reader = csv.reader(data_file)
		for row in deliveries_reader:
			if row[0] == 'R':
				data_resource.append(Resource(row[1], row[2]))
		data_file.close()
		return data_resource

	def load_cost(self):
		"""
		This function is to load cost object data from storage.
		:return: cost object list.
		"""
		data_cost = []
		data_file = open(self.storage)
		deliveries_reader = csv.reader(data_file)
		for row in deliveries_reader:
			if row[0] == 'C':
				data_cost.append(Cost(row[1], row[2]))
		data_file.close()
		return data_cost

	def save_data(self, data):
		"""
		This function is to store data into storage.
		:param data: data to be storage.
		:return: confirmation
		"""
		data = data
		output_file = open(self.storage, 'w', newline='')
		output_writer = csv.writer(output_file)
		for item in data:
			output_writer.writerow(item.as_csv())
		output_file.close()
		return 'Data save to ' + '[ /' + self.storage + ' ]' + ' as csv format.'

	def __str__(self):
		"""
		This function call during initialization
		:return: storage
		"""
		return self.storage


if __name__ == '__main__':
	pass
