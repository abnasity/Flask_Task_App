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
        flash(f'registration for {new_user.first_name} successfully!', 'success')
        return redirect(url_for('register'))
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
            user_id=1  
        )
        db.session.add(new_task)
        db.session.commit()
        flash(f'Task {new_task.title} added successfully!', 'success')
        return redirect(url_for('tasks'))
    print(form.errors)
    return render_template('tasks.html', title='Tasks', form=form)

@app.route('/toggle_task/<int:task_id>' , methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    flash(f'Task {task.title} updated successfully!', 'success')
    return redirect(url_for('home'))




@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f'User {user.username} deleted successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash(f'Task {task.title} deleted successfully!', 'success')
    return redirect(url_for('home'))
