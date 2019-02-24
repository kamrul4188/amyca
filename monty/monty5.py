# Monty for is updated as week 4.
import sys

items = []


def print_items():
    if len(items) == 0:
        print('>>> Nothing to list')
    else:
        print(">>> List of items:")
        for i, item in enumerate(items):
            if items[i][1] == True:
                print("   ", '[✓] ' + str(i + 1) + '.', items[i][0])
            else:
                print("   ", '[✗] ' + str(i + 1) + '.', items[i][0])


def add_item(user_input):
    new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
    items.append([new_input, False])


def done_item (user_input):
    new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
    new_input = confirm_is_number(new_input)  # Return as integer
    new_input = new_input - 1
    if new_input < 0:
        raise ValueError('Index must be greather than 0')
    else:
        try:
            items[new_input][1] = True
        except IndexError:
            raise IndexError('No item at index ' + str(new_input+1))


def confirm_is_number(number):
    try:
        number = int(number)
        return number
    except ValueError:
        raise ValueError((str(number) + ' is not a number'))


def terminate():
    print('>>> Are you sure? y/n')
    response = input()
    if response == 'y':
        print(">>> Bye!")
        sys.exit()


def execute_command(command):
    if command == '':
        return
    elif command == 'exit':
        terminate()
    elif command == 'list':
        print_items()
    elif command.startswith('add '):
        add_item(command)
    elif command.startswith('done '):
        done_item(command)
    else:
        raise ValueError('command not recognized')


def print_greeting():
    print(">>> Hello, my name is Monty")


def read_command():
    print(">>> What can I do for you?\n")
    read = input()
    return read


def main():
    print_greeting()
    while True:
        try:
            command = read_command()
            execute_command(command)
        except Exception as e:
            print('>>> SORRY, I could not perform that command. Problem:', e)


main()


