# Imports
import os, json, collections
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from firebase import firebase

FIREBASE_URL = 'https://engauge.firebaseio.com/'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

FIREBASE_URL = 'https://engauge.firebaseio.com/'
firebase = firebase.FirebaseApplication(FIREBASE_URL, None)

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    result = firebase.get('/groups', None)
    return render_template('index.html', result=result)

@app.route('/group/<groupId>')
def group(groupId):
    groupInfo = firebase.get('/groups/'+groupId, None) 
    qids = firebase.get('/groups/'+groupId+'/questions', None)
    questions = []    

    for q in qids:
        questions.append(firebase.get('/groups/'+groupId+'/questions/'+q, None))

    return render_template('group.html', groupInfo=groupInfo, questions=questions)

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	result = convert(firebase.get('/users', None))
	usernames = []
	passwords = []
	for key, value in result.items():
		usernames.append(value.get('username'))
		passwords.append(value.get('password'))
		
	if request.method == 'POST':
		if request.form['username'] not in usernames:
			error = 'Invalid username'
		elif request.form['password'] not in passwords:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			return redirect(url_for('show_entries'))
	return render_template('index.html', error=error)

@app.route('/dashboard', methods=['GET', 'POST'])
def show_entries():
	if not session.get('logged_in'):
		flash("You're not logged in.")
		return redirect(url_for('login'))
	return render_template('dashboard.html')

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You have been logged out.')
	return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
