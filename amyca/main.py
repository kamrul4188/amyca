import sys
import datetime
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# from tkinter import messagebox

tasks = []  # 0.ACTIVITY, 1.START DATE, 2.END DATE, 3.MANPOWER, 4.COST, 5.STATUS

# Access Level : 1.Team Member, 2.Team Leader, 3.Project Manger, 4.System Admin
access_level = 0

# [usr_id, password, access_level]
users = [['admin', 'admin123', 4], ['kamrul', 'kamrul123', 3], ['abdullah', 'abdullah123', 2], ['xiao','xiao123', 1]]


def check_user_level(user_id, user_pw):
    try:
        for i, user in enumerate(users):
            temp_user_id = users[i][0]
            temp_user_pw = users[i][1]
            set_user_level = users[i][2]

            if temp_user_id == user_id and temp_user_pw == user_pw:
                return set_user_level

    except ValueError as e:
        raise ValueError(e)


def add_user():
    if access_level == 4:
        new_user_id = input('Please enter new user id: ')
        new_user_pw = input('Please enter new password: ')
        new_user_level = input('Please enter access level: ')
        users.append([new_user_id, new_user_pw, new_user_level])
    else:
        print('You have not authorize to add or remove user')


def help_amyca():
    need_help = '''
>>> I'm glad you asked. Here it is:
==================================================
Amyca can understand the following commands:

add DESCRIPTION 
    Adds a task to the list
    Example: add installation aircon 

list
    Lists the tasks in the Task
     
task INDEX 
    full detail of teh INDEX task
    Example: task 1
    
done INDEX
    Marks the task at INDEX as 'done'
    Example: done 1

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
    new_input = new_input - 1
    if new_input < 0:
        raise ValueError('Index must be greater than 0')
    else:
        try:
            tasks[new_input][5] = True
            print('>>> Congrats on completing a task! :-)')
        except IndexError:
            raise IndexError('No item at index ' + str(new_input+1))


def print_tasks(user_input):
    new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
    new_input = int(new_input)
    task_index = new_input - 1

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
        status = 'Due to start in' + str(due_to_start)
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


def timeline_task():
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
        #plt.xticks(x_pos, task_id)
        plt.xlabel('days')
        #plt.ylabel('days')
        plt.title('Tasks Time Line')
        plt.show()


def confirm_manpower():
    try:
        while True:
            manpower = input('Manpower: ')
            if manpower.isnumeric():
                return manpower
    except ValueError:
        raise ValueError((str(manpower) + ' is not a number'))


def add_task(user_input):
    new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
    # 1.ACTIVITY, 1.START DATE, 2.END DATE, 3.MANPOWER, 4.COST, 5.STATUS
    print('----------------------------------------------------------')
    print('You are going to add activity >> ' + new_input + ' >> into to your new task.')
    print('Please enter following details into your task. ')
    try:
        task_activity = new_input
        task_start_date = format_to_datetime(input('Start Date (dd/mm/yyyy): '))
        task_end_date = format_to_datetime(input('End Date (dd/mm/yyyy): '))
        # task_manpower = confirm_is_number(input('Manpower: '))
        task_manpower = confirm_manpower()
        if access_level == 3:
            task_cost = confirm_is_number(input('Cost($): '))
        else:
            task_cost = 0
            print('Task cost only can add by Project Manager')

        tasks.append([task_activity,task_start_date,task_end_date,task_manpower,task_cost, False])  # Added new items to list
        print('>>> Activity added to the task')
    except ValueError:
        raise ValueError('Invalid input')


def terminate():
    print('>>> Are you sure? y/n')
    response = input()
    if response == 'y':
        print(">>> Bye!")
        sys.exit()
    elif response == 'n':
        print('Welcome back !')
    else:
        raise ValueError('Invalid input')


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
        timeline_task()
    elif command.startswith('task '):
        print_tasks(command)
    elif command.startswith('add '):
        add_task(command)
    elif command.startswith('done '):
        done_task(command)
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
            if access_level > 0:
                break
        except TypeError:
            print('!!! Invalid user ID or Password !!! Tty again......')


def main():
    access_control()
    print_greeting() # Welcome massage here

    while True:
        try:
            command = read_command()
            execute_command(command)
        except Exception as e:
            print('Sorry, I could not perform that command. Problem:', e)
            # massage = '''Sorry, I could not perform that command.\n\n Problem: ''' + str(e)
            # messagebox.showinfo('Error...!!!',  massage)


main()
