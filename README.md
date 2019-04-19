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

## LoginScreen
```python
LoginScreen(self)
```
This is for GUI window for user login
## AddUserScreen
```python
AddUserScreen(self, project)
```
This class is as GUI to add new user
## RemoveUserScreen
```python
RemoveUserScreen(self)
```
This class is a GUI to remove user
## ChangePasswordScreen
```python
ChangePasswordScreen(self)
```
This cass is GUI to change password
