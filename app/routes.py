from flask import render_template
from app import app
from app.models import User


@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users, title='Home')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html', title='Tasks')

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users, title='Users')

