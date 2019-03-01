import sys


tasks = []  # 0.ACTIVITY, 1.START DATE, 2.END DATE, 3.MANPOWER, 4.COST, 5.STATUS


def confirm_is_number(number):
    try:
        number = int(number)
        return number
    except ValueError:
        raise ValueError((str(number) + ' is not a number'))


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
    if tasks[task_index][5]:
        task_status = 'Completed'
    else:
        task_status = 'Not Completed'
    print('=======================================================')
    print(' TASK ID      : ' + str(new_input))
    print(' ACTIVITY     : ' + tasks[task_index][0])
    print(' START DATE   : ' + tasks[task_index][1])
    print(' END DATE     : ' + tasks[task_index][2])
    print(' MANPOWER     : ' + tasks[task_index][3])
    print(' COST         : ' + '$' + tasks[task_index][4])
    print(' STATUS       : ' + task_status)
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


def add_task(user_input):
    new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
    # 1.ACTIVITY, 1.START DATE, 2.END DATE, 3.MANPOWER, 4.COST, 5.STATUS
    print('----------------------------------------------------------')
    print('You are going to add activity >> ' + new_input + ' >> into to your new task.')
    print('Please enter following details:  ')
    try:
        task_activity = new_input
        task_start_date = input('Start Date (dd/mm/yy): ')
        task_end_date = input('End Date (dd/mm/yy): ')
        task_manpower = input('Manpower: ')
        task_cost = input('Cost($): ')

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
    elif command == 'list':
        print_activity()
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

def main():
    print_greeting() # Welcome massage here
    while True:
        try:
            command = read_command()
            execute_command(command)
        except Exception as e:
            print('Sorry, I could not perform that command. Problem:', e)


main()
