from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.column(db.integer, primary_key=True)
    username = db.column(db.string(50), nullable=False, unique=True)
    first_name = db.column(db.string(50), nullable=False)
    last_name = db.column(db.string(50), nullable=False)
    password = db.column(db.string(200), nullable=False)
    task = db.relationship('Task', backref='user', lazy=True)
    
    
def display_user(self):
        return f"User ID: {self.user_id}, Username: {self.user_name}, Name: {self.first_name} {self.last_name}"

def display_tasks(self):
        if not self.tasks:
            return f"{self.user_name} has no tasks."
        return "\n".join([task.display_task() for task in self.tasks])
    
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.column(db.integer, primary_key=True)
    title = db.column(db.string(100), nullable=False)
    description = db.column(db.Text, nullable=False)
    completed = db.column(db.Boolean, default=False)
    user_id = db.column(db.integer, db.ForeignKey('users.id'), nullable=False)
    
    
def display_task(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task ID: {self.task_id}, Title: {self.title}, Status: {status}, Description: {self.description}"