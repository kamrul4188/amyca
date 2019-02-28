import sys


def print_greeting():
    print('*******************************************************')
    print('Welcome! I am Amyca your project management assistance.')
    print('*******************************************************')


def read_command():
    print('What can I do for you ?\n')
    read = input()
    return read


def terminate():
    print('>>> Are you sure? y/n')
    response = input()
    if response == 'y':
        print(">>> Bye!")
        sys.exit()


def execute_command(command):
    if command == '':
        raise ValueError('You did not input anything')
    elif command == 'exit' or command == 'end':
        terminate()
    elif command == 'list':
        pass # print_items()
    elif command.startswith('add '):
        pass # add_item(command)
    elif command.startswith('done '):
        pass # done_item(command)
    else:
        raise ValueError('command not recognized')


def main():
    print_greeting() # Welcome massage here
    while True:
        try:
            command = read_command()  # To read user input
            execute_command(command)  # Execute user command
        except Exception as e:
            print('Sorry, I could not perform that command. Problem: ', e)


main()
