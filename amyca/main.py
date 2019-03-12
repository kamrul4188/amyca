import sys
import datetime
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
# from tkinter import messagebox

tasks = []

INDEX_ACTIVITY = 0
INDEX_START_DATE = 1
INDEX_END_DATE = 2
INDEX_MANPOWER = 3
INDEX_COST = 4
INDEX_STATUS = 5

DEFAULT_USER_ID = 'admin'
DEFAULT_USER_PW = 'admin123'
DEFAULT_USER_LEVEL = 4

users = [[DEFAULT_USER_ID, DEFAULT_USER_PW, DEFAULT_USER_LEVEL]]
current_user = ['user', 'pw', 0]

USER_LEVEL_1 = 1
USER_LEVEL_2 = 2
USER_LEVEL_3 = 3
USER_LEVEL_4 = 4

INDEX_USER_ID = 0
INDEX_USER_PW = 1
INDEX_USER_LEVEL = 2

MINIMUM_PW_LENGTH = 6
INDEX_OFFSET = 1
NULL = 0


def check_user_level(user_id, user_pw):
    try:
        for i, user in enumerate(users):
            temp_user_id = users[i][INDEX_USER_ID]
            temp_user_pw = users[i][INDEX_USER_PW]
            user_level = users[i][INDEX_USER_LEVEL]
            if temp_user_id == user_id and temp_user_pw == user_pw:
                return user_level

    except ValueError as e:
        raise ValueError(e)


def check_pw_length(user_input):
    if len(user_input) >= MINIMUM_PW_LENGTH:
        password = user_input
        return password
    else:
        raise ValueError('Minimum password length is 6.')


def add_user():
    try:
        new_user_id = input('Please enter new user id: ')
        new_user_pw = check_pw_length(input('Please enter new password with minimum length (6): '))
        new_user_level = confirm_is_number(input('Please enter access level: '))
        users.append([new_user_id, new_user_pw, new_user_level])
        print('>>> You have added ' + new_user_id + ' as user and his/her access level is ' + str(new_user_level))

    except ValueError as e:
        raise ValueError(e)


def print_user():
    print(">>> Here is the list of your user.")
    print('==================================================')
    print(' INDEX | USER ID ')
    print('--------------------------------------------------')
    for i, user in enumerate(users):
        print('   ' + str(i + INDEX_OFFSET) + '   |   ' + str(users[i][INDEX_USER_ID]))
    print('--------------------------------------------------')


def remove_user():
    user_input = confirm_is_number(input('Enter index to delete user: '))
    input_index = user_input - INDEX_OFFSET
    if len(users) < 2:
        raise ValueError('Minimum user should be one.')
    elif input_index < 0:
        raise ValueError('Invalid input !!!')
    else:
        del users[input_index]


def change_password():
    user_input = confirm_is_number(input('Enter index to change password: '))
    input_index = user_input - INDEX_OFFSET
    new_password = check_pw_length(input('Please enter new password with minimum length(6)'))
    users[input_index][INDEX_USER_PW] = new_password


def admin_task():
    if current_user[INDEX_USER_LEVEL] == 4:
        print('''
------------------------------------------------------------------------
Welcome to you in admin panel..............!!!!!!!
Please select your index form the list.:
    1. Add new user <add user>
    2. Delete user <del user>
    3. Change user password  <cp user>
    4. View user index <show user>
    5. To exit admin panel <exit admin>
-------------------------------------------------------------------------''')
        while True:
            print('>>> Enter your admin command')
            admin_input = input()
            if admin_input == 'add user':
                add_user()
            elif admin_input == 'del user':
                remove_user()
            elif admin_input == 'cp user':
                change_password()
            elif admin_input == 'show user':
                print_user()
            elif admin_input == 'exit admin':
                break
            else:
                print('You have entered invalid input. Please try again...')
    else:
        raise ValueError('You have not authorize to add or remove user')


