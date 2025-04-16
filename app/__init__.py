from  flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY']='837ff881ff74c5fc48e9a3e5b177960ca1db7488c6edf91a9b38f9f29250e5a0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///abnas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)







from app import routes