from bookdao import Bookdao
from book import Book
from user import User

# start with populate
print("populate: ")
dao = Bookdao()
dao.populate()

# select
print("select all:")
accounts = dao.selectAll()
print(accounts)

# insert
print("insert: ")
account = Book('test book', 'sam gotee', '2729283291')
dao.insert(account)
accounts = dao.selectAll()
print(accounts)

# select by email
print("select by email: ")
account = dao.selectByIsbn('6178291199')
print(account)

# update
print("update:")
print(account)
account.title = 'this book title should be changed'
dao.update(account)
accounts = dao.selectAll()
print(accounts)

# delete
print("delete:")
dao.delete(account.isbn)
accounts = dao.selectAll()
print(accounts)