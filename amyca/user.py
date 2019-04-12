import password as pw


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

	def remove(cls, name):
		# Todo: add functionality to remove user
		pass

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
