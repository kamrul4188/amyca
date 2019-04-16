import password as pw
import csv


class User:
	__users = []
	__total = 0
	__current_user_name = ''
	__current_user_level = 0

	INDEX_USER_NAME = 0
	INDEX_USER_PASSWORD = 1
	INDEX_USER_ACCESS_LEVEL = 2

	def __init__(self, user_name, password, access_level):
		self.__user_name = user_name
		self.__password = pw.Password.hash(password)
		self.__access_level = int(access_level)
		User.__total = User.__total + 1
		User.__users.append([self.__user_name, self.__password, self.__access_level])

	@classmethod
	def verify(cls, name, password):
		try:
			for i, user in enumerate(cls.__users):
				temp_user_name = cls.__users[i][cls.INDEX_USER_NAME]
				temp_user_password = cls.__users[i][cls.INDEX_USER_PASSWORD]
				temp_user_access_level = cls.__users[i][cls.INDEX_USER_ACCESS_LEVEL]
				if temp_user_name == name and pw.Password.verify(temp_user_password, password):
					cls.__current_user_name = temp_user_name
					cls.__current_user_level = temp_user_access_level
					return True
		except IndexError:
			raise IndexError('Index is our of range')

	@classmethod
	def remove(cls, name, password):
		user_name = name
		user_password = password
		for i, user in enumerate(cls.__users):
			if cls.verify(user_name, user_password):
				del cls.__users[i]
				return '[' + user_name + '] has been remove from user.'

		return '[' + user_name + '] Not exit in user list'

	@classmethod
	def change_password(cls, name, current_password, new_password):
		user_name = name
		current_password = current_password
		new_password = pw.Password.hash(new_password)
		for i, user in enumerate(cls.__users):
			if cls.verify(user_name, current_password):
				cls.__users[i][1] = new_password
				return 'Password Change for user [ ' + user_name + ' ]'
		return 'Username or password not match'

	@classmethod
	def get_total(cls):
		return cls.__total

	@classmethod
	def get_current_user_name(cls):
		return cls.__current_user_name

	@classmethod
	def get_current_user_access_level(cls):
		return cls.__current_user_level

	@classmethod
	def get_users(cls):
		return User.__users

	@classmethod
	def save_as_csv(cls, storage):
		output_file = open(storage, 'w', newline='')
		output_writer = csv.writer(output_file)
		for user in User.__users:
			output_writer.writerow(user)
		output_file.close()
		return 'User info save'

	@classmethod
	def load_form_csv(cls, storage):
		file = open(storage)
		deliveries_reader = csv.reader(file)
		for row in deliveries_reader:
			User.__users.append([row[0], row[1], row[2]])
		file.close()

		return 'User is loaded'


	def __str__(self):
		return 'New User added. [' + self.__user_name + ']'


if __name__ == '__main__':
	#User('admin', 'admin123', 4)
	#User('kamrul', 'kamrul123', 3)
	#print(User.get_users())
	#User.remove('admin', 'admin123')
	#User.change_password('admin', 'admin123', '123456')
	#print('After: ', User.get_users())
	#User.save_as_csv('program_data/users.csv')
	print('befour load', User.get_users())
	User.load_form_csv('program_data/users.csv')
	print('After load', User.get_users())


