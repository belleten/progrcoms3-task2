from __future__ import print_function 
import sqlite3
from flask import render_template
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

def ins_user(username, fullname, email, password):  #function used to insert new users to the database
	conn = sqlite3.connect('userdatabase.db')
	try:   #here we try to insert the parameters values of new users into database, if done OK returns TRUE
		conn.execute("insert into login (username, fullname, email, password) values (?, ?, ?, ?)",(username, fullname, email, password))	
		conn.commit() 
		conn.close()
		return True  
	except:  #if the insert fails it returns FALSE
		return False

def get_users():    #function used to find users already in database
	conn = sqlite3.connect('userdatabase.db')
	cursor = conn.execute("SELECT username, fullname, email, password from login") #we select all values of each user from table named login
	data = [row for row in cursor] #data saves info for each row of table login
	conn.close()
	return data

def check_password(username_login,password_login): #function that checks if the username and password are already into database
	conn = sqlite3.connect('userdatabase.db')
	cursor = conn.execute("SELECT password from login WHERE username = ?",(username_login,)) #here we select the password that correspond to the username passed by the user 
	db_password =  cursor.fetchone() #this will give the lenght of password
	print(db_password)
	if db_password is None: #if the username doesn't exist, the database will tell that the lenght is less than 0 because it can't find a password matching a nonexisting username
		return False
	else:  #but if the username exists in the database it will give the value to db_password [0], meaning that we want the first into the list
		db_password = db_password[0] 
	if password_login == db_password: 
		return True   #if also the password given by the user is the same that we have into database it returns TRUE
	else:
		return False  #if not FALSE

@app.route('/')
def main():  #defines the landing page into the specified route
	return render_template('landingpage.html')

@app.route('/insert_user', methods=['GET','POST'])
def new_user():  #function that uses ins_user function and get and post methods into a html code to insert new users into database
	if request.method == 'GET':   
		return render_template('user_register_form.html') #it shows the html with the form to create new users ready to get the info
	elif request.method == 'POST': 
		username = request.form.get('username') 
		fullname = request.form.get('fullname')
		email = request.form.get('email')
		password = request.form.get('password')
		if ins_user(username, fullname, email, password):  
			return render_template('newregister.html')	

@app.route('/show_users')
def list_users():  #list an html page that shows all users into database
	table_users = get_users()
	return render_template('list_users_table.html', table_users=table_users)


@app.route('/login', methods=['GET','POST'])
def login_user():   #function to get the login info provided by the user and looking for it inside database data using get and post methods
	if request.method == 'GET':
		return render_template('login_page.html') #it gets the info using a html page
	elif request.method == 'POST':
		username_login = request.form.get('username')  
		password_login = request.form.get('password')
		if check_password(username_login,password_login): #uses check_password function to check if the username and password already exist inside database
			return render_template('wel_back.html') #if TRUE welcome back html page
		else:
			return render_template('invalid_log.html') #if FALSE incorrect login html page

if __name__ == '__main__': #for inicialize webapp
    app.debug = True
    app.run("0.0.0.0")
