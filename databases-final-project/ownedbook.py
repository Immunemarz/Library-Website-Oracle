class OwnedBook:
	def __init__(self, email, isbn):
		self.email = email
		self.isbn = isbn

		
#category thumbnail description published rating pages
#9 total

	#(first name, last name, street address, city, state, zip, phone,email)
	def __repr__(self):
		return str(self.isbn) + ' ' + str(self.email)