class User:
	def __init__(self, user, password):
		self.user = user
		self.password = password



	#(first name, last name, street address, city, state, zip, phone,email)
	def __repr__(self):
		return self.user + ' ' + self.password