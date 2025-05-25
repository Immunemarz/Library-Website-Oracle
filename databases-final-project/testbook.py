from book import Book
from bookdao import Bookdao
import pandas as pd
df = pd.read_csv('books.csv')

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
	print(row['isbn'])
	# Create a Book object for each row
	book = Book(row['isbn'], row['title'], row['authors'], row['category'], row['thumbnail'], row['description'], row['published'], row['rating'], row['pages'])

dao = Bookdao()
#new_book = dao.selectByIsbn('7205589')
#print(new_book)