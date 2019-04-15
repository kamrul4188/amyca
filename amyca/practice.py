class TimeLineScreen:
	def __init__(self):
		self.timeline_window = Toplevel()
		self.timeline_window.geometry('300x300')
		self.timeline_window.title('Timeline Task')
		self.timeline_window.iconphoto(self.timeline_window, PhotoImage(file='img_title.png'))

		self.label = Label(self.timeline_window, text='Please enter details to add timeline tasks')
		self.label.pack(padx=10, pady=10)

		self.label_description = Label(self.timeline_window, text='Description *')
		self.label_description.pack(padx=5, pady=5)
		self.entry_description = Entry(self.timeline_window)
		self.entry_description.pack(padx=5, pady=5)

		self.label_start_date = Label(self.timeline_window, text='Start Date *')
		self.label_start_date.pack(padx=5, pady=5)
		self.start_date = StringVar()
		self.entry_start_date = Entry(self.timeline_window, textvariable=self.start_date)
		self.entry_start_date.pack(padx=5, pady=5)
		self.entry_start_date.bind('<Return>', self.get_start_date)
		self.entry_start_date.bind('<Key>', self.get_start_date)

		self.label_end_date = Label(self.timeline_window, text='End Date *')
		self.label_end_date.pack(padx=5, pady=5)
		self.end_date = StringVar()
		self.entry_end_date = Entry(self.timeline_window, textvariable=self.end_date)
		self.entry_end_date.pack(padx=5, pady=5)
		self.entry_end_date.bind('<Return>', self.get_end_date)
		self.entry_end_date.bind('<Key>', self.get_end_date)

		self.add_timeline_task_button = Button(self.timeline_window, text=' Add Timeline Task ', command=self.add_timeline_task)
		self.add_timeline_task_button.pack(padx=10, pady=10)

	def add_timeline_task(self):
		description = self.entry_description.get()
		start_date = self.entry_start_date.get()
		end_date = self.entry_end_date.get()
		MessageScreen.add_timeline_task(TimeLine(description, False, start_date, end_date))
		self.timeline_window.destroy()

	def get_start_date(self, event):
		def get_calendar():
			self.start_date.set(calendar.selection_get())
			calendar_window.destroy()
		current_year = int(datetime.date.today().strftime('%Y'))
		current_month = int(datetime.date.today().strftime('%m'))
		current_day = int(datetime.date.today().strftime('%d'))
		calendar_window = Toplevel()
		calendar = Calendar(calendar_window, font='Arial 14', selectmode='day', locale='en_US',
		                         cursor='hand1', year=current_year, month=current_month, day=current_day)
		calendar.pack(fill='both', expand=True)
		ok_button = ttk.Button(calendar_window, text=' OK ', command=get_calendar)
		ok_button.pack(padx=5, pady=5)

	def get_end_date(self, event):
		def get_calendar():
			self.end_date.set(calendar.selection_get())
			calendar_window.destroy()
		current_year = int(datetime.date.today().strftime('%Y'))
		current_month = int(datetime.date.today().strftime('%m'))
		current_day = int(datetime.date.today().strftime('%d'))
		calendar_window = Toplevel()
		calendar = Calendar(calendar_window, font='Arial 14', selectmode='day', locale='en_US',
		                         cursor='hand1', year=current_year, month=current_month, day=current_day)
		calendar.pack(fill='both', expand=True)
		ok_button = ttk.Button(calendar_window, text=' OK ', command=get_calendar)
		ok_button.pack(padx=5, pady=5)

	def start(self):
		return self.timeline_window.mainloop()
