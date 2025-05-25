import cx_Oracle
import sys
from user import User

# Establish the database connection
class Userdao:
	def __init__(self):
		self.dsn = cx_Oracle.makedsn('csc325.cjjvanphib99.us-west-2.rds.amazonaws.com', 1521, sid="ORCL")
		self.connection = cx_Oracle.connect(user='rwebber2', password='csrocks55',dsn=self.dsn)
		# Obtain a cursor
		self.cursor = self.connection.cursor()

	def __del__(self):
		self.cursor.close()
		self.connection.close()
	
	def rowToAccount(self,row):
		account = User(row[0],row[1])
		return account
	
	def accountToRow(self,account):
		row = dict(user=account.user, password = account.password)
		return row

	def insert(self,account):
		#print('books:',account.books,file = sys.stderr
		sql = "insert into USERS values (\'" + account.user + "\', \'" + account.password + "\')"
		self.cursor.execute(sql)
		self.connection.commit()

	def delete(self, email):
		sql = "delete from USERS where user='"+user+"'"
		print(sql)
		self.cursor.execute(sql)
		self.connection.commit()
	
	def deleteAll(self):
		sql = "delete from USERS"
		self.cursor.execute(sql)
		self.connection.commit()
	
	def selectAll(self):
		sql = "select * from USERS"
		self.cursor.execute(sql)
		users=[]
		while True:
			row = self.cursor.fetchone()
			if row is None:
				break
			account = self.rowToAccount(row)
			users.append(account)
		return users
			
	
	def selectByEmail(self,user):
		sql = "select * from USERS where email='"+user+"'"
		print(sql)
		self.cursor.execute(sql) #i think theres an error because its not in the database, cant put in cause no dbeaver though 
		row = self.cursor.fetchone()
		if row!= None:
			#print(row)
			user = self.rowToAccount(row)
			return user
		return None


	
	def update(self, account):

		sql = f"UPDATE USERS SET email='{account.user}', password='{account.password}' WHERE email='{account.user}'"
		self.cursor.execute(sql)
		self.connection.commit()
	#(first name, last name, street address, city, state, zip, phone,email)
	def populate(self):
		self.deleteAll()
		account = User('bdugan@stonehill.edu','csrocks55')
		self.insert(account)
		account = User('rgoodreau@students.stonehill.edu','ryanrocks55')
		self.insert(account)
		account = User('nstahl@students.stonehill.edu','naterocks55')
		self.insert(account)
