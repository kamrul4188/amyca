class Human:
	def __init__(self, name):
		self.name = name


	def get_name(self):
		return 'my name is : ' + str(self.name)


class Man(Human):

		def __init__(self, name, hand):
			self.hand = hand
			super().__init__(name)

kamru = Man('Kamrul', 'Myhad')
print(kamru.get_name())