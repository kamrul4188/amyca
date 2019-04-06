import datetime
from tkinter import *

import sys


class GUI:

    def __init__(self, task_manager):
        self.task_manager = task_manager
        self.window = Tk()
        self.window.geometry('800x700')  # set Window size
        self.window.title('Monty')  # set Window title

        self.input_box = Entry(self.window)  # create an input box
        self.input_box.pack(padx=5, pady=5, fill='x')  # make the input box fill the width of the Window
        self.input_box.bind('<Return>', self.command_entered)  # bind the command_entered function to the Enter key
        self.input_box.focus()  # set focus to the input box

        # add a text area to show the chat history
        self.history_area = Text(self.window, width="50")
        self.history_area.pack(padx=5, pady=5, side=LEFT, fill="y")
        self.output_font = ('Courier New', 12)
        self.history_area.tag_configure('error_format', foreground='red', font=self.output_font)
        self.history_area.tag_configure('success_format', foreground='green', font=self.output_font)
        self.history_area.tag_configure('normal_format', font=self.output_font)

        # add a text area to show the list of tasks
        self.list_area = Text(self.window)
        self.list_area.pack(padx=5, pady=5, side=RIGHT, fill="both")
        self.list_area.tag_configure('normal_format',  font=self.output_font)
        self.list_area.tag_configure('pending_format', foreground='red', font=self.output_font)
        self.list_area.tag_configure('done_format', foreground='green', font=self.output_font)

        # show the welcome message and the list of tasks
        self.update_chat_history('start', 'Welcome to Monty!', 'success_format')
        self.update_task_list(self.task_manager.items)

    def update_chat_history(self, command, response, status_format):
        """
        status_format: indicates which color to use for the status message
          can be 'error_format', 'success_format', or 'normal_format'
        """
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.history_area.insert(1.0, '-' * 40 + '\n', 'normal_format')
        self.history_area.insert(1.0, '>>> ' + response + '\n', status_format)
        self.history_area.insert(1.0, 'You said: ' + command + '\n', 'normal_format')
        self.history_area.insert(1.0, current_time + '\n', 'normal_format')

    def update_task_list(self, tasks):
        self.list_area.delete('1.0', END)  # clear the list area
        for i, task in enumerate(tasks):
            if task[1]:
                icon = '✓'
                output_format = 'done_format'
            else:
                icon = '✗'
                output_format = 'pending_format'
            self.list_area.insert(END, icon + ' ' + str(i+1) + ' ' + task[0] + '\n', output_format)

    def clear_input_box(self):
        self.input_box.delete(0, END)

    def command_entered(self, event):
        command = None
        try:
            command = self.input_box.get()
            if command.strip().lower() == 'exit':
                sys.exit()
            output = self.task_manager.execute_command(command)
            self.update_chat_history(command, output, 'success_format')
            self.update_task_list(self.task_manager.items)
            self.clear_input_box()
        except Exception as e:
            self.update_chat_history(command, str(e) + '\n' + self.task_manager.get_help(), 'error_format')

    def start(self):
        self.window.mainloop()


class TaskManager:
    def __init__(self):
        self.items = [
            ['task 1', True],
            ['task 2', False],
            ['task 3', True]
        ]

    def get_help(self):
        return 'help:\n...'

    def execute_command(self, command):
        if command == 'help':
            return self.get_help()
        elif command.startswith('add '):
            self.items.append([command[4:], False])
            return 'task added'
        else:
            raise Exception('Command not recognized')


GUI(TaskManager()).start()