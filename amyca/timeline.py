import todo
import datetime

class TimeLine(todo.ToDo):
	"""This class is to add Timeline object"""
	TYPE_KEY = 'TL'

	def __init__(self, description, status, start_date, end_date):
		super().__init__(description, status)
		self.start_date = self.format_to_datetime(start_date)
		self.end_date = self.format_to_datetime(end_date)

	def get_as_string(self):
		duration = self.duration_datetime(self.start_date, self.end_date)
		start = self.due_to_start(self.start_date)
		end = self.due_to_end(self.end_date)
		return self.description + '\n\t' + str(start) + '\n\t' + str(end) + '\n\t' + 'Duration: ' + str(duration)


	def as_csv(self):
		"""Return the details of timeline object as a list"""
		start_date = self.datetime_to_print_format(self.start_date)
		end_date = self.datetime_to_print_format(self.end_date)
		return ['TL', self.description, 'done' if self.is_done else 'pending', start_date, end_date]

	def format_to_datetime(self, date):
		date_format = '%d/%m/%Y'
		input_date = date
		try:
			date_obj = datetime.datetime.strptime(date, date_format).date()
			return date_obj
		except ValueError:
			raise ValueError("Incorrect data format, should be dd/mm/yyyy")

	def datetime_to_print_format(self, date):
		try:
			print_date = date.strftime("%d/%m/%Y")
			return print_date
		except ValueError:
			return 'Format of your input is not datetime'

	def duration_datetime(self, start_date, end_date):
		try:
			if end_date >= start_date:
				duration = end_date - start_date
				duration = str(duration).split(',', 1)[0]
				return duration
			else:
				return 'Your end date ims earlier than start'
		except ValueError:
			raise ValueError('Format of your input ins not detetime')

	def due_to_start(self, date):
		input_date = date # end date
		today_date = datetime.date.today()
		if input_date >= today_date:
			due_date = self.duration_datetime(today_date, input_date)
			return 'Starting: ' + str(due_date)
		else:
			due_date = self.duration_datetime(input_date, today_date)
			return 'Progress: ' + str(due_date)

	def due_to_end(self, date):
		input_date = date  # end date
		today_date = datetime.date.today()
		if input_date >= today_date:
			due_date = self.duration_datetime(today_date, input_date)
			return 'Ending: ' + str(due_date)
		else:
			due_date = self.duration_datetime(input_date, today_date)
			return 'Overdue: ' + str(due_date)

	def get_start_date(self):
		return self.start_date

	def get_end_date(self):
		return self.end_date

	def get_duration(self):
		return self.duration_datetime(self.start_date, self.end_date)

if __name__ == '__main__':
	tasks = []
	obj_1 = TimeLine('install air con', False, '20/04/2019', '30442019')
	obj_2 = TimeLine('Repair', True, '01/04/2019', '05/04/2019')
	tasks.append(obj_1)
	tasks.append(obj_2)
	print(tasks)






