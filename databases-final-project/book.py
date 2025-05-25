class Book:
	def __init__(self, isbn,title,author,category,thumbnail,description,published,rating,pages):
		self.isbn = isbn
		self.title = title
		self.author = author
		self.category = category
		self.thumbnail = thumbnail
		self.description = description
		self.published = published
		self.rating = rating
		self.pages = pages
		
#category thumbnail description published rating pages
#9 total

	#(first name, last name, street address, city, state, zip, phone,email)
	def __repr__(self):
		return str(self.isbn) + ' ' + str(self.title) + ' ' + str(self.author) + ' ' + str(self.category) + ' ' + str(self.thumbnail) + ' ' + str(self.description) + ' ' + str(self.published) + ' ' + str(self.rating) + ' ' + str(self.pages)