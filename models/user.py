from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, unique=True, primary_key=True)
  username = db.Column(db.String(32), unique=True, nullable=False)
  password = db.Column(db.String(80), nullable=False)
  role = db.Column(db.String(8), nullable=False, default='user')
  meals = db.relationship('Meal', backref='user', lazy=True)
