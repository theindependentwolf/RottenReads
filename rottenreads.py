from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('home.html')


@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		if request.form['username']:
			session['logged_in'] = True			
		else:
			flash('wrong password!')
		return redirect('/')
	else:
		return render_template('login.html')


if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=5000)