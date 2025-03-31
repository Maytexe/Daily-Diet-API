from database import db
from datetime import datetime

class Meal(db.Model):
  id = db.Column(db.Integer, unique=True, primary_key=True)
  name = db.Column(db.String(32), nullable=False)
  description = db.Column(db.String(80), nullable=False)
  date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
  time = db.Column(db.Time, nullable=False, default=datetime.utcnow)
  is_in_diet = db.Column(db.Boolean, default=False, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