def help_amyca():
    need_help = '''
>>> I'm glad you asked. Here it is:
==================================================
Amyca can understand the following commands:

add DESCRIPTION 
    Adds a task to the list
    Example: add installation air-con 

list
    Lists the tasks in the Task
    
timeline
    To view schedule of task

res
    To view task resource

cost
    To view cost of task and project

admin
    Access to admin panel

add DESCRIPTION
    Add new task/activity 
    Example: add Install air-caon

update INDEX
    Update/edit task parameter 
    Example: update 1
     
task INDEX 
    full detail of teh INDEX task
    Example: task 1
    
done INDEX
    Marks the task at INDEX as 'done'
    Example: done 1
    
logout 
    Logout from user

exit
    Exits the application
-------------------------------------------------- 
'''
    print(need_help.strip(), '\n')


def confirm_is_number(number):
    try:
        number = int(number)
        return number

    except ValueError:
        raise ValueError((str(number) + ' is not a number'))


def format_to_datetime(date):
    date_format = '%d/%m/%Y'
    while True:
        date = date
        try:
            date_obj = datetime.datetime.strptime(date, date_format).date()
            return date_obj
            break
        except ValueError:
            print("Incorrect data format, should be dd/mm/yyyy")
            date = input('Please enter your date again: ')


def datetime_to_print_format(date):
    try:
        print_date = date.strftime("%d %b, %Y")
        return print_date
    except ValueError:
        print('Format of your input is not datetime')


def duration_datetime(start_date, end_date):
    try:
        if end_date >= start_date:
            duration = end_date - start_date
            duration = str(duration).split(',', 1)[0]
            return duration
        else:
            print('Your end date ims earlier than start')
    except ValueError:
        print('Format of your input ins not detetime')


def done_task(user_input):
    new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
    new_input = confirm_is_number(new_input)  # Return as integer
    index_input = new_input - INDEX_OFFSET
    if new_input < 0:
        raise ValueError('Index must be greater than 0')
    else:
        try:
            tasks[index_input][5] = True
            print('>>> Congrats on completing a task! :-)')
        except IndexError:
            raise IndexError('No item at index ' + str(index_input+INDEX_OFFSET))


def print_tasks(user_input):
    new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
    new_input = int(new_input)
    task_index = new_input - INDEX_OFFSET

    task_id = new_input
    activity = tasks[task_index][0]
    start_date = tasks[task_index][1]
    end_date = tasks[task_index][2]
    manpower = tasks[task_index][3]
    cost = tasks[task_index][4]
    status = tasks[task_index][5]

    duration = duration_datetime(start_date, end_date)
    today = datetime.date.today()

    if status:
        status = 'Completed'
    elif start_date > today:
        due_to_start = duration_datetime(today, start_date)
        status = 'Due to start in ' + str(due_to_start)
    elif today > end_date:
        status = 'Task is overdue by ' + duration_datetime(end_date, start_date)
    else:
        status = 'Task on progress'

    print('=======================================================')
    print(' TASK ID      : ' + str(task_id))
    print(' ACTIVITY     : ' + activity)
    print(' START DATE   : ' + datetime_to_print_format(start_date))
    print(' END DATE     : ' + datetime_to_print_format(end_date))
    print(' Duration     : ' + str(duration))
    print(' MANPOWER     : ' + str(manpower))
    print(' COST         : ' + '$' + str(cost))
    print(' STATUS       : ' + status)
    print('=======================================================')


def print_activity():
    if len(tasks) == 0:
        print('>>> Nothing to list')
    else:
        print(">>> Here is the list of tasks:")
        print('==================================================')
        print('STATUS | TASK ID | ACTIVITY')
        print('--------------------------------------------------')
        for i, task in enumerate(tasks):
            if tasks[i][5]:
                print('  ✓ ' + '  |    ' + str(i + 1) + '    | ' + tasks[i][0])
            else:
                print('  ✗ ' + '  |    ' + str(i + 1) + '    | ' + tasks[i][0])
        print('--------------------------------------------------')


