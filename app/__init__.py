from  flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY']='837ff881ff74c5fc48e9a3e5b177960ca1db7488c6edf91a9b38f9f29250e5a0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///abnas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'



from app import models
from app import routes