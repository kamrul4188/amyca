# Amyca - Project Management Assistance
### It has been build as project requirement of TE3201 - Software Engineering of National University of Singapore


## Project Naming:

The software to help the project team to run the project smoothly.
As our software is part of the project team as assistance, So we get a lovely Name.
The latin female form of Amicus of Latin Origin: Meaning: Female friend or Friendly, Loving Woman
Form latin Amicus to English Amyca. We have selected name of our software is Amyca
`[Amyca - Project Management Assistance]`

## Basic Functionality:

1. Initially Amyca interface build in text-base than updated `Graphical User Interface (GUI)`.
2. Amyca and storing and retrieving various data type is require to project management. following are:
	 eg: todo, deadline, timeline, resource and cost
3. Amyca is not understand natural language but command format most likely as natural and user friendly.
	but user require to follow those strict format. more information you can found on help menu.	
	`Example: cost of DESCRIPTION is AMOUNT`
4. Amyca data stored into hard disk.
	* Project and user data stored as .csv
	* Logging data stored as .log
	* Documentation data stored as .txt

## Additional Functionality:

1. **Timeline as graph:** User can view all of there timeline task as graph by just clicking TimeLine menu
2. **View Calender:** User can view calender in monthly view. Pup up in current date by clicking can be view as needed.
3. **Multiple Users:** Multiple users is support by Amyca. Amyca has four user access levels.

	1. Team Member: `Access Level = 1`
	2. Team Leader: `Access Level = 2`
	3. Project Manager: `Access Level = 3`
	4. System Admin: `Access Level = 4`

4. **Password:** Amyca has posword policy to stored password not understandable by users.
	1. `Minimum length of password is 6`. Amyca not add user with below minimum length.
	2. Stored user particular into hard disk with `password as hash (encrypted)`
	
## Command
Amyca can understand the following commands:

```
todo DESCRIPTION
    Adds a todo task into the task list
    Example: todo read book

deadline DESCRIPTION by DEADLINE
    Adds a deadline task into the task list
    Example: deadline read book by tomorrow

timeline DESCRIPTION from DATE to DATE
    Adds a timeline task into the task list
    Example: timeline borrow book from 30/04/2019 to 30/05/2019

resource DESCRIPTION is QUANTITY PREFIX
    Adds resource into resource list
    Example: resource manpower is 10 pack

cost of DESCRIPTION is AMOUNT
    adds cost into cost list
    example: cost of manpower is 10000

done INDEX
    Marks the task at index as 'done'
    Example: done 1

pending INDEX
    Marks the task at index as 'pending'
    Example: pending 1

remove task INDEX
    Remove task as indexed from task list
    Example: remove task 1

remove resource INDEX
    Remove resource as indexed from the resource list
    Example: remove resource 1

remove cost INDEX
    Remove cost as indexed from the cost list
    Example: remove cost 1

exit
    Exits the application
 ```
 