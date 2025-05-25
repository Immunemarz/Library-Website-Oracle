import cx_Oracle
import pandas as pd
from ownedbook import OwnedBook

#Note for us!!!
#use clob for the text of the book

# Establish the database connection
class Ownedbooksdao:
	def __init__(self):
		self.dsn = cx_Oracle.makedsn('csc325.cjjvanphib99.us-west-2.rds.amazonaws.com', 1521, sid="ORCL")
		self.connection = cx_Oracle.connect(user='rwebber2', password='csrocks55',dsn=self.dsn)
		# Obtain a cursor
		self.cursor = self.connection.cursor()

	def __del__(self):
		self.cursor.close()
		self.connection.close()
	
	def rowToAccount(self,row):
		book = OwnedBook(row[0],row[1])
		return book
	
	def accountToRow(self,book):
		row = dict(email = book.email,isbn=book.isbn)
		return row
	#category thumbnail description published rating pages
	def insert(self,book):
		sql = "INSERT INTO ownedbooks VALUES ('" + str(book.email) + "', '" + str(book.isbn) +  "')"
		self.cursor.execute(sql)
		self.connection.commit()

	def delete(self, isbn,user):
		sql = "DELETE FROM ownedbooks WHERE email = '" + str(user) + "' AND isbn = '" + str(isbn) + "'"
		print(sql)
		self.cursor.execute(sql)
		self.connection.commit()
	
	def deleteAll(self):
		sql = "delete from ownedbooks"
		self.cursor.execute(sql)
		self.connection.commit()
	
	def selectAll(self,user):
		sql = "select * from ownedbooks where email ='"+str(user)+"'"
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
	
	def update(self, book):
		print(book)
		sql = f"UPDATE ownedbooks SET email='{book.email}', isbn='{book.isbn}' WHERE isbn='{book.isbn}'"
		self.cursor.execute(sql)
		self.connection.commit()
	
	def populate(self):
		self.deleteAll()
		#book = Book('Magic Tree House', 'nathanael stahl','6178201159')
		#self.insert(book)
		account = OwnedBook('bdugan@stonehill.edu','0006551394')
		self.insert(account)
		account = OwnedBook('rgoodreau@students.stonehill.edu','000664600X')
		self.insert(account)
		account = OwnedBook('nstahl@students.stonehill.edu','0007117531')
		self.insert(account)
