from app import app

@app.route('/home')
def home():
    return "<h1>Welcome to the task manager!</>"