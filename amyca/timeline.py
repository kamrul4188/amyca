"""
Module Name: timeline
This module is to crate timeline object
"""

import todo
import datetime


class TimeLine(todo.ToDo):
	"""This class is to add Timeline object"""
	TYPE_KEY = 'TL'

	def __init__(self, description, status, start_date, end_date):
		"""
		This function is initialize TimeLine class
		:param description: name/details of timeline object.
		:param status: task status -> bool
		:param start_date: stating date of timeline task
		:param end_date: ending date of timeline task
		"""
		super().__init__(description, status)
		self.start_date = self.format_to_datetime(start_date)
		self.end_date = self.format_to_datetime(end_date)

	def get_as_string(self):
		"""
		This function to get timeline object as string.
		Suitable to display into gui.
		:return: timeline object as string
		"""
		duration = self.duration_datetime(self.start_date, self.end_date)
		start = self.due_to_start(self.start_date)
		end = self.due_to_end(self.end_date)
		return self.description + '\n\t' + str(start) + '\n\t' + str(end) + '\n\t' + 'Duration: ' + str(duration)

	def as_csv(self):
		"""
		This function is to get timeline object as csv format
		:return: as csv
		"""
		start_date = self.datetime_to_print_format(self.start_date)
		end_date = self.datetime_to_print_format(self.end_date)
		return ['TL', self.description, 'done' if self.is_done else 'pending', start_date, end_date]

	def format_to_datetime(self, date):
		"""
		This function is to convert input date into datetime format.
		:param date: input date
		:return: datetime
		"""
		date_format = '%d/%m/%Y'
		input_date = date
		try:
			date_obj = datetime.datetime.strptime(input_date, date_format).date()
			return date_obj
		except ValueError:
			raise ValueError("Incorrect data format, should be dd/mm/yyyy")

	def datetime_to_print_format(self, date):
		"""
		This function in to convert date into printable format from datetime format.
		:param date:
		:return:
		"""
		try:
			print_date = date.strftime("%d/%m/%Y")
			return print_date
		except ValueError:
			return 'Format of your input is not datetime'

	def duration_datetime(self, start_date, end_date):
		"""
		This function is to get duration between two days
		:param start_date: stating date
		:param end_date: end date
		:return: duration
		"""
		try:
			if end_date >= start_date:
				duration = end_date - start_date
				duration = str(duration).split(',', 1)[0]
				return duration
			else:
				return 'Your end date ims earlier than start'
		except ValueError:
			raise ValueError('Format of your input ins not datetime')

	def due_to_start(self, date):
		"""
		This function is to get duration of date from today.
		:param date: input date
		:return: duration from today
		"""
		input_date = date # end date
		today_date = datetime.date.today()
		if input_date >= today_date:
			due_date = self.duration_datetime(today_date, input_date)
			return 'Starting: ' + str(due_date)
		else:
			due_date = self.duration_datetime(input_date, today_date)
			return 'Progress: ' + str(due_date)

	def due_to_end(self, date):
		"""
		This function is to get duration form today
		:param date: input date
		:return: duration from today
		"""
		input_date = date  # end date
		today_date = datetime.date.today()
		if input_date >= today_date:
			due_date = self.duration_datetime(today_date, input_date)
			return 'Ending: ' + str(due_date)
		else:
			due_date = self.duration_datetime(input_date, today_date)
			return 'Overdue: ' + str(due_date)

	def get_start_date(self):
		"""
		This function is get starting date of timeline object.
		:return: date
		"""
		return self.start_date

	def get_end_date(self):
		"""
		This function is to get end date of timeline object.
		:return: date.
		"""
		return self.end_date

	def get_duration(self):
		"""
		This function is to get duration of timeline object between stat date and end date.
		:return: duration.
		"""
		return self.duration_datetime(self.start_date, self.end_date)


if __name__ == '__main__':
	pass






