# amyca


- Module Name : amyca
- Module Type : root
- Github      : https://github.com/kamrul4188/amyca


The software named  is 'Amyca' - Project Management Assistance
It has been build as project requirement of TE3201 - Software Engineering of National University of Singapore


Project Naming:
---------------
The software to help the project team to run the project smoothly.
As our software is part of the project team as assistance, So we get a lovely Name.
The latin female form of Amicus of Latin Origin: Meaning: Female friend or Friendly, Loving Woman
Form latin Amicus to English Amyca. We have selected name of our software is Amyca
[Amyca - Project Management Assistance]

Basic Functionality:
--------------------
1. Initially Amyca interface build in text-base than updated Graphical User Interface (GUI).
2. Amyca and storing and retrieving various data type is require to project management. following are:
 eg: todo, deadline, timeline, resource and cost
3. Amyca is not understand natural language but command format most likely as natural and user friendly.
 but user require to follow those strict format. more information you can found on help menu.
 Example: cost of DESCRIPTION is AMOUNT
4. Amyca data stored into hard disk.
 a. Project and user data stored as .csv
 2. Logging data stored as .log
 3. Documentation data stored as .txt

Additional Functionality:
-------------------------
1. Timeline as graph: User can view all of there timeline task as graph by just clicking TimeLine menu
2. View Calender: User can view calender in monthly view. Pup up in current date by clicking can be view as needed.
3. Multiple Users: Multiple users is support by Amyca. Amyca has four user access levels.
 a. Team Member: Access Level = 1
 b. Team Leader: Access Level = 2
 c. Project Manager: Access Level = 3
 d. System Admin: Access Level = 4
4. Password: Amyca has posword policy to stored password not understandable by users.
 a. Minimum length of password is 6. Amyca not add user with below minimum length.
 b. Stored user particular into hard disk with password as hash (encrypted)


 NOTE: Default User: admin, Password: admin123


## MainScreen
```python
MainScreen(self)
```

The class MainScreen si Main user interface.
All project tasks, resources and cost viable as main screen.
Added menu bar with addition functionality as require by project
 eg:  file, user, TimeLine, Calender, Help, and Amyca

### start
```python
MainScreen.start(self)
```
This function is for call main loop for starting GUI
### start_logging
```python
MainScreen.start_logging(self)
```
This function is initial configuration of logging module
### load_data
```python
MainScreen.load_data(self)
```
This function called during runtime to load project date from hard disk to project list
### save_data
```python
MainScreen.save_data(self)
```
This function to save project data form project list to hard dive
### add_user
```python
MainScreen.add_user(self)
```
This function to add user to amyca
### logout
```python
MainScreen.logout(self)
```

This function is called at Menu bar>User>Logout button click
To execute: destroy current and window and pop up login window
Registered user only can login to access Amyca

### get_calendar
```python
MainScreen.get_calendar(self)
```
This function is to view calendar
### get_timeline_graph
```python
MainScreen.get_timeline_graph(self)
```

This function to call for display timeline object as graph
timeline object is a task with start and end date of task

### help
```python
MainScreen.help(self)
```
This function is call to show/display help info
### get_log
```python
MainScreen.get_log(self)
```

This function is called to display logging.
Open log file form hard disk as read only mode.
File stored in hard disk as .log format

### get_about_developer
```python
MainScreen.get_about_developer(self)
```

This function is call to display developer personal and contract information.
File stored in hard disk as .txt format

### get_about_amyca
```python
MainScreen.get_about_amyca(self)
```

This function is call to display software information
File stored in .txt format. and open file as read mode

### get_current_time
```python
MainScreen.get_current_time(self)
```

This function is to get current time as datetime format
:return: current time

### clear_input_box
```python
MainScreen.clear_input_box(self)
```
This function is for clear input box
### update_chat_history
```python
MainScreen.update_chat_history(self, command, response, status_format)
```

This function is update chat history and display with following parameter
:param command: command entered by user in command window
:param response: return response form execute function
:param status_format: tag: normal_format, success_format, error_format.

### update_task_list
```python
MainScreen.update_task_list(self, tasks)
```

This function is to update task list into display  as string
:param tasks: Project task list

### update_resource_list
```python
MainScreen.update_resource_list(self, resources)
```

This function is to update project resources list into display as string
:param resources: project resources

### update_cost_list
```python
MainScreen.update_cost_list(self, cost_list)
```

This function is to update project cost list into display as string
:param cost_list: project cost list

### command_entered
```python
MainScreen.command_entered(self, event)
```

This function is event interrupt function.
At command enter window press enter to call this function
:param event: command

### remove_from_word
```python
MainScreen.remove_from_word(self, text, word)
```

This function is to break a string by key word
:param text: Input string to be break
:param word: Key word to break the string
:return: first part of string

### remove_to_word
```python
MainScreen.remove_to_word(self, text, word)
```

This function is to break the string by key word
:param text: input string to be break
:param word: last part of the string
:return:

### execute_command
```python
MainScreen.execute_command(self, command)
```

This function is to execute the command entered
Do pre processing before call the execution function is need
:param command: Command entered
:return: value form execute function

## LoginScreen
```python
LoginScreen(self)
```
This is for GUI window for user login
### start
```python
LoginScreen.start(self)
```
This function is for call mainloop for starting GUI
### verify_user_login
```python
LoginScreen.verify_user_login(self)
```
Tins function is to verify valid user in registered in database
### login_success
```python
LoginScreen.login_success(self)
```

This function is call after get successfully verify a valid users
This function will kil login window screed and call welcome/greeting window
Get ack form greeting window to start MainScreen window

## AddUserScreen
```python
AddUserScreen(self, project)
```
This class is as GUI to add new user
### add_user
```python
AddUserScreen.add_user(self)
```
Ths function is to execute user object
### start
```python
AddUserScreen.start(self)
```
This function is for call mainloop for starting GUI
## RemoveUserScreen
```python
RemoveUserScreen(self)
```
This class is a GUI to remove user
### remove_user
```python
RemoveUserScreen.remove_user(self)
```
This function is called user remove method
### start
```python
RemoveUserScreen.start(self)
```
This function is for call mainloop for starting GUI
## ChangePasswordScreen
```python
ChangePasswordScreen(self)
```
This cass is GUI to change password
### change_password
```python
ChangePasswordScreen.change_password(self)
```
This function call user to change password method
### start
```python
ChangePasswordScreen.start(self)
```
This function is for call mainloop for starting GUI
