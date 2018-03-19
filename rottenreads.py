from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 


from models import *

@app.route('/', methods=['GET','POST'])
def home():
	"""
	Home Page
	"""	
	return render_template('home.html')


@app.route('/login', methods=['GET','POST'])
def login():
	"""
	The login page
	"""
	if request.method == 'POST':
		if request.form['username']:
			session['logged_in'] = True
			session['username'] = request.form['username']			
		else:
			flash('wrong password!')
		return redirect('/')
	else:
		if session.get('logged_in') == True:
		 	return redirect('/')
		else:
			return render_template('login.html')


@app.route('/books', methods=['GET','POST'])
def explore():
	"""
	GET - Books from everyone 
	POST - Add a book (Check for duplicate ISBN)
	"""
	if request.method == 'GET':
		books = Book.query.all()
		return render_template('explore.html', books = books)
	elif request.method == 'POST':
		if not 'username' in session:
			return render_template('login.html')
		else:
			username = session['username']
			error_message = add_book_validation(request)
			if len(error_message) <= 0:			
				book = Book(isbn=request.form['isbn'],title=request.form['title'],author=request.form['author'],
				description=request.form['description'], added_by=username, added_date=datetime.now())
				db.session.add(book)
				db.session.commit()
				flash('Book has been added')
			else:
				flash(error_message)
			books = Book.query.filter_by(added_by=username)	
			return render_template('mybooks.html', books=books)


@app.route('/mybooks', methods=['GET'])
def mybooks():
	"""
	Get books by username
	"""
	if 'username' in session:
		username = session['username']
		books = Book.query.filter_by(added_by=username)	
		return render_template('mybooks.html', books=books)
	else:
		return render_template('mybooks.html')



@app.route('/books/<isbn>', methods=['GET','POST'])
def get_book(isbn):
	"""
	Book page for given ISBN - contains book info and reviews (GET)
	Post a review (POST)
	"""
	if request.method == 'GET':
		book = Book.query.filter_by(isbn=isbn).first()
		reviews = Review.query.filter_by(isbn=isbn)
		return render_template('book.html', book=book, reviews=reviews, overall_rating=get_overall_rating(isbn))
	elif request.method == 'POST':
		error_message = add_review_validation(request, isbn)
		if len(error_message) <= 0:
			review = Review(isbn=isbn, title=request.form['title'], star=request.form['rating'], comment=request.form['comment'], added_by=session['username'], added_date=datetime.now())
			book = Book.query.filter_by(isbn=isbn).first()
			db.session.add(review)
			db.session.commit()
			reviews = Review.query.filter_by(isbn=isbn)
			flash('Review has been added.')
			return render_template('book.html', book=book, reviews=reviews, overall_rating=get_overall_rating(isbn))
		else:
			flash(error_message)
			book = Book.query.filter_by(isbn=isbn).first()
			reviews = Review.query.filter_by(isbn=isbn)
			return render_template('book.html', book=book, reviews=reviews, overall_rating=get_overall_rating(isbn))

@app.route('/myreviews', methods=['GET'])
def get_my_reviews():
	"""
	Get my reviews
	"""
	if not 'username' in session:
		return render_template('myreviews.html')
	else:
		username = session['username']
		reviews_plus = Review.query.filter_by(added_by=username)
		return render_template('myreviews.html', reviews=reviews_plus)



@app.route('/logout')
def logout():
	session['logged_in'] = False
	session.clear()
	return redirect('/')



def is_duplicate_review(username, isbn):
	"""
	Check if the review for person and book already exists
	"""
	review = Review.query.filter_by(added_by=username, isbn=isbn).first()
	if review:
		return True
	else:
		return False

def is_duplicate_book(isbn):
	"""
	Check if the book is duplicate
	"""
	book = Book.query.filter_by(isbn=isbn).count()
	if book > 0:
		return True
	else:
		return False

def get_overall_rating(isbn):
	"""
	Gets the overall rating of a book
	"""
	overall_rating = 0
	if does_review_exist:
		overall_rating_query = "select AVG(star) as average from reviews where isbn='{}'".format(isbn)
		overall_rating_result = db.engine.execute(overall_rating_query)
		for avg in overall_rating_result:
			overall_rating = avg[0]
	return overall_rating
	


def does_review_exist(isbn):
	"""
	Check if a review exists for a book
	"""
	review = Review.query.filter_by(isbn=isbn).filter_by(added_by=session['username']).count()
	if review > 0:
		return True
	else:
		return False


def add_book_validation(request):
	"""
	Validate book addition
	"""
	error_string = ""
	if not request.form['isbn']:
		error_string += 'ISBN is mandatory. '
	else:
		if is_duplicate_book(request.form['isbn']):
			error_string += 'ISBN already exists. '
	if not request.form['title']:
		error_string += 'Title is mandatory. '
	if not request.form['author']:
		error_string += 'Author is mandatory. '

	return error_string


def add_review_validation(request, isbn):
	"""
	Validate reviews
	"""
	error_string = ""
	if does_review_exist(isbn):
		error_string += 'You can only add one review per book. '
	if not 'rating' in request.form:
		error_string += 'Star Rating is mandatory. '

	return error_string



# return redirect(url_for('foo'))


if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=5000)
