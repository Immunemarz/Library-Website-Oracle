import cx_Oracle
import pandas as pd
from book import Book

#Note for us!!!
#use clob for the text of the book

# Establish the database connection
class Bookdao:
	def __init__(self):
		self.dsn = cx_Oracle.makedsn('csc325.cjjvanphib99.us-west-2.rds.amazonaws.com', 1521, sid="ORCL")
		self.connection = cx_Oracle.connect(user='rwebber2', password='csrocks55',dsn=self.dsn)
		# Obtain a cursor
		self.cursor = self.connection.cursor()

	def __del__(self):
		self.cursor.close()
		self.connection.close()
	
	def rowToAccount(self,row):
		book = Book(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
		return book
	
	def accountToRow(self,book):
		row = dict(isbn=book.isbn,title=book.title, author = book.author,category=book.category,thumbnail=book.thumbnail, description = book.description,published=book.published,rating=book.rating, pages = book.pages)
		return row
	#category thumbnail description published rating pages
	def insert(self,book):
		sql = "INSERT INTO BOOKS VALUES ('" + str(book.isbn) + "', '" + str(book.title) + "', '" + str(book.author) + "', '" + str(book.category) + "', '" + str(book.thumbnail) + "', '" + str(book.description) + "', '" + str(book.published) + "', '" + str(book.rating) + "', '" + str(book.pages) + "')"
		self.cursor.execute(sql)
		self.connection.commit()

	def delete(self, isbn):
		sql = "delete from BOOKS where isbn='"+str(isbn)+"'"
		print(sql)
		self.cursor.execute(sql)
		self.connection.commit()
	
	def deleteAll(self):
		sql = "delete from BOOKS"
		self.cursor.execute(sql)
		self.connection.commit()
	
	def selectAll(self):
		sql = "select * from BOOKS"
		self.cursor.execute(sql)
		BOOKS=[]
		while True:
			row = self.cursor.fetchone()
			if row is None:
				break
			account = self.rowToAccount(row)
			BOOKS.append(account)
		return BOOKS
			
	
	def selectByIsbn(self,isbn):
		sql = "select * from BOOKS where isbn='"+isbn+"'"
		print(sql)
		self.cursor.execute(sql) 
		row = self.cursor.fetchone()
		if row!= None:
			#print(row)
			user = self.rowToAccount(row)
			return user
		return None

	def selectByTitle(self,title):
		sql = "select * from BOOKS where title='"+title+"'"
		print(sql)
		self.cursor.execute(sql) 
		row = self.cursor.fetchone()
		if row!= None:
			#print(row)
			user = self.rowToAccount(row)
			return user
		return None	

	def selectByThumbnail(self,thumbnail):
		sql = "select * from BOOKS where thumbnail='"+thumbnail+"'"
		print(sql)
		self.cursor.execute(sql) 
		row = self.cursor.fetchone()
		if row!= None:
			#print(row)
			user = self.rowToAccount(row)
			return user
		return None	
	
	def update(self, book):
		print(book)
		sql = f"UPDATE BOOKS SET isbn='{book.isbn}', title='{book.title}', author='{book.author}', category='{book.category}', thumbnail='{book.thumbnail}', description='{book.description}', published='{book.published}', rating='{book.rating}', pages='{book.pages}' WHERE isbn='{book.isbn}'"
		self.cursor.execute(sql)
		self.connection.commit()
	
	def populate(self):
		self.deleteAll()
		#book = Book('Magic Tree House', 'nathanael stahl','6178201159')
		#self.insert(book)
		df = pd.read_csv('books.csv')

		# Iterate over the rows of the DataFrame
		for index, row in df.iterrows():
			#print(row['isbn'], row['title'], row['authors'], row['categories'], row['thumbnail'], row['description'], str(row['published']), str(row['rating']) + '\n')
			# Create a Book object for each row
			book = Book(str(row['isbn']), row['title'].lower(), row['authors'], row['categories'], row['thumbnail'], row['description'], str(row['published']), str(row['rating']), str(row['pages']))
			
			self.insert(book)
