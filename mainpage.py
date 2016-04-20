import sqlite3
from flask import render_template
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

def ins_user(username, fullname, email, password)
	conn = sqlite3.connect('userdatabase.db')
	try:
		conn.execute("insert into login (username, fullname, email, password) values (?, ?, ?, ?)",(username, fullname, email, password))
		conn.commit()
		conn.close()
		return True
	except:
		return False

def get_users():
	conn = sqlite3.connect('userdatabase.db')
	cursor = conn.execute("SELECT username, fullname, email, password")
	data = [row for row in cursor]
	conn.close()
	return data


@app.route('/')
def main():
	return render_template('landingpage.html')

@app.route('/insert_user', methods=['GET','POST'])
def new_user():
	if request.method == 'GET':
		return render_template('user_register_form.html')
	elif request.method == 'POST':
		username = request.form.get('username')
		fullname = request.form.get('fullname')
		email = request.form.get('email')
		password = request.form.get('password')

