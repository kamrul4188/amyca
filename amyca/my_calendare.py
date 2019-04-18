"""
Module Name: my_calendar

This module to create calender in monthly view.
"""

import datetime
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar


class CalendarScreen:
	"""This class to create calendar object"""
	def __init__(self):
		"""Initialize CalendarScreen class"""
		self.current_year = int(datetime.date.today().strftime('%Y'))
		self.current_month = int(datetime.date.today().strftime('%m'))
		self.current_day = int(datetime.date.today().strftime('%d'))
		self.calendar_window = Toplevel()
		self.calendar = Calendar(self.calendar_window, font='Arial 14', selectmode='day', locale='en_US',
		                         year=self.current_year, month=self.current_month, day=self.current_day)
		self.calendar.pack(fill='both', expand=True)
		self.ok_button = ttk.Button(self.calendar_window, text=' OK ', command=self.calendar_window.destroy)
		self.ok_button.pack(padx=5, pady=5)

	def start(self):
		"""
		This function is to stat.
		:return: mainloop()
		"""
		return self.calendar_window.mainloop()


if __name__ == '__main__':
	pass
