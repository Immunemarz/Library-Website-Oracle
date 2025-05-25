import sys
from jsonpickle import encode
from jsonpickle import decode
from flask import Flask
from flask import abort, redirect, url_for
from flask import request
from flask import render_template
from flask import session
from flask import flash
from user import User
from userdao import Userdao
from book import Book
from ownedbook import OwnedBook
from favoritebooks import FavoriteBooks
from bookdao import Bookdao
from ownedbooksdao import Ownedbooksdao
from favoritebooksdao import Favoritebooksdao
result_list = []
favorite_books = []
app = Flask(__name__)

@app.route('/')
def index():
	#print(image_url,file = sys.stderr)
	return render_template('login.html', **locals())

@app.route('/login',methods=['GET','POST'])
def login():
	# get account id from login and get account from db
	dao = Userdao()
	email = request.form['email']
	account = dao.selectByEmail(email)
	if account is not None:
		session['account'] = encode(account)
		session['email'] = encode(email)
		print('it is hitting this!', account, file = sys.stderr)
		return redirect(url_for('home'))
	
	else:
		return render_template('login.html', **locals())

@app.route('/registeruser',  methods=['GET', 'POST'])
def registeruser():
	user = request.form.get('email')
	password = request.form.get('pass')
	
	if(createUserIsValid(user,password)):
		dao = Userdao()
		new_user = User(user,password)
		dao.insert(new_user)
		print(new_user)
		return redirect(url_for('index'))
	else:
		return render_template('createuser.html')




@app.route('/home', methods = ['GET','POST'])
def home():
    book_dao = Ownedbooksdao()
    bookdao = Bookdao()
    if 'chosenbook' in request.form:
        book = request.form['chosenbook']
        bookchosen = bookdao.selectByIsbn(book)
        #print(f'BOOK CHOSEN IS {bookchosen}')
        session['chosenbook'] = book
        return redirect(url_for('checkbook'))
    else:
        dao = Userdao()
        account = decode(session['account'])
        
        
        list_of_books = book_dao.selectAll(account.user)
        print(list_of_books)
        all_books = []
        for isbn in list_of_books:
            new_book = bookdao.selectByIsbn(isbn.isbn)
            all_books.append(new_book)

        #print('List of books::',all_books,file = sys.stderr)
        return render_template('home.html', **locals())


@app.route('/checkbook', methods = ['GET','POST'])
def checkbook():
	bookchosen = session['chosenbook']
	book_dao = Bookdao()
	book = book_dao.selectByIsbn(bookchosen)
	return render_template('bookstats.html',**locals())
	
@app.route('/search', methods = ['GET','POST'])
def search():
	query = request.form.get('query')
	dao = Bookdao()
	result = ' '
	global result_list
	
	if query is not None:
		print(f'Result list is:{query}')
		result = dao.selectByTitle(query)
		if result is not None:
			result_list.append(result)	
		
		return render_template('searchforbook.html',**locals(),result_list = result_list)
	else:
		
		return render_template('searchforbook.html',**locals(),result_list = result_list)



@app.route('/select_book', methods=['GET','POST'])
def select_book():
	isbn = request.form['chosenbook']
	dao = Bookdao()
	print('BOOOK IN SELECT BOOK IS:',isbn)
	book = dao.selectByIsbn(str(isbn))
	print('BOOOK IN SELECT BOOK IS:',book)
	if book is not None:
		session['chosenbook'] = book.isbn
		return redirect(url_for('checkbook'))
	else:
		return redirect(url_for('search'))

#/favoritebook

@app.route('/favoritebook', methods=['GET','POST'])
def favoritebook():
	
	isbn = session['chosenbook']
	user = decode(session['email'])
	favoritebook = Favoritebooksdao()
	allfavorites = favoritebook.selectAll(user)

	all_isbns = [book.isbn for book in allfavorites]
	if isbn in all_isbns:
		favoritebook.delete(user,isbn)
		return redirect(url_for('favoritebooks'))
	bookadded = FavoriteBooks(user,isbn)
	favoritebook.insert(bookadded)
	return redirect(url_for('favoritebooks'))

@app.route('/favoritebooks', methods=['GET','POST'])
def favoritebooks():
	
	dao = Favoritebooksdao()
	bookdao = Bookdao()
	thumbnails = []
	user = decode(session['email'])
	#isbn = request.form['chosenbook']
	favoritebook = Favoritebooksdao()
	allfavorites = favoritebook.selectAll(user)
	for book in allfavorites:
		new_book = bookdao.selectByIsbn(str(book.isbn))
		thumbnails.append(new_book)

	return render_template('favoritebooks.html',**locals())



@app.route('/add_to_library', methods = ['GET','POST'])
def add_to_library():

	isbn = request.form['isbn']
	dao = Userdao()
	ownedbooks = Ownedbooksdao()
	get_account = decode(session['email'])
	all_user_books = ownedbooks.selectAll(get_account)
	for book in all_user_books:
		if str(isbn) == book.isbn:  # If the ISBN matches
			flash('Warning: This book is already in your library!')
			return redirect(url_for('search'))  # do javascript to put warning box maybe
	bookadded = OwnedBook(get_account,isbn)
	print(bookadded)
	ownedbooks.insert(bookadded)
	return redirect(url_for('search'))
		
@app.route('/deletebook', methods = ['GET','POST'])
def deletebook():
	dao = Userdao()
	bookdao = Ownedbooksdao()
	book_dao = Bookdao()
	account = decode(session['email'])
	isbn = request.form.get('chosenbook')
	if isbn is None:
		dao = Userdao()
		
		
		
		list_of_books = bookdao.selectAll(account)
		print(list_of_books)
		all_books = []
		for isbn in list_of_books:
			new_book = book_dao.selectByIsbn(isbn.isbn)
			all_books.append(new_book)
		return render_template('deletebook.html',**locals())

	else:
		bookdao.delete(isbn,account)
		return redirect(url_for('home'))











def createUserIsValid(user,password):
	print(user,password, file = sys.stderr)
	if(user is not None and password is not None):
		return True
		#dao.update(user)
	print('false',file = sys.stderr)
	return False

if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)