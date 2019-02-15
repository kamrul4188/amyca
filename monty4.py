import sys

items = []


def print_items():
    if len(items) == 0:
        print('>>> Nothing to list')
    else:
        for i, item in enumerate(items):
          print(i,'.', items[i])
            # ...


def add_item(user_input):
    items = user_input
    print(items.index)    
    items.append(user_input)
    
    


def terminate():
    print('>>> Are you sure? y/n')
    response = input()
    return response == 'y'


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
  print (">>> Hello, my name is Monty")
  
def read_command():
  print (">>> What can I do for you?")
  read = input()
  return read

def main():
    print_greeting()
    while True:
        command = read_command()
        execute_command(command)


main()