def print_cost():
    if len(tasks) == 0:
        print('>>> Nothing to show cost ! Please add your task cost to view.')
    else:
        total_cost = 0
        print('>>> here is your cost details: ')
        print('==================================================')
        print(' TASK ID |  Cost($)')
        print('--------------------------------------------------')
        for i, task in enumerate(tasks):
            task_cost = tasks[i][INDEX_COST]
            total_cost = total_cost + task_cost
            print('    ' + str(i+INDEX_OFFSET) + '    |  ' + '$' + str(task_cost))
        print('--------------------------------------------------')
        print('Total Cost: ' + '$' + str(total_cost))
        print('==================================================')


def print_timeline():
    task_id = []
    duration = []
    if len(tasks) == 0:
        print('>>> Nothing to show on time-line')
    else:
        for i, task in enumerate(tasks):
            index_id = 'Task ID : ' + str(i + 1)
            task_id.append(index_id)

            start_date = tasks[i][1]
            end_date = tasks[i][2]
            task_duration = duration_datetime(start_date, end_date)
            task_duration = str(task_duration).split(' ', 1)[0]
            duration.append(int(task_duration))
            print(str(index_id) + ' >> Duration: ' + str(task_duration) + ' days')

        x_pos = np.arange(len(task_id))
        plt.barh(x_pos, duration, align='center', alpha = 0.5)
        plt.yticks(x_pos, task_id)
        plt.xlabel('days')
        plt.title('Tasks Time Line')
        plt.show()


def print_resource():

    if len(tasks) == 0:
        print('>>> Nothing to show on resource')
    else:
        for i, task in enumerate(tasks):
            index_id = 'Task ID : ' + str(i + 1)
            manpower = tasks[i][3]
            print(str(index_id) + '>> Manpower: ' + str(manpower) + ' Pac')


def confirm_manpower():
    try:
        while True:
            manpower = input('Manpower: ')
            if manpower.isnumeric():
                return manpower
    except ValueError:
        raise ValueError((str(manpower) + ' is not a number'))


def add_task(user_input):
    try:
        if current_user[INDEX_USER_LEVEL] == USER_LEVEL_3 or current_user[INDEX_USER_LEVEL] == USER_LEVEL_2:
            new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
            # 1.ACTIVITY, 1.START DATE, 2.END DATE, 3.MANPOWER, 4.COST, 5.STATUS
            print('----------------------------------------------------------')
            print('You are going to add activity >> ' + new_input + ' >> into to your new task.')
            print('Please enter following details into your task. ')

            task_activity = new_input
            task_start_date = format_to_datetime(input('Start Date (dd/mm/yyyy): '))
            task_end_date = format_to_datetime(input('End Date (dd/mm/yyyy): '))
            task_manpower = confirm_manpower()
            if current_user[INDEX_USER_LEVEL] == USER_LEVEL_3:
                print('enter cost')
                task_cost = confirm_is_number(input('Cost($): '))
            else:
                print('not enter cost')
                task_cost = NULL
                print('Task cost only can add by Project Manager')
        else:
            raise ValueError('You are not authorize to add task !!! ')

        tasks.append([task_activity, task_start_date, task_end_date, task_manpower, task_cost, False])
        print('>>> Activity added to the task')
    except ValueError:
        raise ValueError('Invalid input')


def update_task(user_input):
    """
    update/edit/modify task parameter. from user_input can select which parameter of task update.
    :param user_input: 1.ACTIVITY, 2.START DATE, 3.END DATE, 4.MANPOWER, 5.COST, 6.STATUS
    :return:
    """
    try:
        new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
        task_index = int(new_input) - 1
        print('''
-----------------------------------------------------------------------
please select which following parameter index you would like to update. 
    1. Activity
    2. Start date
    3. End date
    4. Manpower
    5. Cost
    
Enter \'0\' for exit update 
------------------------------------------------------------------------
''')

        while True:
            parameter_input = confirm_is_number(input('Please enter your preference: '))
            parameter_index = parameter_input - INDEX_OFFSET
            if parameter_index == INDEX_ACTIVITY:
                task_activity = input('Update activity: ')
                tasks[task_index][parameter_index] = task_activity
            elif parameter_index == INDEX_START_DATE:
                task_start_date = format_to_datetime(input('Update start date: '))
                tasks[task_index][parameter_index] = task_start_date
            elif parameter_index == INDEX_END_DATE:
                task_end_date = format_to_datetime(input('Update end date: '))
                tasks[task_index][parameter_index] = task_end_date
            elif parameter_index == INDEX_MANPOWER:
                task_manpower = confirm_manpower()
                tasks[task_index][parameter_index] = task_manpower
            elif parameter_index == INDEX_COST and current_user[INDEX_USER_LEVEL] == USER_LEVEL_3:
                task_cost = confirm_is_number(input('Update cost($): '))
                tasks[task_index][parameter_index] = task_cost
            elif parameter_index == INDEX_COST and current_user[INDEX_USER_LEVEL] != USER_LEVEL_3:
                print(' >> Only manager can update cost ')
            elif parameter_index < 0:
                break
            else:
                print('Invalid input')

    except ValueError:
        raise ValueError('Invalid input')


