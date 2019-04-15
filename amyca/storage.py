import csv
from todo import ToDo
from deadline import Deadline
from timeline import TimeLine
from resource import Resource
from cost import Cost


class StorageManager:
	"""this class used to read data from the data file and write data back to the data file."""
	def __init__(self, file_path):
		self.storage = file_path

	def load_tasks(self):
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
		data_deadline = []
		data_file = open(self.storage)
		deliveries_reader = csv.reader(data_file)
		for row in deliveries_reader:
			if row[0] == 'D':
				data_deadline.append(Deadline(row[1], True if row[2] == 'done' else False, row[3]))
		data_file.close()
		return data_deadline

	def load_resource(self):
		data_resource = []
		data_file = open(self.storage)
		deliveries_reader = csv.reader(data_file)
		for row in deliveries_reader:
			if row[0] == 'R':
				data_resource.append(Resource(row[1], row[2]))
		data_file.close()
		return data_resource


	def load_cost(self):
		data_cost = []
		data_file = open(self.storage)
		deliveries_reader = csv.reader(data_file)
		for row in deliveries_reader:
			if row[0] == 'C':
				data_cost.append(Cost(row[1], row[2]))
		data_file.close()
		return data_cost

	def save_data(self, data):
		data = data
		output_file = open(self.storage, 'w', newline='')
		output_writer = csv.writer(output_file)
		for item in data:
			output_writer.writerow(item.as_csv())
		output_file.close()
		return 'Data save to ' + '[ /' + self.storage + ' ]' + ' as csv format.'

	def __str__(self):
		return self.storage


if __name__ == '__main__':
	tasks = []
	task_1 = ToDo('Read book', False)
	task_2 = ToDo('Return book', True)
	task_3 = Deadline('install Air-Con', False, 'Monday')
	task_4 = Deadline('Servicing Air-Con', True, 'Today')
	tasks.append(task_1)
	tasks.append(task_2)
	tasks.append(task_3)
	tasks.append(task_4)

	resources = []
	resources.append(Resource('Manpower', 100))
	resources.append(Resource('Service Charge', 5000))

	storage_manager = StorageManager('data/data.csv')
	print(storage_manager)

	save = storage_manager.save_data(tasks)
	print(save)

	todo = storage_manager.load_todo()
	print(todo)

	deadline = storage_manager.load_deadline()
	print(deadline)

	res = StorageManager('data/resources.csv')
	res_save = res.save_data(resources)
	print(res_save)

	my_resource = res.load_resource()
	print(my_resource)

	costs = [Cost('Manpower', 500), Cost('Service Charge', 50)]
	my_cost = StorageManager('data/cost.csv')
	my_cost.save_data(costs)

	cost = my_cost.load_cost()
	print(cost)

