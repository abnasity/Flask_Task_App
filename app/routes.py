from flask import render_template,flash
from app import app, db
from app.models import User
from app.models import Task
from app.forms import TaskForm, UserForm
from flask import redirect, url_for



@app.route('/')
def home():
    users = User.query.all()
    user_count = User.query.count()
    tasks = Task.query.all()
    task_count = Task.query.count()
    return render_template('index.html', user_count=user_count,  task_count=task_count, users=users, tasks=tasks, title='Home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data, 
            first_name=form.first_name.data,
            last_name=form.last_name.data, 
            password=form.password.data)       
        
        db.session.add(new_user)
        db.session.commit()
        flash('User registered successfully!', 'success')
        return redirect(url_for('home'))
    print(form.errors)
    return render_template('register.html',title='Register', user_form=form)
    



@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            completed=form.completed.data,
            user_id=1  # Assuming a user ID of 1 for simplicity
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('tasks'))
    print(form.errors)
    return render_template('tasks.html', title='Tasks', form=form)





