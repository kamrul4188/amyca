import sys

def is_exit_confirmed():
    print('>>> Are you sure? y/n')
    response = input()
    return response == 'y'


def execute_command(command):
    if command == 'list':
      print(">>> Nothing to list")
      #sys.exit()
        #return
    elif command == 'foo':
      print(">>> OOPS! Unknown command")
    
    elif command == 'exit':
        if is_exit_confirmed():
            print('>>> Bye!')
            sys.exit()
    # ...
    
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
