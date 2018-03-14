from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os

app = Flask(__name__)

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


@app.route('/explore', methods=['GET','POST'])
def explore():
	"""
	Books from everyone
	"""	
	return render_template('explore.html')


@app.route('/mybooks', methods=['GET','POST'])
def mybooks():
	"""
	Books from everyone
	"""	
	return render_template('mybooks.html')


@app.route('/myreviews', methods=['GET','POST'])
def myreviews():
	"""
	Books from everyone
	"""	
	return render_template('myreviews.html')



if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=5000)