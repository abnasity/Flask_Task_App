from flask import render_template
from app import app
from app.models import User
from app.models import Task



@app.route('/')
def home():
    users = User.query.all()
    user_count = User.query.count()
    tasks = Task.query.all()
    task_count = Task.query.count()
   
    
    return render_template('index.html', user_count=user_count,  task_count=task_count, users=users, title='Home')


@app.route('/tasks')
def tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks, title='Tasks')



@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users, title='Users')

