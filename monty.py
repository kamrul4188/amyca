# Monty for is updated as week 4.
import sys

items = []


def print_items():
    if len(items) == 0:
        print('>>> Nothing to list')
    else:
        print(">>> List of items:")
        for i, item in enumerate(items):
            print("   ", str(i + 1) + '.', items[i])


def add_item(user_input):
    # items_len = len(items)
    # print(items_len)
    new_input = user_input.split(" ", 1)[1]  # remove first word 'add' from the input
    # print (new_input)
    items.append(new_input)


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
    else:
        print('>>> OOPS! Unknown command')


def print_greeting():
    print(">>> Hello, my name is Monty")


def read_command():
    print(">>> What can I do for you?\n")
    read = input()
    return read


def main():
    print_greeting()
    while True:
        command = read_command()
        execute_command(command)
main()

