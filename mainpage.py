import sqlite3
from flask import render_template
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

def ins_user(username, fullname, email, password):
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
	cursor = conn.execute("SELECT username, fullname, email, password from login")
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
		if ins_user(username, fullname, email, password):
			return redirect(url_for('main'))
			#return redirect(url_for('newregister.html')
		else:
			return "Error inserting temperature"		

#@app.route('/new_register', methods=['POST'])
#def new_reg():
#	return render_template('newregister.html')
#	if request.method == 'POST':


@app.route('/show_users', methods=['GET','POST'])
def list_users():
	table_users = get_users()
	return render_template('list_users_table.html', table_users=table_users)


@app.route('/login', methods=['GET','POST'])
def login_user():
	if request.method == 'GET':
		return render_template('login_page.html')
	elif request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		if get_users():
			return "WELCOME BACK!!!!!"
			#return redirect(url_for('ret_main'))
		else:
			return "ERROR --> INVALID username OR password"

#@app.route('/back', methods=['GET','POST'])
#def ret_main():
#	if request.method == 'GET':
#		return render_template('wel_back.html')
#	elif request.method == 'POST':
#		return redirect(url_for('main'))

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
