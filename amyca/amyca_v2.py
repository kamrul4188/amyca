import sys

class Project:
	def __init__(self, name):
		self.name = name
		self.task = []


class Users:
	total = []

	def __init__(self, user_id, password, access_level):
		self.user_id = user_id
		self.password = password
		self.access_level = access_level
		Users.total.append([self.user_id, self.password, self.access_level])
		#print('Total: ', Users.total)

	@classmethod
	def get_info(self):
		return Users.total


def main():
    while True:
        try:
            kamrul = Users('kamrul', 'kamrul123', 3)
            foo = Users('foo', 'foo123', 2)
            #print(kamrul.user_id)
            print('Call function: ', Users.get_info())
            user_input = input('Please enter value: ')
            print('Your input is: ', user_input)
        except Exception as e:
            print('Sorry, I could not perform that command. Problem:', e)
            sys.exit()




if __name__ == '__main__':
    main()