# Imports
import json
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from firebase import firebase

app = Flask(__name__)

FIREBASE_URL = 'https://engauge.firebaseio.com/'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app.config.from_object(__name__)

engauge_fb = firebase.FirebaseApplication(FIREBASE_URL)

@app.route('/')
def index():
    result = engauge_fb.get('/groups', None)
    return render_template('index.html', result=result)

@app.route('/group/<groupId>')
def group(groupId):
    groupInfo = engauge_fb.get('/groups/'+groupId, None) 
    qids = engauge_fb.get('/groups/'+groupId+'/questions', None)
    questions = []    

    for q in qids:
        questions.append(engauge_fb.get('/groups/'+groupId+'/questions/'+q, None))

    return render_template('group.html', groupInfo=groupInfo, questions=questions)


if __name__ == '__main__':
    app.run()