def terminate():
    print('>>> Are you sure? y/n')
    response = input()
    if response.lower() == 'y':
        print(">>> Bye!")
        sys.exit()
    elif response.lower() == 'n':
        print('Welcome back !')
    else:
        raise ValueError('Invalid input')


def log_out():
    """
    This function is called when user command logout. Amyca will resume function main.
    user have to login with user ID and password in order to continue.
    :return:
    """
    main()


def execute_command(command):
    if command == '':
        raise ValueError('You did not input anything')
    elif command == 'exit' or command == 'end':
        terminate()
    elif command == 'help':
        help_amyca()
    elif command == 'list':
        print_activity()
    elif command == 'timeline':
        print_timeline()
    elif command == 'res':
        print_resource()
    elif command == 'cost':
        print_cost()
    elif command == 'logout':
        log_out()
    elif command == 'admin':
        admin_task()
    elif command.startswith('add '):
        add_task(command)
    elif command.startswith('task '):
        print_tasks(command)
    elif command.startswith('done '):
        done_task(command)
    elif command.startswith('update '):
        update_task(command)
    else:
        raise ValueError('command not recognized')


def read_command():
    print('----------------------------------------------------------')
    print(">>> What can I do for you?\n")
    read = input()
    return read


def print_greeting():
    banner = '''    
*****************************************************************************************************
*  __          __  _                            _              __                      _            * 
*  \ \        / / | |                          | |            /  \                    | |           *
*   \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___      / /\ \    _ __ ___  _   _| |  _  ___   *
*    \ \/  \/ / _ \ |/ __/ _ \| '_ ' _ \ / _ \ | __/ _ \    / /__\ \  | '_ ' _ \| | | | |/ / /__ \  *
*     \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |  / /_  _\ \ | | | | | | |_| | | /  _ _) | *
*      \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  /_/      \_\|_| |_| |_|\__, |_|\_\ \___/  *
*                                                                                 __/ |             *
*                                                                                |___/              *
*****************************************************************************************************
    '''
    print(banner.strip(), '\n')


def access_control():
    """ Access control function to control access into Amyca. The function only allow authorize user with
    with right password. Without
    """
    while True:
        try:
            # print('\nCurrent ID: admin, PW: admin123 or ID: kamrul PW: kamrul123\n ')
            user_id = input('Please Enter User ID: ')
            user_pw = input('Please Enter Password: ')
            access_level = check_user_level(user_id, user_pw)
            current_user[INDEX_USER_ID] = user_id
            current_user[INDEX_USER_PW] = user_pw
            current_user[INDEX_USER_LEVEL] = access_level
            print('Access Level: ', access_level)
            if access_level > 0:
                break
        except TypeError:
            print('!!! Invalid user ID or Password !!! Tty again......')


def main():
    access_control()
    print_greeting()

    while True:
        try:
            command = read_command()
            execute_command(command)
        except Exception as e:
            print('Sorry, I could not perform that command. Problem:', e)
            # massage = '''Sorry, I could not perform that command.\n\n Problem: ''' + str(e)
            # messagebox.showinfo('Error...!!!',  massage)


main()
